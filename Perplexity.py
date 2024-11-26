import math
import pickle

with open("Smoothed_Probs/smoothed_probs_chars.pkl", "rb") as file:
    smoothed_probs_chars = pickle.load(file)

with open("Smoothed_Probs/smoothed_probs_syls.pkl", "rb") as file:
    smoothed_probs_syls = pickle.load(file)

with open("N-gram_tables/ngram_table_syl_test.pkl", "rb") as f:
    ngrams_syl_test = pickle.load(f)

with open("N-gram_tables/ngram_table_char_test.pkl", "rb") as f:
    ngrams_char_test = pickle.load(f)


def calculate_perplexity(test_ngrams, smoothed_probabilities):
    log_sum = 0
    N = sum(test_ngrams.values())

    for ngram, freq in test_ngrams.items():
        prob = smoothed_probabilities.get(ngram, smoothed_probabilities['<unseen>'])
        log_sum += math.log(prob) * freq

    perplexity = math.exp(-log_sum/N)
    return perplexity


for n, ngram in ngrams_char_test.items():
    word_perplexity = calculate_perplexity(ngram, smoothed_probs_chars[n])
    print(f"Character based {n}-Gram Perplexity:", word_perplexity)

print("")
# Hece tabanlı perplexity
for n, ngram in ngrams_syl_test.items():
    syl_perplexity = calculate_perplexity(ngram, smoothed_probs_syls[n])
    print(f"Syllable based {n}-Gram Perplexity:", syl_perplexity)

