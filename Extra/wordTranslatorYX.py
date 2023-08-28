import os
import json
from yandex.Translater import Translater
from tqdm import tqdm
import time  # Ajout de l'import pour le module time

def translate_with_retry(translater, text, max_retries=3):
    for _ in range(max_retries):
        try:
            translater.set_text(text)
            return translater.translate()
        except Exception as e:
            print(f"Translation error: {e}")
            print("Retrying after a brief pause...")
            time.sleep(1)
    return None

with open('suggestions.json', 'r', encoding='utf-8-sig') as file:
    data = json.load(file)
    suggestions = data['suggestions']

translater = Translater()

output_directory = 'Translated'
os.makedirs(output_directory, exist_ok=True)

languages = ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu'
]  

for lang_code in languages:
    translater.set_from_lang('fr')
    translater.set_to_lang(lang_code)
    
    print(f"Translating to {lang_code}...")
    
    translated_suggestions = []
    with tqdm(total=len(suggestions), desc=f"Progress ({lang_code})", unit="word") as pbar:
        for word in suggestions:
            translation = translate_with_retry(translater, word)
            if translation:
                translated_suggestions.append(translation)
            pbar.update(1)
    
    translated_data = {'suggestions': translated_suggestions}
    
    output_filename = os.path.join(output_directory, f'suggestions_{lang_code}.json')
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        json.dump(translated_data, output_file, ensure_ascii=False, indent=2)
        
    print(f'Translated suggestions to {lang_code} and saved as {output_filename}')
