import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')
data_dir = os.path.join("data", "extracted_texts")
files = [f for f in sorted(os.listdir(data_dir)) if f != "summary.json" and f.endswith(".json")]

for f in files:
    with open(os.path.join(data_dir, f), "r", encoding="utf-8") as fp:
        doc = json.load(fp)
    print(f"=== {doc['topic_name']} ({doc['file']}) | Pages: {doc['total_pages']} ===")
    # Print slide titles / headers from first few pages and middle pages
    for p in doc['pages'][:6]:
        lines = [line.strip() for line in p['text'].split('\n') if line.strip()]
        header = " | ".join(lines[:3]) if lines else "Empty"
        print(f"  P{p['page']}: {header[:120]}")
    print()
