from spire.doc import *
from spire.doc.common import *

def para_footnote_index(file_path, para_index, refer_string):
    # Create a Document instance
    document = Document()
    # Load a sample Word document
    document.LoadFromFile(file_path)
    section = document.Sections[0]
    if section.Paragraphs.get_Item(0).Text == "Evaluation Warning: The document was created with Spire.Doc for Python.":
        section.Paragraphs.RemoveAt(0)
    paragraph = section.Paragraphs.get_Item(para_index)

    # Find a specific text
    selection = document.FindString(refer_string, False, True)
    

    # if selection:
    # Get the found text as a single text range
    textRange = selection.GetAsOneRange()    
  

    # Get the index position of the text range in the paragraph
    index = paragraph.ChildObjects.IndexOf(textRange)
    print(index)
    document.Close
    return index
    
# para_footnote_index(file_path='test111.docx', para_index=7, refer_string='----footnote1----')    