class Sentence:
    def __init__(self, text):
        self.text = text

    def get_words_number(self):
        words = self.text.split()
        return len(words)

if __name__ == "__main__":
    sentence = input("Please input a sentence: ")
    word = Sentence(sentence)
    word_count = word.get_words_number()
    print(f"The Number of words in the sentence: {word_count}")