
import fitz

def read_pdf(file_path):
    with fitz.open(file_path) as document:
        all_text = []

        for page in document:
            all_text.append(page.get_text())

    return "\n".join(all_text)
