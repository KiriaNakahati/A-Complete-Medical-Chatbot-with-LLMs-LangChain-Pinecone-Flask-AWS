from dotenv import load_dotenv
import os 
from src.helper import load_pdf_files, filter_to_minimal_docs, text_split, download_embedding
from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

extracted_data = load_pdf_files(
    os.getenv("PATH_DATA")
)
minimal_docs = filter_to_minimal_docs(extracted_data)
text_chunk = text_split(minimal_docs)


embedding = download_embedding()

pinecone_api_key = PINECONE_API_KEY

pc = Pinecone(api_key=pinecone_api_key)

index_name= "medical-chatbot"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384, #dimension of embedding
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )
    
index = pc.Index(index_name)


docsearch = PineconeVectorStore.from_documents(
    documents=text_chunk,
    embedding=embedding,
    index_name=index_name
    )