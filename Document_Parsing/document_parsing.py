from pathlib import Path
from pypdf import PdfReader

#Task: Import a file and print the text
pdf_file_name = "paper.pdf"

pdf_path = Path(__file__).resolve().parent / pdf_file_name
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

print(all_text)