from sklearn.pipeline import Pipeline
from {{cookiecutter.package_name}}.config.config import config
from processing import preprocessors as pp
from {{cookiecutter.package_name}}.config.logging_config import ProcessLogger

############################## ANALYSIS AND OUTPUT #########################
############################################################################

###
### DATA CLEANING
###


analysis_pipeline = Pipeline(
    [
        (
            "Analysis pipeline step One",
            print('Step one')
        ),
        (
            "Analysis pipeline Step Two",
            print('Step two')
        )
    ]
)