# project_templates

The purpose of this package is to establish a framework for producing data analytical results.
A well defined workflow and project structure enhances clarity and predictability by facilitating
familiarity, transparency, reproducibility and inclusion of fail-safe mechanisms.

This package aims to be flexible in the sense that it provides a guiding framework of components which can be adapted,
modified and added to depending on project-specific context and needs. As such, this framework is designed to help
and encourage technical project implementation by acting as a guide for working within a clean and logical structure.

By using this package you will:
    - Find it easier to include and collaborate with others on your project.
    - Feel more confident in the results and output yielded by your analysis.
    - Easier identify, locate and rectify errors or incorrect results and output.
    - Avoid confusion of which exact data to use, which cleaning steps to take, when and where.
    - Be able to more easily branch out in different directions and roll back changes.

Create cross-project coherence.


### Project directory structure

------------
```
[ROOT]
├── packages/
│   ├── project_api /                                   <- Description.
│   ├── project_package /                               <- Description.
|   │   │   ├── requirements.txt                        <- Requirements file for reproducing analysis.
|   │   │   ├── tox.ini                                 <- tox file with settings for running tox; set up environment and run tests and package.
|   │   │   └── project_package/
|   │   │   |   ├── .env                                <- Environment file for storing user credentials for use throughout package (DO NOT SHARE!)
|   │   │   |   ├── VERSION                             <- File for specifying current version for traceability and reproducibility.
|   │   │   |   ├── config.yml                          <- File for specifying constants for use throughout package (variables, names, etc.)
|   │   │   |   ├── main.py                             <- Central script for collecting modules and running package.
|   │   │   |   ├── assets/                             <- Folder for storing any form of assets (documents, files, images..) for use through package.
|   │   │   |   ├── config/
|   |   │   │   |   ├── config.py                       <- Script for path specifications, collecting and verifying specifications in config.yml.
|   |   │   │   |   └── logging_config.py               <- Script for specifying logging configurations for use throughout the package.
|   │   │   |   ├── graphs/
|   |   │   │   |   └── graphs.py                       <- Script for defining design and functionality for creating graphs.
|   │   │   |   ├── modeling/
|   |   │   │   |   └── regression/
|   |   |   |   │   │   ├── regression_models.py        <- Script for defining regression models.
|   |   |   |   │   │   └── regression_resources.py     <- Script for capturing and exporting regression model output.
|   │   │   |   ├── processing/
|   |   │   │   |   ├── data_management.py              <- Script for managing data files; load and export.   
|   |   │   │   |   ├── preprocessors.py                <- Script defining data preprocessing steps for inclusion into pipeline.
|   |   │   │   |   ├── analyzers.py                    <- Script defining data analysis steps for inclusion into pipeline.
|   |   │   │   |   └── errors.py                       <- Script defining and handling custom errors [Should be moved to config/ perhaps]
|   │   │   |   ├── pipelines/
|   |   │   │   |   ├── preprocessing_pipeline.py       <- Script for collecting and organizing data preprocessing steps.
|   |   │   │   |   └── analysis_pipeline.py            <- Script for collecting and organizing data analysis steps.
|   │   │   |   ├── input/
|   |   │   │   |   └── raw_data.xlsx                   <- Original unchanged data.
|   │   │   |   ├── output/
|   |   │   │   |   ├── processed_data.xlsx             <- Final data file for analysis and output production.
|   |   │   │   |   ├── graph_output/                   <- Graph files: graph files (.png)
|   |   │   │   |   ├── tabular_output/                 <- Table files: tabulations of frequencies and statistical tests.
|   |   │   │   |   └── regression_output/              <- Regression files: serialized (.pkl), model results (.xlsx and .pdf)
|   │   │   |   └── tests/
|   |   │   │   |   ├── unittest.py                     <- Modules for unit testing (ensure that correct output is produced.)
```