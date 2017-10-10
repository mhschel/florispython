import nltk

class Analyzer():
    """Implements sentiment analysis."""

    # stores words of a file into a list
    def load(self, file, storage):
        file = open(file, "r")
        for line in file:
            if line.startswith(';') == False:
                storage.append(line.rstrip("\n"))
        file.close()

    def __init__(self, positives, negatives):
        self.positives = []
        self.negatives = []

        # initialise the tweet tokenizer
        self.tokenizer = nltk.tokenize.TweetTokenizer()

        #store the positive and negative words as a list
        self.load(positives, self.positives)
        self.load(negatives, self.negatives)

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""

        # stores the score to determine sentiment
        score = 0

        # separate the words within the text
        tokens = self.tokenizer.tokenize(text)

        # iterate through each word in text
        for word in tokens:
            if word.lower() in self.positives:
                score =+ 1
            elif word.lower() in self.negatives:
                score =- 1
            else:
                continue
        return score