import model

QUERY = model.Get_User_Query()
DOCS = model.Search_docs()
BM25 = model.BM_25()

docs = DOCS.load_documents_from_folder('./documents')