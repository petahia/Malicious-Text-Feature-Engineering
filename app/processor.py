from collections import Counter
import nltk
from nltk.corpus import words
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Processor:
    def __init__(self,collection):
        self.dataframe = collection


    def find_rarest_word(self):
        def rarest(text):
            words = text.split()
            counts = Counter(words)
            rarest_word = min(counts, key=counts.get)
            return rarest_word
        self.dataframe['word_rarest'] = self.dataframe['Text'].apply(rarest)
        return self.dataframe

    def find_sentiment_word(self):
        def sentiment(text):
            nltk.download('vader_lexicon')
            score = SentimentIntensityAnalyzer().polarity_scores(text)
            return score['compound']
        self.dataframe['sentiment'] = self.dataframe['Text'].apply(sentiment)
        return self.dataframe


    def detected_weapons(self):
        def weapons(text):
            with open('/Users/petahiam/PycharmProjects/malicious_text_eng./data/weapon_list.txt', 'r') as file:
                rows = [row for row in file.readlines()]
                words = text.split()
                for word in words:
                    if word in rows:
                        return word
                return None
        self.dataframe['weapon_detected'] = self.dataframe['Text'].apply(weapons)
        return self.dataframe














