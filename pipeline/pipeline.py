from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender

from config.config import GROQ_API_KEY,MODEL_NAME

from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class AnimeRecommenderPipeline:
    def __init__(self, persist_dir:str="chroma_db"):
        try:
            logger.info("Initializing Anime Recommender Pipeline...")

            vector_builder = VectorStoreBuilder(csv_path="", persist_dir=persist_dir)
            retriever = vector_builder.load_vector_store().as_retriever()
            self.recommender = AnimeRecommender(retriever, GROQ_API_KEY, MODEL_NAME)

            logger.info("Pipeline initialized successfully...")
        except Exception as e:
            logger.error(f"Failed to intialize pipeline {str(e)}")
            raise CustomException(f"Error initializing pipeline: {e}")

    def recommend(self, query:str) -> str:
        try:
            logger.info(f"Recived a query {query}")

            recommendation = self.recommender.get_recommendation(query)

            logger.info("Recommendation generated sucesfulyy...")
            return recommendation
        except Exception as e:
            logger.error(f"Failed to get recommendation {str(e)}")
            raise CustomException("Error during getting recommendation" , e)