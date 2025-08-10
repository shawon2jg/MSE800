class SentenceCheck:
    def __init__(self, text):
        self.text = text

    def get_words_number(self):
        words = self.text.strip().split()
        return len(words)

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    object = SentenceCheck(sentence)
    word_count = object.get_words_number()
    print(f"The Number of words in the sentence: {word_count}")