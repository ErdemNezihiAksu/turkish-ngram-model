import re
from syllabify import get_syllables
from sklearn.model_selection import train_test_split
import pickle

FILE_NAME = 'wiki.txt'

def data_preparation(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    text = re.sub(r"<doc.*?>.*\n.*", "", text)
    text = re.sub(r"</doc>", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r'(?m)^\s*.*\balign\b.*$', '', text)
    text = re.sub(r'(?m)^.*!colspan.*$', '', text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r'[\"\'\(\)\{\}\[\]]', '', text)

    text = text.lower()
    text = re.sub("i̇", "i", text)


    sentences = re.findall(r'.+?(?<!\d)(?:\.{3}|[.!?:])', text)

    processed_sentences = [sentence.strip() for sentence in sentences]

    regex = r'<s>|</s>|\b[a-zA-Zçğıi̇öşüÇĞİÖŞÜ]+\b|\d+\.\d*|\d+|\’|\.{3}|[:.,!?/\{\}\[\]!\;\`\"\'\<\>\(\)-]'
    tokens =[['<s>'] + re.findall(regex, sentence) + ['</s>'] for sentence in processed_sentences]

    return tokens



def character_based_model(tokens):
    char_data = []
    for token in tokens:
        sentence = []
        sentence.append(token[0])
        for word in token[1:-1]:
            sentence += [char for char in word]
        sentence.append(token[-1])
        char_data.append(sentence)
    char_train, char_test = train_test_split(char_data, test_size=0.05, random_state=42)
    data = {
        "train" : char_train,
        "test" : char_test
    }
    with open("Train-Test_Data/character_data.pkl", "wb") as file:
        pickle.dump(data, file)
    
def syllable_based_model(tokens):
    syllable_data = []
    for token in tokens:
        sentence = []
        sentence.append(token[0])
        for word in token[1:-1]:
            sentence += get_syllables(word)
        sentence.append(token[-1])
        syllable_data.append(sentence)

    syllable_train, syllable_test = train_test_split(syllable_data, test_size=0.05, random_state=42)
    data = {
        "train" : syllable_train,
        "test" : syllable_test
    }
    with open("Train-Test_Data/syllable_data.pkl", "wb") as file:
        pickle.dump(data, file)


text = data_preparation(FILE_NAME)
character_based_model(text)
syllable_based_model(text)


    
