from {{cookiecutter.package_name}} import __version__ as _version
from {{cookiecutter.package_name}}.config.config import config
from {{cookiecutter.package_name}}.config.logging_config import ProcessLogger
from {{cookiecutter.package_name}}.processing.data_management import load_excel, export_excel
from {{cookiecutter.package_name}}.pipelines.preprocessing_pipeline import preprocessing_pipeline
from {{cookiecutter.package_name}}.pipelines.analysis_pipeline import analysis_pipeline

from dotenv import find_dotenv, load_dotenv



ProcessLogger = ProcessLogger(__name__)

def main():


    ProcessLogger.processLogger.info(f"======== Starting process with version: {_version} ======== \n")
    
    ### LOAD CREDENTIALS
    load_dotenv(find_dotenv())


    ### LOAD DATA
    raw_df = load_excel(file_name=config.package_config.raw_data)
    ProcessLogger.processLogger.info(f"Running pipeline: \n {preprocessing_pipeline}")
    
    ### PROCESS DATA
    processed_df = preprocessing_pipeline.fit_transform(raw_df)
    export_excel(data= processed_df, file_name=f"example_data_processed")

    ### ANALYZE DATA
    ProcessLogger.processLogger.info(f"Running pipeline: \n {analysis_pipeline}")
    analysis_pipeline.fit_transform(processed_df)

    ProcessLogger.processLogger.info(f"=========== END =========== \n \n")




if __name__=='__main__':
    main()
    