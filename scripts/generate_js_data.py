import os
import json

data_dir = os.path.join(os.getcwd(), "data")
js_dir = os.path.join(os.getcwd(), "js")
os.makedirs(js_dir, exist_ok=True)

with open(os.path.join(data_dir, "topics.json"), "r", encoding="utf-8") as f:
    topics = json.load(f)

with open(os.path.join(data_dir, "all_questions.json"), "r", encoding="utf-8") as f:
    questions = json.load(f)

with open(os.path.join(data_dir, "revision.json"), "r", encoding="utf-8") as f:
    revision = json.load(f)

payload = {
    "topics": topics,
    "questions": questions,
    "revision": revision
}

js_content = f"// Automatically generated NPTEL Prep data bundle\nwindow.NPTEL_DATA = {json.dumps(payload, ensure_ascii=False)};\n"

out_file = os.path.join(js_dir, "data.js")
with open(out_file, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Generated {out_file} with {len(topics)} topics, {len(questions)} questions, {len(revision)} revision sets.")
