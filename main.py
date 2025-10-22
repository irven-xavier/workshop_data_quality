import pdfplumber

path = r"Z:\DEPTO FISCAL - NOVO\EMPRESAS\SPE EMPREENDIMENTOS LOTEAMENTO BAIRRO JARDINS - 563\INFORMAÇÕES GERAIS\CAIXA\2025\10-2025\09-2025\12241_2_08-2025 - Loteamento Jardins.pdf"

with pdfplumber.open(path) as arquivo:
    texto = ''
    for page in arquivo.pages:
        text = page.extract_text()
        print(text)