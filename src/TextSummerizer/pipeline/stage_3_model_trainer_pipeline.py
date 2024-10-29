from src.TextSummerizer.config.configuration import ConfigurationManager
from src.TextSummerizer.components.model_trainer import ModelTrainer
from src.TextSummerizer.logging import logger

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    def initiate_model_trainer(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()