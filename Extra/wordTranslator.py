import os
import json
from translate import Translator
import time

ascii_art = r''' 
GPMailbox wordTranslator

 ckKK0              okKK0KKKKKKKKKKKK0
  cXMM0     oo     kWWWNxoxxxxxxxxxxxd
   dWMWk   0MM0   oWWWWx           
    kWMWd:0MMWW0   KWWO      XNNk     
     0MMWNWMWWMW0  cOO       cWMM   
      XMMMMWxdNMW0           cNMW    
       KXXXx  dXXXx          KXXx    

'''

print(ascii_art)

with open('suggestions.json', 'r', encoding='utf-8-sig') as file:
    data = json.load(file)
    suggestions = data['suggestions']

languages = ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu'
]  

output_directory = 'Translated'
os.makedirs(output_directory, exist_ok=True)

for lang in languages:
    lang_output_filename = os.path.join(output_directory, f'suggestions_{lang}.json')
    if not os.path.exists(lang_output_filename):
        with open(lang_output_filename, 'w', encoding='utf-8') as lang_output_file:
            json.dump({'suggestions': []}, lang_output_file, ensure_ascii=False, indent=2)

for lang in languages:
    print(f"Traduction vers {lang} en cours...")
    
    lang_output_filename = os.path.join(output_directory, f'suggestions_{lang}.json')
    with open(lang_output_filename, 'r', encoding='utf-8') as lang_output_file:
        lang_translations = json.load(lang_output_file)['suggestions']
    
    for idx, word in enumerate(suggestions):
        if idx < len(lang_translations):
            continue
        
        translator = Translator(from_lang='fr', to_lang=lang)
        translation = translator.translate(word)
        
        lang_translations.append((word, translation))
        
        with open(lang_output_filename, 'w', encoding='utf-8') as lang_output_file:
            json.dump({'suggestions': lang_translations}, lang_output_file, ensure_ascii=False, indent=2)
        
        print(f"[{word} fr] => [{translation} {lang}]")
        time.sleep(0.5)
