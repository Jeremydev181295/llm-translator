from spire.doc import *
from spire.doc.common import *

def paragraphs_for_footnote(file_path):
    # Create a Document instance
    document = Document()
    # Load a Word document    
    document.LoadFromFile(file_path)
    # Get the first section of the document
    section = document.Sections[0]   
    
    para_footnote_indexes = []
    # Loop through the paragraphs in the section
    for y in range(section.Paragraphs.Count):    
        para = section.Paragraphs.get_Item(y)
        index = -1
        i = 0
        cnt = para.ChildObjects.Count
        while i < cnt:        
            pBase = para.ChildObjects[i] if isinstance(para.ChildObjects[i], ParagraphBase) else None
            if isinstance(pBase, Footnote):
                index = i 
                if index > -1:
                    para_footnote_indexes.append(y)
            i += 1
    document.Close
    return para_footnote_indexes
   
# print(paragraphs_for_footnote("test.docx"))