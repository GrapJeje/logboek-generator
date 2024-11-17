from docx import Document
from functions import heading

# create a new document
document = Document()

heading("Basic Info")

# Ask for document name
docName = input("Geef een document naam op: ")

# save the document
document.save(f"documents/{docName}.docx")
