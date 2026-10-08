"""One-off conversion of the SYBA checkpoint (not used at prediction time).

syba.joblib is a pickled SybaClassifier whose fragment table is a Python dict of
26.4M entries {fragment id: (present score, absent score)}. Unpickling millions of
Python objects took ~50 s on every run. This script stores the same numbers as
plain numpy arrays, which load in under a second:

    keys          sorted fragment ids (uint32; Morgan ids are 32-bit)
    score_index   for each key, a row in score_table (uint16)
    score_table   the 31,757 distinct (present, absent) score pairs (float64)
    all_off_frags_score   the classifier's starting score (float64)

Values are copied exactly (float64 is the same type as Python's float).

Usage: python convert_checkpoint.py syba.joblib syba_fragments.npz
"""

import sys

import joblib
import numpy as np

joblib_path, npz_path = sys.argv[1], sys.argv[2]
classifier = joblib.load(joblib_path)

keys = np.array(sorted(classifier.fragments), dtype=np.uint32)
pairs = np.array([classifier.fragments[k] for k in keys.tolist()], dtype=np.float64)
score_table, score_index = np.unique(pairs, axis=0, return_inverse=True)
assert len(score_table) < 2**16, "too many distinct score pairs for uint16"

np.savez(
    npz_path,
    keys=keys,
    score_index=score_index.reshape(-1).astype(np.uint16),
    score_table=score_table,
    all_off_frags_score=np.float64(classifier.ALL_OFF_FRAGS_SCORE),
)
