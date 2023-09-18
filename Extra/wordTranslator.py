import os
import json
from translate import Translator
import time
import socket

def is_internet_available():
    try:
        socket.gethostbyname("dns.google")
        return True
    except:
        return False

def preview_languages(continent):
    print(f"Langues disponibles pour le continent {continent} :")
    for lang in continents[continent]:
        print(f"\033[34m{lang}\033[0m = {language_names[lang]}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def confirm_translation(user_selected_language):
    confirmation = input(f"Êtes-vous sûr de vouloir traduire du français vers {language_names[user_selected_language]} (o/n) ? ").strip().lower()
    return confirmation == 'o'

ascii_art = r''' 
GPMailbox wordTranslator

 ckKK0              okKK0KKKKKKKKKKKK0
  cXMM0     oo     kWWWNxoxxxxxxxxxxxd
   dWMWk   0MM0   oWWWWx           
    kWMWd:0MMWW0  cOO       cWMM     
     0MMWNWMWWMW0  KWWO      XMM   
      XMMMMWxdNMW0           cNMW    
       KXXXx  dXXXx          KXXx    

'''

os.system('cls' if os.name == 'nt' else 'clear')
print(ascii_art)

language_names = {
    'af': 'Afrikaans',
    'sq': 'Albanais',
    'am': 'Amharique',
    'ar': 'Arabe',
    'hy': 'Arménien',
    'az': 'Azéri',
    'eu': 'Basque',
    'be': 'Biélorusse',
    'bn': 'Bengali',
    'bs': 'Bosniaque',
    'bg': 'Bulgare',
    'ca': 'Catalan',
    'ceb': 'Cebuano',
    'ny': 'Chichewa',
    'zh-cn': 'Chinois (simplifié)',
    'zh-tw': 'Chinois (traditionnel)',
    'co': 'Corse',
    'hr': 'Croate',
    'cs': 'Tchèque',
    'da': 'Danois',
    'nl': 'Néerlandais',
    'en': 'Anglais',
    'eo': 'Espéranto',
    'et': 'Estonien',
    'tl': 'Filipino',
    'fi': 'Finnois',
    'fr': 'Français [Par defaut]',
    'fy': 'Frison occidental',
    'gl': 'Galicien',
    'ka': 'Géorgien',
    'de': 'Allemand',
    'el': 'Grec',
    'gu': 'Gujarati',
    'ht': 'Créole haïtien',
    'ha': 'Haoussa',
    'haw': 'Hawaïen',
    'iw': 'Hébreu',
    'hi': 'Hindi',
    'hmn': 'Hmong',
    'hu': 'Hongrois',
    'is': 'Islandais',
    'ig': 'Igbo',
    'id': 'Indonésien',
    'ga': 'Irlandais',
    'it': 'Italien',
    'ja': 'Japonais',
    'jw': 'Javanais',
    'kn': 'Kannada',
    'kk': 'Kazakh',
    'km': 'Khmer',
    'ko': 'Coréen',
    'ku': 'Kurde',
    'ky': 'Kirghize',
    'lo': 'Lao',
    'la': 'Latin',
    'lv': 'Letton',
    'lt': 'Lituanien',
    'lb': 'Luxembourgeois',
    'mk': 'Macédonien',
    'mg': 'Malgache',
    'ms': 'Malais',
    'ml': 'Malayalam',
    'mt': 'Maltais',
    'mi': 'Maori',
    'mr': 'Marathi',
    'mn': 'Mongol',
    'my': 'Birman',
    'ne': 'Népalais',
    'no': 'Norvégien',
    'ps': 'Pachto',
    'fa': 'Persan',
    'pl': 'Polonais',
    'pt': 'Portugais',
    'pa': 'Pendjabi',
    'ro': 'Roumain',
    'ru': 'Russe',
    'sm': 'Samoan',
    'gd': 'Gaélique écossais',
    'sr': 'Serbe',
    'st': 'Sesotho',
    'sn': 'Shona',
    'sd': 'Sindhi',
    'si': 'Sinhala',
    'sk': 'Slovaque',
    'sl': 'Slovène',
    'so': 'Somalien',
    'es': 'Espagnol',
    'su': 'Soundanais',
    'sw': 'Swahili',
    'sv': 'Suédois',
    'tg': 'Tadjik',
    'ta': 'Tamoul',
    'te': 'Télougou',
    'th': 'Thaï',
    'tr': 'Turc',
    'uk': 'Ukrainien',
    'ur': 'Ourdou',
    'ug': 'Ouïghour',
    'uz': 'Ouzbek',
    'vi': 'Vietnamien',
    'cy': 'Gallois',
    'xh': 'Xhosa',
    'yi': 'Yiddish',
    'yo': 'Yoruba',
    'zu': 'Zoulou'
}

output_directory = 'Translated'
os.makedirs(output_directory, exist_ok=True)
for lang_code in language_names.keys():
    lang_output_filename = os.path.join(output_directory, f'suggestions_{lang_code}.json')
    if not os.path.exists(lang_output_filename):
        with open(lang_output_filename, 'w', encoding='utf-8') as lang_output_file:
            json.dump({'suggestions': []}, lang_output_file, ensure_ascii=False, indent=2)

with open('suggestions.json', 'r', encoding='utf-8-sig') as file:
    data = json.load(file)
    suggestions = data['suggestions']

continents = {
    'Afrique': ['af', 'am', 'ar', 'ha', 'ig', 'sn', 'so', 'sw', 'yo'],
    'Amerique (N)': ['fr', 'es','en'],
    'Amerique (S)': ['pt'],
    'Amerique (C)': ['es'],
    'Asie': ['bn', 'gu', 'hi', 'ja', 'jw', 'kn', 'ko', 'ml', 'mr', 'my', 'ne', 'pa', 'si', 'su', 'ta', 'te', 'th', 'ur', 'vi'],
    'Europe': ['en', 'sq', 'ca', 'da', 'de', 'es', 'fr', 'it', 'nl', 'no', 'pl', 'pt', 'ro', 'ru', 'sv'],
    'Oceanie': ['haw'],
}

if not is_internet_available():
    print("Désolé, nous ne pouvons pas accéder aux services Google Traductions en raison d'une erreur de connexion.")
else:
    while True:
        lang_translations = []
        for idx, word in enumerate(suggestions):
            lang_translations.append('')
        if os.path.exists(lang_output_filename):
            with open(lang_output_filename, 'r', encoding='utf-8') as lang_output_file:
                lang_translations = json.load(lang_output_file)['suggestions']

        user_selected_continent = None

        user_choice = input("Choisissez une langue (exemple [en] pour Anglais, 'P' pour Preview des langues, 'Q' pour Quitter) : ").strip().lower()

        if user_choice == 'q':
            break

        if user_choice == 'p':
            clear_screen()
            print("Continents disponibles :")
            for idx, continent in enumerate(continents.keys()):
                print(f"{idx + 1}. {continent}")
            continent_choice = input("Choisissez le numéro du continent ou 'q' pour quitter : ").strip().lower()

            if continent_choice == 'q':
                break

            try:
                continent_index = int(continent_choice)
                continent_list = list(continents.keys())
                if 1 <= continent_index <= len(continent_list):
                    user_selected_continent = continent_list[continent_index - 1]
                else:
                    print("Numéro de continent non valide.")
            except ValueError:
                print("Veuillez entrer un numéro de continent valide.")

            if user_selected_continent:
                clear_screen()
                preview_languages(user_selected_continent)
                language_choice = input(f"Choisissez le code de la langue pour le continent {user_selected_continent} (entrez le code ou 'q' pour quitter) : ").strip().lower()

                if language_choice == 'q':
                    break

                if language_choice in continents[user_selected_continent]:
                    user_selected_language = language_choice
                    if confirm_translation(user_selected_language):
                        clear_screen()
                    else:
                        user_selected_language = None
                else:
                    print("Langue non prise en charge ou invalide.")