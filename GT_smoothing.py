import pickle
from collections import defaultdict

with open("N-gram_tables/ngram_table_syl_train.pkl", "rb") as f:
    ngrams_syl_train = pickle.load(f)

with open("N-gram_tables/ngram_table_char_train.pkl", "rb") as f:
    ngrams_char_train = pickle.load(f)


def calculate_frequencies(ngram_table):
    freq_count = defaultdict(int)
    for freq in ngram_table.values():
        freq_count[freq] += 1
    return freq_count


def good_turing_smoothing(ngram_tables):
    smoothed_probabilities_table = {}

    for n, ngram_table in ngram_tables.items():
        total_observations = sum(ngram_table.values())
        freq_count = calculate_frequencies(ngram_table)
        smoothed_probabilities = {}

        unseen_prob = freq_count[1] / total_observations if 1 in freq_count else 1e-10
        smoothed_probabilities['<unseen>'] = unseen_prob

        for ngram, count in ngram_table.items():
            c = count
            Nc = freq_count[c]
            Nc_plus_1 = freq_count.get(c + 1, 0)

            if c > 1:

                if Nc_plus_1 > 0:
                    c_star = (c + 1) * Nc_plus_1 / Nc
                else:
                    c_star = c 
    
            if n == 1:
                smoothed_probabilities[ngram] = c_star / total_observations
            else:
                prev_ngram_key = ngram[:n-1]
                prev_count = ngram_tables[n-1].get(prev_ngram_key,0)
                smoothed_probabilities[ngram] = c_star / prev_count
        
        smoothed_probabilities_table[n] = smoothed_probabilities
            
    return smoothed_probabilities_table


smoothed_probs_chars = good_turing_smoothing(ngrams_char_train)
smoothed_probs_syls = good_turing_smoothing(ngrams_syl_train)


with open("Smoothed_Probs/smoothed_probs_chars.pkl", "wb") as file:
    pickle.dump(smoothed_probs_chars, file)

with open("Smoothed_Probs/smoothed_probs_syls.pkl", "wb") as file:
    pickle.dump(smoothed_probs_syls, file)
