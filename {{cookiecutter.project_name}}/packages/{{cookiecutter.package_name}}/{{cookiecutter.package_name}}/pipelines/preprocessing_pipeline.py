from sklearn.pipeline import Pipeline
from {{cookiecutter.package_name}}.config.config import config
#from processing import preprocessors as pp
from {{cookiecutter.package_name}}.processing import preprocessors as pp
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
            pp.ExtractSubsetVariables(variables=config.model_config.variables_to_include)
        ),
        (
            "Preprocessing pipeline Step Two",
            print('Step two')
        )
    ]
)