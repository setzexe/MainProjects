from deep_translator import GoogleTranslator                                                    # imports GoogleTranslator (which uses Google's API) from deep-translator, maintained specifically for translation services
from pypinyin import pinyin, Style                                                              # Imports pinyin & stylying for pinyin. Translates raw Hanzi to pinyin (Chinese is not written in Pinyin)

def main():
    try:
        english = input("Enter text to translate: ")
    except: 
        print("Bad input!")
    
    # translate English to Chinese (Simplified)
    hanzi_text = GoogleTranslator(source='en', target='zh-CN').translate(english)               # GoogleTranslates (with the preset source, english, and output language, simplified chinese) the english translation via Translate
    print(f"{english} to Hanzi: {hanzi_text}")
    
    # convert Hanzi to Pinyin
    pinyin_text = ' '.join([item[0] for item in pinyin(hanzi_text, style=Style.TONE)])          # The Pinyin function translates the hanzi into a set toned list of pinyin characters. Because this is a list, we can join each item[0] (because one element per loop) together
    print(f"{english} to Pinyin: {pinyin_text}")

if __name__ == "__main__":
    main()

