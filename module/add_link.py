from docx import Document
import docx
#This is only needed if you're using the builtin style above
def get_or_create_hyperlink_style(d):
    """If this document had no hyperlinks so far, the builtin
       Hyperlink style will likely be missing and we need to add it.
       There's no predefined value, different Word versions
       define it differently.
       This version is how Word 2019 defines it in the
       default theme, excluding a theme reference.
    """
    if "Hyperlink" not in d.styles:
        if "Default Character Font" not in d.styles:
            ds = d.styles.add_style("Default Character Font",
                                    docx.enum.style.WD_STYLE_TYPE.CHARACTER,
                                    True)
            ds.element.set(docx.oxml.shared.qn('w:default'), "1")
            ds.priority = 1
            ds.hidden = True
            ds.unhide_when_used = True
            del ds
        hs = d.styles.add_style("Hyperlink",
                                docx.enum.style.WD_STYLE_TYPE.CHARACTER,
                                True)
        hs.base_style = d.styles["Default Character Font"]
        hs.unhide_when_used = True
        hs.font.color.rgb = docx.shared.RGBColor(0x05, 0x63, 0xC1)
        hs.font.underline = True
        del hs

    return "Hyperlink"


def add_hyperlink(paragraph, source_file_path, text, url):
    # This gets access to the document.xml.rels file and gets a new relation id value
    part = paragraph.part
    r_id = part.relate_to(url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)

    # Create the w:hyperlink tag and add needed values
    hyperlink = docx.oxml.shared.OxmlElement('w:hyperlink')
    hyperlink.set(docx.oxml.shared.qn('r:id'), r_id, )

    # Create a new run object (a wrapper over a 'w:r' element)
    new_run = docx.text.run.Run(
        docx.oxml.shared.OxmlElement('w:r'), paragraph)
    new_run.text = text

   
    # Set the run's style to the builtin hyperlink style, defining it if necessary

    # new_run.style = get_or_create_hyperlink_style(part.document)

    # # copy source file link style
    source_doc = Document(source_file_path)
    for source_para in source_doc.paragraphs:
            if source_para.text == text :
                paragraph.style = source_para.style
                if source_para.runs:
                    for source_run in source_para.runs: 

                        font_source = source_run.font
                        font_target = new_run.font

                        font_target.name = font_source.name
                        font_target.size = font_source.size
                        font_target.bold = font_source.bold
                        font_target.italic = font_source.italic
                        font_target.underline = True
                        font_target.color.rgb = docx.shared.RGBColor(0x05, 0x63, 0xC1)
                            
    #                     font_target.highlight_color = font_source.highlight_color
                        
    #                     font_target.math = font_source.math
            
    # Alternatively, set the run's formatting explicitly
    # new_run.font.color.rgb = docx.shared.RGBColor(0x05, 0x63, 0xC1)
    # new_run.font.underline = True

    # Join all the xml elements together
    hyperlink.append(new_run._element)
    paragraph._p.append(hyperlink)
    return hyperlink

# document = docx.Document()
# p = document.add_paragraph('')
# add_hyperlink(p, 'having some', "http://supersitedelamortquitue.fr")

# document.save('demo_hyperlink.docx')


