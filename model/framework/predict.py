import sys
import csv

from rdkit import Chem
from syba.syba import SybaClassifier

syba = SybaClassifier()
syba.fitDefaultScore()

infile = sys.argv[1]
outfile = sys.argv[2]

with open(infile, "r") as f:
    reader = csv.reader(f)
    next(reader)
    smiles = []
    for r in reader:
        smiles += [r[0]]

preds = []
for smi in smiles:
    mol = Chem.MolFromSmiles(smi)
    if mol is None:
        preds += [None]
    else:
        preds += [syba.predict(mol=mol)]

with open(outfile, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["score"])
    for p in preds:
        if p is None:
            p = ""
        writer.writerow([p])
