import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text.strip()

def extract_specific_info(pdf_path, keywords):
    text = extract_text_from_pdf(pdf_path)
    extracted_info = {}
    for keyword in keywords:
        if keyword in text:
            start_index = text.index(keyword) + len(keyword)
            end_index = text.find("\n", start_index)
            extracted_info[keyword] = text[start_index:end_index].strip()
    return extracted_info