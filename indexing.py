import os

from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage,
)
from llama_index.readers.web import SimpleWebPageReader
import crawler


def indexing(data, storage_path):
    index_loaded = None
    try:
        storage_context = StorageContext.from_defaults(persist_dir=storage_path)
        index = load_index_from_storage(storage_context)
        index_loaded = True
    except:
        index_loaded = False

    if not index_loaded:
        docs = creating_docs(data)

        # build index
        index = VectorStoreIndex.from_documents(docs)

        # persist index
        index.storage_context.persist(persist_dir=storage_path)
    return index


def creating_docs(data):
    if os.path.exists(data[0]):
        docs = file_helper(data)
    else:
        docs = website_helper(data)
    return docs


def website_helper(data):
    web_crawler = crawler.Crawler(urls=data)
    web_crawler.run()
    docs = SimpleWebPageReader(html_to_text=True).load_data(
        web_crawler.visited_urls,
    )
    return docs


def file_helper(data):
    docs = SimpleDirectoryReader(input_files=data).load_data()
    return docs
