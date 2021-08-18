import pandas as pd

from {{cookiecutter.package_name}} import __version__ as _version
from {{cookiecutter.package_name}}.config.logging_config import ProcessLogger
from {{cookiecutter.package_name}}.config import config

ProcessLogger = ProcessLogger(__name__)

def load_excel(*, file_name: str) -> pd.DataFrame:
    ProcessLogger.processLogger.info(f" Loading data: {file_name}")
    _data = pd.read_excel(f"{config.INPUT_DIR}/{file_name}")
    ProcessLogger.processLogger.info(f" Data dimensions: {_data.shape}")
    return _data

def export_excel(*, data: pd.DataFrame, file_name: str) -> None:
    data.to_excel(f"{config.OUTPUT_DIR}/{file_name}_v{_version}_{config.TODAY}.xlsx", index=False)
    return None

def export_artifact_excel(*, data: pd.DataFrame, file_name: str) -> None:
    data.to_excel(f"{config.PROCESS_ARTIFACT_DIR}/{file_name}.xlsx", index=False)
    return None