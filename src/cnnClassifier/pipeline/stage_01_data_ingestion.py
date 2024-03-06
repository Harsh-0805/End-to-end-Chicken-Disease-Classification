from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger

STAGE_NAME = "Data Ingestion"

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        logger.info(f"Starting {STAGE_NAME}...")
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} <<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"stage {STAGE_NAME} completed successfully")
    except Exception as e:
        logger.error(f"stage {STAGE_NAME} failed! Error: {e}")
        raise e