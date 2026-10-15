import os
import sys
import json
from pypdf import PdfReader

# Force UTF-8 for console output
sys.stdout.reconfigure(encoding='utf-8')

pdf_dir = os.path.join(os.getcwd(), "Lecture Materials")
output_dir = os.path.join(os.getcwd(), "data", "extracted_texts")
os.makedirs(output_dir, exist_ok=True)

files = sorted([f for f in os.listdir(pdf_dir) if f.lower().endswith(".pdf")])
print(f"Processing {len(files)} PDFs from {pdf_dir}...\n")

summary = []

for f in files:
    pdf_path = os.path.join(pdf_dir, f)
    base_name = os.path.splitext(f)[0]
    topic_name = base_name.replace("-", " ").title()
    
    # Specific topic name polish
    topic_name_map = {
        "Isp Full Slides": "Input Space Partitioning (ISP)",
        "Oo Testing": "Object-Oriented Testing",
        "Exer Student": "Comprehensive Testing Exercises & Case Studies",
        "Graphs Data Flow": "Graph Coverage - Data Flow",
        "Graphs Source Code Data Flow": "Graph Coverage - Source Code Data Flow",
        "Graphs Source Code": "Graph Coverage from Source Code",
        "Graphs Specification": "Graph Coverage from Specifications",
        "Graphs Structural Coverage Algorithms": "Graph Structural Coverage Algorithms",
        "Graphs Structural Coverage": "Graph Structural Coverage Criteria",
        "Logic Coverage Algorithms": "Logic Coverage Algorithms",
        "Logic Coverage Criteria": "Logic Coverage Criteria (ACC, GACC, CACC, RACC)",
        "Logic Source Code1": "Logic Coverage from Source Code (Part 1)",
        "Logic Source Code2": "Logic Coverage from Source Code (Part 2)",
        "Mobile Apps Testing": "Mobile Applications Testing",
        "Mutation For Integration": "Mutation Testing for Integration",
        "Mutation Operators Source Code": "Mutation Operators for Source Code",
        "Mutation Testing Source Code": "Mutation Testing Principles & Practice",
        "Non Functional Testing": "Non-Functional Testing (Performance & Security)",
        "Regression Testing": "Regression Testing (Selection & Prioritization)",
        "Web Apps Testing": "Web Applications Testing"
    }
    pretty_topic = topic_name_map.get(topic_name, topic_name)
    
    try:
        reader = PdfReader(pdf_path)
        pages_data = []
        total_text_len = 0
        
        for idx, page in enumerate(reader.pages):
            text = page.extract_text() or ""
            clean_text = text.strip()
            total_text_len += len(clean_text)
            pages_data.append({
                "page": idx + 1,
                "text": clean_text
            })
            
        doc_data = {
            "file": f,
            "topic_id": base_name.lower(),
            "topic_name": pretty_topic,
            "total_pages": len(reader.pages),
            "char_count": total_text_len,
            "pages": pages_data
        }
        
        out_file = os.path.join(output_dir, f"{base_name.lower()}.json")
        with open(out_file, "w", encoding="utf-8") as out_fp:
            json.dump(doc_data, out_fp, indent=2, ensure_ascii=False)
            
        status = "OK" if total_text_len > 500 else "WARNING_LOW_TEXT"
        summary.append({
            "file": f,
            "topic_name": pretty_topic,
            "topic_id": base_name.lower(),
            "pages": len(reader.pages),
            "chars": total_text_len,
            "status": status
        })
        print(f"[{status:16}] {f:38} | Pages: {len(reader.pages):3} | Chars: {total_text_len:6}")
        
    except Exception as e:
        print(f"[ERROR           ] {f:38} | Error: {e}")
        summary.append({
            "file": f,
            "topic_name": pretty_topic,
            "topic_id": base_name.lower(),
            "pages": 0,
            "chars": 0,
            "status": f"ERROR: {str(e)}"
        })

summary_file = os.path.join(output_dir, "summary.json")
with open(summary_file, "w", encoding="utf-8") as s_fp:
    json.dump(summary, s_fp, indent=2, ensure_ascii=False)

print(f"\nExtracted data saved to {output_dir}")
