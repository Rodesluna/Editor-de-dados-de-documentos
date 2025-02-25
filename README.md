# Editor-de-dados-de-documentos
O objetivo desse código é editar pequedos dados de um documento pronto, tal como contratos e acordos'


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

# Exemplo de uso
template_path = 'caminho/para/seu/modelo.docx'
output_path = 'caminho/para/o/contrato_editado.docx'
replacements = {
    'NOME': 'João da Silva',
    'CPF': '123.456.789-00',
    'ENDEREÇO': 'Rua Exemplo, 123, Cidade, Estado',
    'DATA': '24 de fevereiro de 2025'
}

edit_contract(template_path, output_path, replacements)
Este script carrega um documento de modelo, substitui os campos especificados (como NOME, CPF, ENDEREÇO, DATA, etc.) pelos valores fornecidos no dicionário replacements e salva o documento editado.

Certifique-se de ajustar o caminho para o seu modelo de documento e o caminho onde deseja salvar o contrato editado. Para instalar a biblioteca python-docx, você pode usar o pip:

sh
pip install python-docx
