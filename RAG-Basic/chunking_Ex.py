from langchain_text_splitters import CharacterTextSplitter
text_splitter = CharacterTextSplitter(chunk_size = 500 , chunk_overlap = 50)
docs = text_splitter.create_documents([raw_text])