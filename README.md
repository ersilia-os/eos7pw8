# Synthetic accessibility score

## Model Identifiers
- Slug: syba-synthetic-accessibility
- Ersilia ID: eos7pw8
- Tags: synthesis,	physchem,	generative

## Model Description
Bayesian prediction of the synthetic accessibility score of organic compounds 
- Input: SMILES
- Output: SYBAScore	(Measure of the confidence of the prediction (higher values indicate higher confidence that the molecule is synthetically accessible))
- Model type: Regression
- Mode of Training: Pretrained
- Training data: 693,353	(https://github.com/lich-uct/syba/tree/master/syba/resources)
- Experimentally validated: No

## Source code
This model was published by Voršilák, M., Kolář, M., Čmelo, I. et al. SYBA: Bayesian estimation of synthetic accessibility of organic compounds. J Cheminform 12, 35 (2020). DOI: https://doi.org/10.1186/s13321-020-00439-2
- Code: https://github.com/lich-uct/syba
- Chedkpoints: https://github.com/lich-uct/syba/tree/master/bin

## License
The GPL-v3 license applies to all parts of the repository. This repository uses the externally maintained library "syba", located at `/model`

## History
- This model was downloaded and incorporated on October 25, 2021
