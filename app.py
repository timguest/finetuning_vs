from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os
from constants import API_KEY
from langchain.chains.qa_with_sources import load_qa_with_sources_chain

from flask import Flask, render_template, request, jsonify
os.environ["OPENAI_API_KEY"] = API_KEY

app = Flask(__name__)

def process_question(query):
    path = ('Bob_small.pdf')
    reader = PdfReader(path)

    # read data from the file and put them into a variable called raw_text
    raw_text = ''
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            raw_text += text

    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    texts = text_splitter.split_text(raw_text)

    # Download embeddings from OpenAI
    embeddings = OpenAIEmbeddings()
    docsearch = FAISS.from_texts(texts, embeddings)
    chain = load_qa_chain(OpenAI(), chain_type="stuff")

    # search in the embeddings, symantacaly
    docs = docsearch.similarity_search(query)
    return_answer = chain.run(input_documents=docs, question=query)
    chain = load_qa_with_sources_chain(OpenAI(), chain_type="stuff")
    return_answer = chain({"input_documents": docs, "question": query}, return_only_outputs=True)
    return return_answer


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        question = request.form.get('msg')
        answer = process_question(question)  # get answer from your module
        return jsonify({'answer': answer})  # return answer as JSON

    return render_template("chat.html")

if __name__ == "__main__":
    app.run(debug=True)
