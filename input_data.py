from translate import YandexTranslate
import os


user_translate = YandexTranslate()

def main(text, lang):
    directory_folder = r"./Outfiles"
    filename = input('Input file name output : ')
    FileFullPath = os.path.join(directory_folder, filename)
    with open(FileFullPath, 'w',encoding='utf-8') as f:
        print(user_translate.translate_it(text, lang), file=f)


if __name__ == '__main__':
    out_lang = input('Enter the language into which to translate : ')
    if out_lang == '':
        out_lang = 'ru'
    main(open(input('Input file name in : '), encoding='utf-8'), out_lang)
