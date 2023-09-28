import csv
import json

def generate_suggestions(csv_file):
    suggestions = []

    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for word in row:
                words = word.split(',')
                for w in words:
                    w = w.strip()
                    if w:
                        suggestions.append(w)

    return {"suggestions": suggestions}

def save_to_json(data, json_file):
    with open(json_file, 'w') as outfile:
        json.dump(data, outfile, indent=4)

if __name__ == "__main__":
    csv_file = 'keywords.csv'
    json_file = 'keywords.json'

    suggestions_data = generate_suggestions(csv_file)
    save_to_json(suggestions_data, json_file)
    print("Conversion CSV vers JSON terminée.")
