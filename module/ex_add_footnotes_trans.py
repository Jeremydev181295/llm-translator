from spire.doc import *
from spire.doc.common import *

def add_footnote_trans(source_file_path, trans_footnotes):
    # Create a Document instance
    document = Document()
    # Load a Word document    
    document.LoadFromFile(source_file_path)
    # Get the first section of the document
    section = document.Sections[0]
   
    footnote_number = 0
    # Loop through the paragraphs in the section
    for y in range(section.Paragraphs.Count):    
        para = section.Paragraphs.get_Item(y)
        dd_index = section.Paragraphs.IndexOf(para)
        # print(dd_index)
        # print(section.Paragraphs[dd_index].Text)  
        # print(para.Items)
        index = -1
        i = 0
        cnt = para.ChildObjects.Count
        while i < cnt:        
            pBase = para.ChildObjects[i] if isinstance(para.ChildObjects[i], ParagraphBase) else None
            if isinstance(pBase, Footnote):
                index = i 
                if index > -1:
                    print(para.ChildObjects[index-1].Text)
                    # # Remove the footnotes from the paragraph                    
                    # para.ChildObjects.RemoveAt(index)
                    footnote = para.AppendFootnote(FootnoteType.Footnote)
                    para.ChildObjects.Insert(index, footnote)
                    # textRange = footnote.TextBody.AddParagraph().AppendText(trans_footnotes[footnote_number])
                    footnote_number += 1                    
            # else:
            #     print(pBase.Text.strip())
            i += 1

    # Save the result document        
    document.SaveToFile("AddFootnotes.docx", FileFormat.Docx)
    document.Close()
add=[]
add.append("fff1")
add.append("fff2")
add.append("fff3")
add.append("fff4")
add.append("fff5")
add.append("fff6")
add.append("fff7")
add.append("fff8")
add.append("fff9")
add_footnote_trans(source_file_path="test.docx", trans_footnotes=add)