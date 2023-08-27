import json
import io

def remove_duplicates(input_list):
    unique_words = set()
    output_list = []

    for word in input_list:
        if word == "...":
            unique_words.add(word)
        else:
            lowercase_word = word.lower()
            if lowercase_word not in unique_words:
                unique_words.add(lowercase_word)
                output_list.append(word)
    
    return output_list

def main():
    with io.open("suggestions.json", "r", encoding="utf-8-sig") as json_file:
        suggestions = json.load(json_file)["suggestions"]

    cleaned_suggestions = remove_duplicates(suggestions)
    sorted_suggestions = sorted(cleaned_suggestions)  # Tri des mots

    with io.open("suggestions.json", "w", encoding="utf-8-sig") as json_file:
        json.dump({"suggestions": sorted_suggestions}, json_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
