from spire.doc import *
from spire.doc.common import *

def add_footnote(file_path, para_index, refer_string, footnote_text):
    # Create a Document instance
    document = Document()
    # Load a sample Word document
    document.LoadFromFile(file_path)
    section = document.Sections[0]
    if section.Paragraphs.get_Item(0).Text == "Evaluation Warning: The document was created with Spire.Doc for Python.":
        section.Paragraphs.RemoveAt(0)
    paragraph = section.Paragraphs.get_Item(para_index)
    print(paragraph.ChildObjects.Count)
    selection = document.FindString(refer_string, False, True)
    

    # if selection:
    # Get the found text as a single text range
    textRange = selection.GetAsOneRange()    
    
    

    # Get the index position of the text range in the paragraph
    index = paragraph.ChildObjects.IndexOf(textRange)
    print(index)
    # Add a footnote to the paragraph
    footnote = paragraph.AppendFootnote(FootnoteType.Footnote)

    # Insert the footnote after the text range
    paragraph.ChildObjects.Insert(index, footnote)

    # Set the text content of the footnote
    text = footnote.TextBody.AddParagraph().AppendText(footnote_text)

   
    # Save the result document
    document.SaveToFile(file_path, FileFormat.Docx)
    document.Close()



# add_footnote("translated_test_llama3_8b.docx", 1, "----footnote1----", "rrr")