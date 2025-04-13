import json
import re

def parse_questions(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        # Remove any empty lines and strip whitespace
        lines = [line.strip() for line in file if line.strip()]
    
    questions = []
    # Mapping from question number to answer index; update as needed.
    answers = {501: 2, 502: 0}
    
    i = 0
    while i < len(lines):
        # Match a question line formatted like "501.Question text..."
        question_match = re.match(r"(\d+)\.(.*)", lines[i])
        if not question_match:
            print(f"Error parsing question line: {lines[i]}")
            i += 1
            continue
        
        question_number = int(question_match.group(1))
        question_text = question_match.group(2).strip()
        
        options = []
        # Assuming the next four lines are the options
        for j in range(1, 5):
            if i + j < len(lines):
                option_line = lines[i + j]
                # Match lines like "a. Option text"
                option_match = re.match(r"[a-d]\.\s*(.*)", option_line)
                if option_match:
                    options.append(option_match.group(1).strip())
        
        question_obj = {
            "question": question_text,
            "options": options,
            "answer": answers.get(question_number, 0),  # Default answer is 0 if not specified
            "questionNumber": question_number,
            # parse as int
            "questionIndex": int(i / 5),
        }
        questions.append(question_obj)
        
        i += 5  # Move to the next question block

    return questions

def main():
    questions = parse_questions("questions.txt")
    with open("questions.json", "w", encoding="utf-8") as json_file:
        json.dump(questions, json_file, ensure_ascii=False, indent=2)
    print("questions.json generated successfully.")

if __name__ == "__main__":
    main()
