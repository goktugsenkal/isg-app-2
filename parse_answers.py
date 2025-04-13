#!/usr/bin/env python3
import json
import argparse

def parse_answers(answers_file, questions_file, output_file):
    # Load answers mapping from answers.json
    with open(answers_file, 'r', encoding='utf-8') as f:
        answers_list = json.load(f)
    
    # Create a mapping dictionary {questionIndex (int): answer (int)}
    answers_mapping = {}
    for entry in answers_list:
        try:
            q_index = int(entry['question'])
            ans = int(entry['answer'])
        except ValueError:
            # Skip the entry if conversion to integer fails
            continue
        answers_mapping[q_index] = ans

    # Load questions from questions.json
    with open(questions_file, 'r', encoding='utf-8') as f:
        questions = json.load(f)

    # Map answers to each question based on its questionIndex field
    for question in questions:
        q_index = question.get("questionIndex")
        if q_index is not None and q_index in answers_mapping:
            # Update the question's answer with the one from the mapping
            question["answer"] = answers_mapping[q_index]

    # Write the updated questions list to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"Mapping completed. Output saved to {output_file}")

def main():
    # Set up command-line argument parsing for file paths
    parser = argparse.ArgumentParser(
        description="Map answers from answers.json to corresponding questions in questions.json."
    )
    parser.add_argument('--answers', type=str, default='answers.json', 
                        help="Path to the answers JSON file (default: answers.json).")
    parser.add_argument('--questions', type=str, default='questions.json', 
                        help="Path to the questions JSON file (default: questions.json).")
    parser.add_argument('--output', type=str, default='questions_mapped.json', 
                        help="Path to output the updated questions JSON (default: questions_mapped.json).")
    args = parser.parse_args()

    # Execute mapping
    parse_answers(args.answers, args.questions, args.output)

if __name__ == "__main__":
    main()
