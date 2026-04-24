from langchain.document_loaders import PyPDFium2Loader, PyPDFDirectoryLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from typing import List
from langchain.schema import Document
from typing import List 
from langchain.schema import Document



#extract Data from the pdf file 
def load_pdf_files(data):
    
    # Cria um loader (carregador) de documentos a partir de um diretório
    loader = DirectoryLoader(
        
        data,  # Caminho da pasta onde estão os arquivos PDF
        
        glob="*.pdf",  # Define que ele deve pegar apenas arquivos com extensão .pdf
        
        loader_cls=PyPDFium2Loader  # Define qual classe será usada para ler os PDFs
                                     # (nesse caso, PyPDFium2Loader, que extrai o texto dos PDFs)
    )

    documents = loader.load()
    return documents

# split the document into smaller chunks 
def text_split(minimal_docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20, 
        )
    texts_chunk = text_splitter.split_documents(minimal_docs)
    return texts_chunk

def download_embedding():
    #download and return the Hugging face embeddings model.

    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
    )
    return embeddings

def filter_to_minimal_docs(docs: list[Document]) -> List[Document]:
    #given a list of document objects, return a new list of document objects containing only 'source' in metadata and the original page_content
    minimal_docs: list[Document] = []


    minimal_docs: list[Document]
    for doc in docs:
        src = doc.metadata.get("source")
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={"source":src}
                )
            )
    return minimal_docs