from sklearn.pipeline import Pipeline
from {{cookiecutter.package_name}}.config.config import config
from processing import preprocessors as pp
from {{cookiecutter.package_name}}.config.logging_config import ProcessLogger

############################## PREPROCESSING #########################
######################################################################

###
### DATA CLEANING
###


preprocessing_pipeline = Pipeline(
    [
        (
            "Preprocessing pipeline step One",
            print('Step one')
        ),
        (
            "Preprocessing pipeline Step Two",
            print('Step two')
        )
    ]
)