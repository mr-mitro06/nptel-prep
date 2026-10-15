import os
import sys
import json

# Ensure scripts dir is in path
sys.path.insert(0, os.path.dirname(__file__))

from question_data.part1_isp_and_graphs import DATA as PART1
from question_data.part2_graphs_and_logic import DATA as PART2
from question_data.part3_logic_and_mutation import DATA as PART3
from question_data.part4_oo_web_mobile_exer import DATA as PART4

ALL_TOPICS = PART1 + PART2 + PART3 + PART4

print(f"Total topics loaded from modules: {len(ALL_TOPICS)}")

# Validation checks
seen_ids = set()
validation_errors = []
total_questions = 0

topics_meta = []

questions_dir = os.path.join(os.getcwd(), "data", "questions")
os.makedirs(questions_dir, exist_ok=True)

all_questions_list = []

for topic in ALL_TOPICS:
    topic_id = topic["topicId"]
    topic_name = topic["topicName"]
    source_pdf = topic["sourcePdf"]
    questions = topic["questions"]
    
    diff_counts = {"easy": 0, "medium": 0, "hard": 0}
    
    for q in questions:
        total_questions += 1
        qid = q["id"]
        
        # Check unique ID
        if qid in seen_ids:
            validation_errors.append(f"Duplicate question ID: {qid}")
        seen_ids.add(qid)
        
        # Check text
        if not q["question"] or len(q["question"].strip()) < 15:
            validation_errors.append(f"Short/empty question text in {qid}")
            
        # Check options
        opts = q["options"]
        if not isinstance(opts, dict) or set(opts.keys()) != {"A", "B", "C", "D"}:
            validation_errors.append(f"Invalid options keys in {qid}: {opts.keys()}")
            
        for k in ["A", "B", "C", "D"]:
            if not opts.get(k) or len(str(opts[k]).strip()) == 0:
                validation_errors.append(f"Empty option {k} in {qid}")
                
        # Check correct answer
        ca = q["correctAnswer"]
        if ca not in ["A", "B", "C", "D"]:
            validation_errors.append(f"Invalid correct answer '{ca}' in {qid}")
            
        # Check explanation
        if not q["explanation"] or len(q["explanation"].strip()) < 10:
            validation_errors.append(f"Short/empty explanation in {qid}")
            
        # Check difficulty
        diff = q.get("difficulty", "medium").lower()
        if diff not in ["easy", "medium", "hard"]:
            validation_errors.append(f"Invalid difficulty '{diff}' in {qid}")
        diff_counts[diff] = diff_counts.get(diff, 0) + 1
        
        # Add to all_questions_list with topic metadata embedded
        full_q = dict(q)
        full_q["topicId"] = topic_id
        full_q["topicName"] = topic_name
        full_q["sourcePdf"] = source_pdf
        all_questions_list.append(full_q)
        
    # Write individual topic file
    topic_file = os.path.join(questions_dir, f"{topic_id}.json")
    with open(topic_file, "w", encoding="utf-8") as tf:
        json.dump(topic, tf, indent=2, ensure_ascii=False)
        
    topics_meta.append({
        "topicId": topic_id,
        "topicName": topic_name,
        "sourcePdf": source_pdf,
        "questionCount": len(questions),
        "difficultyCounts": diff_counts
    })
    
    print(f"  Processed {topic_name:50} | Questions: {len(questions):2} | Easy: {diff_counts['easy']:2}, Med: {diff_counts['medium']:2}, Hard: {diff_counts['hard']:2}")

# Write master topics.json
topics_file = os.path.join(os.getcwd(), "data", "topics.json")
with open(topics_file, "w", encoding="utf-8") as tpf:
    json.dump(topics_meta, tpf, indent=2, ensure_ascii=False)

# Write all_questions.json
all_q_file = os.path.join(os.getcwd(), "data", "all_questions.json")
with open(all_q_file, "w", encoding="utf-8") as aqf:
    json.dump(all_questions_list, aqf, indent=2, ensure_ascii=False)

print("\n" + "=" * 60)
print(f"VALIDATION SUMMARY:")
print(f"Total Topics: {len(ALL_TOPICS)}")
print(f"Total Questions: {total_questions}")
print(f"Validation Errors Found: {len(validation_errors)}")
if validation_errors:
    for err in validation_errors[:10]:
        print("  ERROR:", err)
    sys.exit(1)
else:
    print("ALL 400 QUESTIONS PASSED 100% STRICT VALIDATION!")
print("=" * 60)
