# Bayesian prediction of synthetic accessibility

SYBA uses a fragment-based approach to classify whether a molecule is easy or hard to synthesize, and it can also be used to analyze the contribution of individual fragments to the total synthetic accessibility. The easy-to-synthesize dataset is an extract of the ZINC purchasable compounds, and the hard-to-synthesize dataset is generated using a Nonpher approach (introducing small molecular perturbations to transform molecules into more complex compounds). The fragments are calculated with ECFP8 descriptors, and independence between fragments is assumed.

This model was incorporated on 2021-10-25.

## Information
### Identifiers
- **Ersilia Identifier:** `eos7pw8`
- **Slug:** `syba-synthetic-accessibility`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `Any`
- **Target Organism:** `Not Applicable`
- **Tags:** `Synthetic accessibility`, `Chemical synthesis`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Higher score indicates higher confidence that the molecule is synthetically available

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| syba_score | float | high | Synthetic accessibility score |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos7pw8](https://hub.docker.com/r/ersiliaos/eos7pw8)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7pw8.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7pw8.zip)

### Resource Consumption
- **Model Size (Mb):** `757`
- **Environment Size (Mb):** `576`


### References
- **Source Code**: [https://github.com/lich-uct/syba](https://github.com/lich-uct/syba)
- **Publication**: [https://jcheminf.biomedcentral.com/articles/10.1186/s13321-020-00439-2](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-020-00439-2)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2020`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-only](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos7pw8
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos7pw8
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
