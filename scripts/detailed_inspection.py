import os
import sys
import json

data_dir = os.path.join("data", "extracted_texts")
files = [f for f in sorted(os.listdir(data_dir)) if f != "summary.json" and f.endswith(".json")]

with open(os.path.join("scripts", "inspection_output.txt"), "w", encoding="utf-8") as out:
    for f in files:
        with open(os.path.join(data_dir, f), "r", encoding="utf-8") as fp:
            doc = json.load(fp)
        out.write(f"\n=======================================================\n")
        out.write(f"TOPIC: {doc['topic_name']} ({doc['file']})\n")
        out.write(f"Total Pages: {doc['total_pages']} | Chars: {doc['char_count']}\n")
        out.write(f"=======================================================\n")
        
        for p in doc['pages']:
            clean = " ".join(p['text'].split())
            if clean:
                out.write(f"[P{p['page']}]: {clean}\n")

print("Inspection output written successfully.")
