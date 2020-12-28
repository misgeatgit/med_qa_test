import json

KEYWORD_FILE = "med_keywords.txt"
QUESTION_FILE = "med_question.txt"


BASE_DIR = "medical-question-answer-data"

files = ["ehealthforumQAs.json", "icliniqQAs.json", "questionDoctorQAs.json",
         "webmdQAs.json"]

questions = set()
keywords = set()
for qfile in files:
    with open( BASE_DIR +"/"+qfile) as jsonf:
        data = json.load(jsonf)
        for qas in data:
            questions.add(qas['question'].replace('\n',' '))
            keywords.update(qas['tags'])

with open(KEYWORD_FILE, 'w') as f:
    f.write("\n".join(word for word in keywords))

with open(QUESTION_FILE, 'w') as f:
    f.write("\n".join(q for q in questions))
