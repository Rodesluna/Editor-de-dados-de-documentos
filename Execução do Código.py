Execução do Código

from docx import Document

def edit_contract(template_path, output_path, replacements):
    # Carregar o documento de modelo
    doc = Document(template_path)
    
    # Substituir os campos no documento
    for paragraph in doc.paragraphs:
        for key, value in replacements.items():
            if key in paragraph.text:
                paragraph.text = paragraph.text.replace(key, value)
    
    # Salvar o documento editado
    doc.save(output_path)