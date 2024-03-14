# import libraries
import os
import streamlit as st
from pinecone import Pinecone
from llama_index.vector_stores.pinecone import PineconeVectorStore
from llama_index.core import VectorStoreIndex

# configure
pinecone_api_key = st.secrets["pinecone_key"]
openai_api_key = st.secrets["openai_key"]
index_name = st.secrets["index"]
os.environ["OPENAI_API_KEY"] = openai_api_key
app_title = "Document Query"  # change to whatever you want

# connect to Pinecone
pc = Pinecone(api_key=pinecone_api_key)
pinecone_index = pc.Index(index_name)

# init LlamaIndex
# NOTE: set the namespace name if you upserted the vectors to a namespace
vector_index = VectorStoreIndex.from_vector_store(vector_store=vector_store)
# vector_store = PineconeVectorStore(pinecone_index=pinecone_index, namespace="<NAMESPACE_NAME>")


# streamlit app UI
def main():
    st.title(app_title)

    # Input for user query
    query = st.text_input("Ask a question:")

    # Button to send query
    if st.button("Submit"):
        if query:
            # Send query to Pinecone index
            results = query_index(query)

            # Display results
            display_results(results)


# send a query to Pinecone index
def query_index(query):
    try:
        # Search for similar vectors in Pinecone
        query_engine = vector_index.as_query_engine()
        results = query_engine.query(query)
        return results

    except Exception as e:
        st.error(f"Error querying Pinecone index: {e}")
        return None


# display query results
def display_results(results):
    if results:
        st.success("Query successful!")

        id = next(iter(results.metadata))
        source = results.metadata[id]["page_label"]

        st.write(results.response)
        st.write("*Source: page " + source + "*")
    else:
        st.warning("No results found.")


if __name__ == "__main__":
    main()
