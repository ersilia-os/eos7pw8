# Bayesian prediction of synthetic accessibility

SYBA uses a fragment-based approach to classify whether a molecule is easy or hard to synthesize, and it can also be used to analyze the contribution of individual fragments to the total synthetic accessibility. The easy-to-synthesize dataset is an extract of the ZINC purchasable compounds, and the hard-to-synthesize dataset is generated using a Nonpher approach (introducing small molecular perturbations to transform molecules into more complex compounds). The fragments are calculated with ECFP8 descriptors, and independence between fragments is assumed.

## Identifiers

* EOS model ID: `eos7pw8`
* Slug: `syba-synthetic-accessibility`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Regression`
* Output: `Score`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Higher score indicates higher confidence that the molecule is synthetically available

## References

* [Publication](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-020-00439-2)
* [Source Code](https://github.com/lich-uct/syba)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos7pw8)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7pw8.zip)

## Citation

If you use this model, please cite the [original authors](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-020-00439-2) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a GPL-3.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!