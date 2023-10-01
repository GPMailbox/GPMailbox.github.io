import csv
import json
import unicodedata
import tkinter as tk
from tkinter import filedialog
import os
from googletrans import Translator
from tqdm import tqdm

#https://www.webfx.com/tools/keywordsfx/

def translate_to_french(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='fr')
    return translation.text

def remove_google_shopping(text):
    return text.replace("Keywords", "").strip()

def remove_accents(text):
    return ''.join(char if unicodedata.category(char) != 'Mn' else '' for char in unicodedata.normalize('NFD', text))

def generate_suggestions(csv_file):
    suggestions = []

    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        total_words = sum(1 for row in reader)
        csvfile.seek(0)

        with tqdm(total=total_words, desc="Progression") as pbar:
            for row in reader:
                word = row[0].strip()
                if word:
                    word = remove_google_shopping(word)
                    word = remove_accents(word)
                    translated_word = translate_to_french(word)
                    suggestions.append(translated_word)
                    pbar.update(1)

    return {"suggestions": suggestions}

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    csv_file_path = filedialog.askopenfilename(title="Choisir un fichier CSV", filetypes=[("CSV Files", "*.csv")])

    if not csv_file_path:
        print("Aucun fichier CSV sélectionné. Fin du programme.")
        exit()

    file_name = os.path.splitext(os.path.basename(csv_file_path))[0]
    json_file = f"{file_name}[keywords].json"

    suggestions_data = generate_suggestions(csv_file_path)

    with open(json_file, 'w', encoding='utf-8') as outfile:
        json.dump(suggestions_data, outfile, indent=4, ensure_ascii=False)

    print(f"Conversion CSV vers JSON terminée. Fichier JSON créé : {json_file}")
