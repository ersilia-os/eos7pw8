# imports
import os
import sys
import csv
from rdkit import Chem
from rdkit.Chem import AllChem  # GetMorganFingerprint lives here (as in the syba library)
import numpy as np
from syba.syba import SybaClassifier

import pathlib




# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# OPTIMIZATION: the model now reads syba_fragments.npz instead of syba.joblib.
# syba.joblib was a 792 MB pickled SybaClassifier whose 26.4M-entry Python dict
# took ~50 s to unpickle on every run, while predicting took milliseconds.
# The .npz holds the same numbers as plain arrays (159 MB, loads in ~0.1 s).
# It was made with convert_checkpoint.py (see that file for the format).
model_path = os.path.join( pathlib.Path(os.path.dirname(os.path.abspath(__file__))).parent.parent ,'checkpoints', 'syba_fragments.npz')

# SYBA settings used by the original checkpoint: Morgan radius 4, and the
# library's default chiral scores (checked equal to those in syba.joblib).
NEIGHBOURHOOD = 4
CHIRAL_SCORER = SybaClassifier()


# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]


def syba_predict(mol, table):
    """Same calculation as SybaClassifier.predict, using the array tables.

    Looks up each Morgan fragment of the molecule in the sorted keys, and applies
    the scores in the same order as the library, so results are bit-identical.
    """
    score = float(table["all_off_frags_score"])
    fragments = list(AllChem.GetMorganFingerprint(mol, NEIGHBOURHOOD).GetNonzeroElements())
    # uint32 like the keys: with Python ints, numpy would convert all 26M keys
    # to int64 on every call (Morgan fragment ids always fit in 32 bits)
    positions = np.searchsorted(table["keys"], np.array(fragments, dtype=np.uint32))
    for fragment, pos in zip(fragments, positions):
        if pos < len(table["keys"]) and table["keys"][pos] == fragment:
            present_score, absent_score = table["score_table"][table["score_index"][pos]]
            score -= float(absent_score)
            score += float(present_score)
    score += CHIRAL_SCORER._getChiralScore(mol, includeAbsentChiralities=True)
    return score


def my_model(smiles,model):
    preds = []
    try:
        with np.load(model) as data:
            table = {name: data[name] for name in data.files}
        for smi in smiles:
            mol = Chem.MolFromSmiles(smi)
            if mol is None:
                preds.append(None)
            else:
                preds.append(syba_predict(mol, table))
        return preds
    except Exception as e:
        print(f"Error occurred while loading the model: {str(e)}")
        sys.exit(0)



outputs = my_model(smiles_list, model_path)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["syba_score"])  # header
    for o in outputs:
        writer.writerow([o])

