from deep_translator import GoogleTranslator                                                   
from pypinyin import pinyin, Style                                                              

def main():
    try:
        english = input("Enter text to translate: ")
    except: 
        print("Bad input!")
    
    # translate English to Chinese (Simplified)
    hanzi_text = GoogleTranslator(source='en', target='zh-CN').translate(english)              
    print(f"{english} to Hanzi: {hanzi_text}")
    
    # convert Hanzi to Pinyin
    pinyin_text = ' '.join([item[0] for item in pinyin(hanzi_text, style=Style.TONE)])          
    print(f"{english} to Pinyin: {pinyin_text}")

if __name__ == "__main__":
    main()


