from spire.doc import *
from spire.doc.common import *

# Create a Document instance
document = Document()
# Load a sample Word document
document.LoadFromFile("translated_test_llama3_8b.docx")

# Get the first section
section = document.Sections[0]

# Get a specified paragraph in the section
paragraph = section.Paragraphs[3]

# Add a footnote at the end of the paragraph
footnote = paragraph.AppendFootnote(FootnoteType.Footnote)

# Set the text content of the footnote
text = footnote.TextBody.AddParagraph().AppendText("The industry code list is available online.")
            
# # Set the text font and color
# text.CharacterFormat.FontName = "Arial"
# text.CharacterFormat.FontSize = 12
# text.CharacterFormat.TextColor = Color.get_DarkBlue()

# # Set the font and color of the footnote reference mark
# footnote.MarkerCharacterFormat.FontName = "Calibri"
# footnote.MarkerCharacterFormat.FontSize = 15
# footnote.MarkerCharacterFormat.Bold = True
# footnote.MarkerCharacterFormat.TextColor = Color.get_DarkCyan()

# Save the result document
document.SaveToFile("translated_test_llama3_8b_f.docx", FileFormat.Docx2016)
document.Close()