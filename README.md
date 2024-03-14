# llamaindex-streamlit-starter

This is a template repository for creating a [Streamlit](https://streamlit.io) app to interact with PDF files with natural language. Content is processed and vectorized with [LlamaIndex](https://www.llamaindex.ai/) and stored in a [Pinecone](https://pinecone.io) database.

## Configuration

### Environment Variables

Copy `.env.template` to `.env` and `secrets.toml.template` to `secrets.toml`. Fill in your Pinecone API key, OpenAI API key, index name, and the path to your PDF file. The `.env` file will be used by the Jupyter notebook for processing the data and upserting it to Pinecone, whereas `secrets.toml` will be used by Streamlit when running locally.

## Processing the PDF

Run all cells in the `pinecone-llamaindex.ipynb` notebook. If you want to create multiple Streamlit apps in the same Github repository, use namespaces to separate the data within a single Pinecone index: comment/uncomment the appropriate lines under the **Upsert vectors to Pinecone** heading.

Assuming the test query returns a response successfully, you're ready to create the Streamlit app.
