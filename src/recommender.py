from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from src.prompt_template import get_anime_prompt

class AnimeRecommender:
    def __init__(self, retriever, api_key:str, model_name:str):
        self.llm = ChatGroq(api_key=api_key,model=model_name,temperature=0)
        self.prompt = get_anime_prompt()

        """
        Creates a chain that retrieves relevant documents ("context") using the retriever,
        then passes both the context and your query (mapped to "question") to the prompt template.
        When you call self.qa_chain({"query": query}), the chain automatically:
            - Uses the retriever to get the context for your query.
            - Fills the prompt template with the retrieved context and your query.
        """
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt":self.prompt}
        )

    def get_recommendation(self,query:str):
        result = self.qa_chain({"query":query})
        return result['result']