from spire.doc import *

def add_footnote(document, refer_word, footnote_string):
    # Create a Document instance
    

    # Find a specific text
    selection = document.FindString(refer_word, False, True)

    # Get the found text as a single text range
    textRange = selection.GetAsOneRange()

    # Get the paragraph where the text range is located
    paragraph = textRange.OwnerParagraph

    # Get the index position of the text range in the paragraph
    index = paragraph.ChildObjects.IndexOf(textRange)

    # Add a footnote to the paragraph
    footnote = paragraph.AppendFootnote(FootnoteType.Footnote)

    # Insert the footnote after the text range
    paragraph.ChildObjects.Insert(index + 1, footnote)

    # Set the text content of the footnote
    text = footnote.TextBody.AddParagraph().AppendText(footnote_string)
    # Create a Document instance)
    # Save the result document
    



    

