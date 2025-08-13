def extrair_texto_pdf(path):
    import pdfplumber
    texto = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            texto += page.extract_text() or ""
    return texto
