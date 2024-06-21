from spire.doc import *
from spire.doc.common import *

def add_footnote(file_path, para_index, footnote_index, footnote_text):
    # Create a Document instance
    document = Document()
    # Load a sample Word document
    document.LoadFromFile(file_path)
    section = document.Sections[0]
    if section.Paragraphs.get_Item(0).Text == "Evaluation Warning: The document was created with Spire.Doc for Python.":
        section.Paragraphs.RemoveAt(0)
    paragraph = section.Paragraphs.get_Item(para_index)
    print(paragraph.ChildObjects.Count)
   
    # Add a footnote to the paragraph
    footnote = paragraph.AppendFootnote(FootnoteType.Footnote)

    # Insert the footnote after the text range
    paragraph.ChildObjects.Insert(footnote_index, footnote)

    # Set the text content of the footnote
    text = footnote.TextBody.AddParagraph().AppendText(footnote_text)

   
    # Save the result document
    document.SaveToFile(file_path, FileFormat.Docx)
    document.Close() 

# add_footnote("translated_test_llama3_8b_c.docx", 7, "----footnote1----", "eee")
