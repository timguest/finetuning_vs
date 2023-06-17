from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS

# Get your API keys from openai, you will need to create an account.
# Here is the link to get the keys: https://platform.openai.com/account/billing/overview
import os
API_KEY = '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'
os.environ["OPENAI_API_KEY"] = API_KEY

path = ('Bob_small.pdf')
path = ('/Users/tgast004/Documents/Bob.pdf')

reader = PdfReader(path)

# read data from the file and put them into a variable called raw_text
raw_text = ''
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        raw_text += text

text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 1000,
    chunk_overlap  = 200,
    length_function = len,
)
texts = text_splitter.split_text(raw_text)

# Download embeddings from OpenAI
embeddings = OpenAIEmbeddings()

# convert text to embedding
# this will convert the text to embedding and store it.
docsearch = FAISS.from_texts(texts, embeddings)

# question answer chain
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

# you cna choose different models of gpt.
chain = load_qa_chain(OpenAI(), chain_type="stuff")

query = "What kind of products do you have in store? and do i need to wear a mask in the store?"
# search in the embeddings, symantacaly
docs = docsearch.similarity_search(query)
hoi = chain.run(input_documents=docs, question=query)

print(hoi)