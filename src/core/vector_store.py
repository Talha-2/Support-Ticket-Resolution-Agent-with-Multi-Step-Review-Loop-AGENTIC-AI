from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS as CommunityFAISS
from langchain.docstore.document import Document


# Mock knowledge base for FAISS
documents = [
    Document(page_content="Billing FAQ: Refunds processed in 5-7 days.", metadata={"category": "Billing"}),
    Document(page_content="Check payment status in account settings.", metadata={"category": "Billing"}),
    Document(page_content="Error 403: Clear cache or reset password.", metadata={"category": "Technical"}),
    Document(page_content="Login issues: Verify credentials or contact support.", metadata={"category": "Technical"}),
    Document(page_content="Security alert: Change password immediately.", metadata={"category": "Security"}),
    Document(page_content="Enable 2FA for account protection.", metadata={"category": "Security"}),
    Document(page_content="General support: Contact us at support@example.com.", metadata={"category": "General"}),
    Document(page_content="FAQs available on our website.", metadata={"category": "General"}),]

embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_store = FAISS.from_texts(
    texts=[doc.page_content for doc in documents],
    embedding=embedding_function,
    metadatas=[doc.metadata for doc in documents]
)