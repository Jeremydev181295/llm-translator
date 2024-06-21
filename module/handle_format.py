# from docx import Document
# from docx.shared import Pt, RGBColor
# from docx.enum.text import WD_ALIGN_PARAGRAPH

def copy_paragraph_font_style(source_paragraph, target_paragraph, copy_para):
    if source_paragraph.runs:
        for i, source_run in enumerate(source_paragraph.runs):   
            target_run = target_paragraph.add_run()     
            copy_run = copy_para.add_run()
            
            copy_run.text = target_paragraph.runs[i].text
            
            font_source = source_run.font
            font_target = copy_run.font

            font_target.name = font_source.name
            font_target.size = font_source.size
            font_target.bold = font_source.bold
            font_target.italic = font_source.italic
            font_target.underline = font_source.underline
            font_target.color.rgb = font_source.color.rgb
            font_target.highlight_color = font_source.highlight_color
            
            font_target.math = font_source.math
            # font_target.highlight_color = font_source.highlight_color
            # font_target.highlight_color = font_source.highlight_color
    else:
        for i, target_run in enumerate(target_paragraph.runs):   
            copy_run = copy_para.add_run()
            
            copy_run.text = target_paragraph.runs[i].text
            
            font_source = target_run.font
            font_target = copy_run.font

            font_target.name = font_source.name
            font_target.size = font_source.size
            font_target.bold = font_source.bold
            font_target.italic = font_source.italic
            font_target.underline = font_source.underline
            font_target.color.rgb = font_source.color.rgb
            font_target.highlight_color = font_source.highlight_color
            
            font_target.math = font_source.math
        
def copy_paragraph_style(source_doc, target_doc):
    for i, source_para in enumerate(source_doc.paragraphs):
        if i < len(target_doc.paragraphs):
            target_para_format = target_doc.paragraphs[i].paragraph_format 
            target_para_format.alignment = source_para.paragraph_format.alignment
            target_para_format.space_before = source_para.paragraph_format.space_before
            target_para_format.space_after  = source_para.paragraph_format.space_after 
            target_para_format.left_indent   = source_para.paragraph_format.left_indent 
            target_para_format.right_indent   = source_para.paragraph_format.right_indent 
            target_para_format.first_line_indent   = source_para.paragraph_format.first_line_indent 
            target_para_format.keep_with_next  = source_para.paragraph_format.keep_with_next
            target_para_format.keep_together   = source_para.paragraph_format.keep_together 
            target_para_format.page_break_before   = source_para.paragraph_format.page_break_before 
            target_para_format.widow_control   = source_para.paragraph_format.widow_control 

            
            target_para_format.line_spacing  = source_para.paragraph_format.line_spacing
            target_para_format.line_spacing_rule  = source_para.paragraph_format.line_spacing_rule
            # target_para_format.tab_stops  = source_para.paragraph_format.tab_stops
            # target_para_format.keep_with_next  = source_para.paragraph_format.keep_with_next