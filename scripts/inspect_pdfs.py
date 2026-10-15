import os
import sys
from pypdf import PdfReader

folder = os.path.join(os.getcwd(), "Lecture Materials")
if not os.path.exists(folder):
    print(f"Error: {folder} does not exist")
    sys.exit(1)

files = sorted([f for f in os.listdir(folder) if f.lower().endswith(".pdf")])
print(f"Total PDFs found: {len(files)}")

report = []
for f in files:
    path = os.path.join(folder, f)
    try:
        reader = PdfReader(path)
        num_pages = len(reader.pages)
        total_chars = 0
        sample_text = ""
        for i, page in enumerate(reader.pages):
            text = page.extract_text() or ""
            total_chars += len(text)
            if i == 0 and text.strip():
                sample_text = text.strip()[:150].replace("\n", " ")
            elif not sample_text and text.strip():
                sample_text = text.strip()[:150].replace("\n", " ")
        report.append({
            "file": f,
            "pages": num_pages,
            "chars": total_chars,
            "sample": sample_text,
            "status": "OK" if total_chars > 200 else "LOW_TEXT/SCANNED?"
        })
    except Exception as e:
        report.append({
            "file": f,
            "pages": 0,
            "chars": 0,
            "sample": str(e),
            "status": f"ERROR: {e}"
        })

for r in report:
    print(f"[{r['status']}] {r['file']} | Pages: {r['pages']} | Chars: {r['chars']}")
    if r['sample']:
        print(f"   Sample: {r['sample'][:100]}...")
