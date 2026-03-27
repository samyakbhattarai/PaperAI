from pathlib import Path
from pypdf import PdfReader


def read_pdf(pdf_file_name):
    pdf_path = Path(pdf_file_name).expanduser()
    if not pdf_path.is_absolute():
        pdf_path = Path.cwd() / pdf_path

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    reader = PdfReader(str(pdf_path))
    total_pages = len(reader.pages)
    i = 0
    all_text=""
    while(i!=total_pages):
        page=  reader.pages[i]
        text = page.extract_text()
        all_text += text + '\n'
        i+=1
    return all_text