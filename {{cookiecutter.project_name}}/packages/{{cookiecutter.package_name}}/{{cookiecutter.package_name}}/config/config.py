# External libraries
from pathlib import Path
from typing import Dict, List, Sequence

from pydantic import BaseModel
from strictyaml import YAML, load
import datetime as dt

import {{cookiecutter.package_name}}

# DIRECTORY PATHS
"""
This section defines the directory structure for consistent 
use in modules across the package.
"""

TODAY = dt.datetime.today().strftime("%Y-%m-%d")

#PACKAGE_ROOT = pathlib.Path().resolve()
PACKAGE_ROOT = Path({{cookiecutter.package_name}}.__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent
INPUT_DIR = f"{PACKAGE_ROOT}/input"
ASSET_DIR = f"{PACKAGE_ROOT}/assets"
OUTPUT_DIR = f"{PACKAGE_ROOT}/output"
CONFIG_FILE_PATH = PACKAGE_ROOT/"config.yml"
PROCESS_ARTIFACT_DIR = f"{PACKAGE_ROOT}/output/process_artifacts"

class PackageConfig(BaseModel):
    """
    Package information config.
    """

    package_name: str
    raw_data: str
    processed_data: str
    train_data_file: str
    test_data_file: str
    preprocess_pipeline_name: str
    analysis_pipeline_name: str
    preprocessing_pipeline_save_file: str
    analysis_pipeline_save_file: str


class ModelConfig(BaseModel):
    """
    All configurations pertaining to
    data processing and model fitting.
    """

    variables_to_include: List[str]
    variance_threshold: float
    alpha: float
    random_state: int
    test_size: float

class LogisticRegressionModelConfig(BaseModel):
    """
    All configurations pertaining to
    the logistic regression.
    """

    dependent_variable: str
    independent_variables: List[str]

class BinaryGraphConfig(BaseModel):
    """
    All configurations pertaining to
    the logistic regression.
    """

    binary_graph_dependent_variables: List[str]
    binary_graph_independent_variables: List[str]

class GraphStyleConfig(BaseModel):
    barchart_colors: List[str]
    
class Config(BaseModel):
    ''' 
    Core config object.
    Collects config.yml, PackageConfig, ModelConfig.
    '''

    package_config: PackageConfig
    model_config: ModelConfig
    logistic_regression_config: LogisticRegressionModelConfig
    binary_graph_config: BinaryGraphConfig
    graph_style_config: GraphStyleConfig

def detect_config_file() -> Path:
    '''
    Identify configuration.yml.
    '''
    if CONFIG_FILE_PATH.is_file():
        return CONFIG_FILE_PATH
    else:
        raise Exception(f"Config.yml not found in {CONFIG_FILE_PATH}")

def extract_configurations_from_yml(config_path: Path = None) -> YAML:
    '''
    Parse YAML for package and model configurations.
    '''

    if not config_path:
        config_path = detect_config_file()
    if config_path:
        with open(config_path, 'r') as config_file:
            parsed_config_file = load(config_file.read())
            return parsed_config_file
    else:
        raise OSError(f"No configuration fle found in {config_path}")

def create_and_validate_configurations(parsed_config_file: YAML = None) -> Config:
    '''
    Run valdidation procedure for configuration information.
    '''
    if parsed_config_file is None:
        parsed_config_file = extract_configurations_from_yml()
    
    _config = Config(
        package_config=PackageConfig(**parsed_config_file.data),
        model_config=ModelConfig(**parsed_config_file.data),
        logistic_regression_config=LogisticRegressionModelConfig(**parsed_config_file.data),
        binary_graph_config=BinaryGraphConfig(**parsed_config_file.data),
        graph_style_config=GraphStyleConfig(**parsed_config_file.data)
    )

    return _config

config = create_and_validate_configurations()