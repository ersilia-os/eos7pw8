# imports
import os
import sys
import csv
from rdkit import Chem
import joblib

import pathlib 




# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

model_path = os.path.join( pathlib.Path(os.path.dirname(os.path.abspath(__file__))).parent.parent ,'checkpoints', 'syba.joblib')


# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]
        
        
def my_model(smiles, model):
    preds = []
    syba_model = joblib.load(model)
    for smi in smiles:
        mol = Chem.MolFromSmiles(smi)
        if mol is None:
            preds.append(None)
        else:
            preds.append(syba_model.predict(mol=mol))
    return preds

#run model

outputs = my_model(smiles_list, model_path)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["value"])  # header
    for o in outputs:
        writer.writerow([o])
