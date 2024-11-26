# turkish-ngram-model
A Turkish language model using n-grams (1-gram, 2-gram, 3-gram) built on the Turkish Wikipedia Dump dataset. Includes character and syllable tokenization, training-test data preparation, and random sentence generation for NLP tasks and language modeling.

# Important Notes
- I have use wiki-Turkish-dump dataset from Kaggle to build this porject. If you want to use your own dataset, you need to change the "FILE_NAME" parameter in DataPrep.py

![Screenshot 2024-11-27 at 01 10 00](https://github.com/user-attachments/assets/2945263d-fb83-4918-9785-e856068f4178)

- I have used "miratcan/annotated_turkish_syllables.py" to annotate turkish words in DataPrep.py . Due to licence limitations, I could not add that file here.
- If you wanna work with your own test and train data (does not matter if its words, characters or syllables) without my data preparation process just forget about the DataPrep.py file. Create a Train-Test_Data directory and add your train and test data as 2 seperate pickle files (.pkl) respectively. Then change the name of the pickle files in other files accordingly and you are good to go.


## How to run
- If you are going to use the DataPrep.py , first run it. (
