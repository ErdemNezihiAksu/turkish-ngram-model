# turkish-ngram-model
A Turkish language model using n-grams (1-gram, 2-gram, 3-gram) built on the Turkish Wikipedia Dump dataset. Includes character and syllable tokenization, training-test data preparation, and random sentence generation for NLP tasks and language modeling.

# Important Notes
- I have use wiki-Turkish-dump dataset from Kaggle to build this porject (you need to to dowland it externally). If you want to use your own dataset, you need to change the **FILE_NAME** parameter in DataPrep.py

![Screenshot 2024-11-27 at 01 10 00](https://github.com/user-attachments/assets/2945263d-fb83-4918-9785-e856068f4178)

- I have used **miratcan/annotated_turkish_syllables.py** to annotate turkish words in DataPrep.py . Due to licence limitations, I could not add that file here.
- If you wanna work with your own test and train data (does not matter if its words, characters or syllables) without my data preparation process just forget about the DataPrep.py file. Create a Train-Test_Data directory and add your train and test data as 2 seperate pickle files (.pkl) respectively. Then change the name of the pickle files in other files accordingly and you are good to go.


## How to run
- If you are going to use the **DataPrep.py** , first run it. If not then skip it.
- Secondly, you need to run **N-gram_create.py** to create and save the n-grams as pickle files.
- Then, run **GT_smoothing.py** to apply smoothing to n-grams and save the smoothed probabilities.
- After that, you can run **Perplexity.py** to evaulate your model if you want.
- Finally, you can run **Generate_Sentence.py** to see your model in action.

## Perplexity Results

### Character Based Model
  ![Screenshot 2024-11-27 at 01 32 54](https://github.com/user-attachments/assets/52a65130-47fe-4f58-94f3-df17bce53c24)

### Syllable Based Model
  ![Screenshot 2024-11-27 at 01 33 49](https://github.com/user-attachments/assets/05b63c8b-a729-44d6-aa73-13c9ba6a8675)

## Generated Random Sentences
- There are 3 sentences for each photo.
- Maximum token length (character or syllable count) of a sentence is 50. **`<s>`** means start of sentence, **`</s>`** means end of sentence.

![Screenshot 2024-11-27 at 01 34 43](https://github.com/user-attachments/assets/d483534a-c96c-4174-a3c0-2ef01dd0f2d0)

![Screenshot 2024-11-27 at 01 35 00](https://github.com/user-attachments/assets/8d052f34-a911-47a5-937d-5f7fe1778c89)

![Screenshot 2024-11-27 at 01 35 32](https://github.com/user-attachments/assets/dccd0cfb-ab7d-4347-8569-137f1428db58)

![Screenshot 2024-11-27 at 01 36 00](https://github.com/user-attachments/assets/f978aaad-fd76-4dc7-a244-7da2a25e0972)

![Screenshot 2024-11-27 at 01 36 50](https://github.com/user-attachments/assets/fc8009bc-1fc4-481b-b44a-a13306188ac5)

![Screenshot 2024-11-27 at 01 37 08](https://github.com/user-attachments/assets/76fe71aa-897e-4e79-805f-51ad7af428f0)






