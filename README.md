# llamaindex-streamlit-starter

This is a template repository for creating a [Streamlit](https://streamlit.io) app to interact with PDF files with natural language. Content is processed and vectorized with [LlamaIndex](https://www.llamaindex.ai/) and stored in a [Pinecone](https://pinecone.io) database.

## Configuration

### Install packages

1. For best results, create a [Python virtual environment](https://realpython.com/python-virtual-environments-a-primer/) with 3.10 or 3.11 and reuse it when running any file in this repo.
2. Run

```shell
pip install -r requirements.txt
```

### Environment Variables

Copy `.env.template` to `.env` and `.streamlit/secrets.toml.template` to `.streamlit/secrets.toml`. Fill in your Pinecone API key, OpenAI API key, index name, and the path to your PDF file. The `.env` file will be used by the Jupyter notebook for processing the data and upserting it to Pinecone, whereas `secrets.toml` will be used by Streamlit when running locally.

## Processing the PDF

Run all cells in the `pinecone-llamaindex.ipynb` notebook. If you want to create multiple Streamlit apps in the same Github repository, use namespaces to separate the data within a single Pinecone index: comment/uncomment the appropriate lines under the **Upsert vectors to Pinecone** heading. (NOTE: you will also have to do this in the [app configuration](#optional-configuring-the-app).)

Assuming the test query returns a response successfully, you're ready to create the Streamlit app.

## Testing the app locally

### [OPTIONAL] Configuring the app

In the `streamlit_app.py` file:

- Set your preferred title on [line 13](https://github.com/pinecone-field/llamaindex-streamlit-starter/blob/ed56db5bdcb940bece8c68f9034debd83d3e3e41/streamlit_app.py#L13)
- Set your preferred prompt on [line 30](https://github.com/pinecone-field/llamaindex-streamlit-starter/blob/ed56db5bdcb940bece8c68f9034debd83d3e3e41/streamlit_app.py#L30)
- Set your preferred button label on [line 33](https://github.com/pinecone-field/llamaindex-streamlit-starter/blob/ed56db5bdcb940bece8c68f9034debd83d3e3e41/streamlit_app.py#L33)
- If you upserted vectors to a namespace when [processing the PDF](#processing-the-pdf), comment/uncomment [lines 21-22](https://github.com/pinecone-field/llamaindex-streamlit-starter/blob/ed56db5bdcb940bece8c68f9034debd83d3e3e41/streamlit_app.py#L21) and set the same namespace name.

### Running the app

1. Validate that Streamlit is [installed](#install-packages) correctly by running

```shell
streamlit hello
```

You should see a welcome message and the demo should automatically open in your browser. If it doesn't open automatically, manually go to the **Local URL** listed in the terminal output.

2. If the demo ran correctly, run

```shell
streamlit run streamlit_app.py
```

3. Confirm that your app looks good and test queries return successful responses. If so, move on to deployment!

## Deploying the app

1. Create and login to a [Streamlit Community Cloud](https://share.streamlit.io) account.
2. Link your Github account in Workspace settings.
3. On the dashboard, click "New app".
4. Select your Github repo and branch, then enter the filename `streamlit_app.py`.
5. [OPTIONAL] Set your preferred app URL.
6. In "Advanced settings...":
   - Change the Python version to match the one you tested locally
   - Copy the contents of your `secrets.toml` file into "Secrets"
   - Click "Save"
7. Click "Deploy"
