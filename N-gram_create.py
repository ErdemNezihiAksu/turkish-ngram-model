from collections import defaultdict
import pickle

def generate_ngrams(tokens, n):
    return [tuple(tokens[i:i+n]) for i in range(len(tokens) - n + 1)]

def create_ngram_tables(sentences, max_n=3):

    ngram_tables = {n: defaultdict(int) for n in range(1, max_n+1)}
    
    for sentence in sentences:
        for n in range(1, max_n+1):
           
            ngrams = generate_ngrams(sentence, n)
            for ngram in ngrams:
                ngram_tables[n][ngram] += 1

    return ngram_tables

with open("Train-Test_Data/syllable_data.pkl", "rb") as f:
    syllable_data = pickle.load(f)

with open("Train-Test_Data/character_data.pkl", "rb") as f:
    char_data = pickle.load(f)

char_train , char_test = char_data["train"] , char_data["test"]
syl_train, syl_test = syllable_data["train"], syllable_data["test"]


ngram_tables_char_train = create_ngram_tables(char_train)
ngram_tables_char_test = create_ngram_tables(char_test)
ngram_tables_syl_train = create_ngram_tables(syl_train)
ngram_tables_syl_test = create_ngram_tables(syl_test)

with open("N-gram_tables/ngram_table_char_train.pkl", "wb") as file:
    pickle.dump(ngram_tables_char_train, file)

with open("N-gram_tables/ngram_table_syl_train.pkl", "wb") as file:
    pickle.dump(ngram_tables_syl_train, file)

with open("N-gram_tables/ngram_table_char_test.pkl", "wb") as file:
    pickle.dump(ngram_tables_char_test, file)

with open("N-gram_tables/ngram_table_syl_test.pkl", "wb") as file:
    pickle.dump(ngram_tables_syl_test, file)
