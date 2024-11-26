import pickle 
import random

with open("Smoothed_Probs/smoothed_probs_chars.pkl", "rb") as file:
    smoothed_probs_chars = pickle.load(file)

with open("Smoothed_Probs/smoothed_probs_syls.pkl", "rb") as file:
    smoothed_probs_syls = pickle.load(file)

def generate_sentence(smoothed_probabilities, n, max_length=30):
    sentence = ['<s>'] if n > 1 else []  

    for _ in range(max_length):
        if n == 1:
         
            top_candidates = sorted(smoothed_probabilities.items(), key=lambda x: x[1], reverse=True)[:5]
        else:

            found = False
            context_length = min(n - 1, len(sentence))

            while context_length > 0:
                context = tuple(sentence[-context_length:])
                candidates = {ngram: prob for ngram, prob in smoothed_probabilities.items() if ngram[:context_length] == context}
                
                if candidates:
                    found = True
                    break
                context_length -= 1
            
            if not found:
                break
            

            top_candidates = sorted(candidates.items(), key=lambda x: x[1], reverse=True)[:5]
        

        next_ngram = random.choice(top_candidates)[0]
        if len(sentence) == 1 and n == 3:
            sentence.append(next_ngram[-2])
        sentence.append(next_ngram[-1])
        

        if next_ngram[-1] == '</s>':
            break

    return ' '.join(word for word in sentence )


for n in [1,2,3]:
    print(f"Character based senctences for {n}-gram:\n")
    for _ in range(3):
        sentence = generate_sentence(smoothed_probs_chars[n],n)
        print(sentence)
    print("\n\n")


for n in [1,2,3]:
    print(f"Syllable based senctences for {n}-gram:\n")
    for _ in range(3):
        sentence = generate_sentence(smoothed_probs_syls[n],n)
        print(sentence)
    print("\n\n")
