import os
import json
from translate import Translator
from tqdm import tqdm 

with open('suggestions.json', 'r', encoding='utf-8-sig') as file:
    data = json.load(file)
    suggestions = data['suggestions']

languages = ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu'
]  

output_directory = 'Translated'
os.makedirs(output_directory, exist_ok=True)

for lang in languages:
    print(f"Traduction vers {lang} en cours...")
    
    translated_suggestions = []
    with tqdm(total=len(suggestions), desc=f"Progress ({lang})", unit="word") as pbar:
        for word in suggestions:
            translator = Translator(from_lang='fr', to_lang=lang)
            translation = translator.translate(word)
            translated_suggestions.append(translation)
            pbar.update(1)
    
    translated_data = {'suggestions': translated_suggestions}
    
    output_filename = os.path.join(output_directory, f'suggestions_{lang}.json')
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        json.dump(translated_data, output_file, ensure_ascii=False, indent=2)
        
    print(f'Translated suggestions to {lang} and saved as {output_filename}')