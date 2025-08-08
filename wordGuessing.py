import random
import random_word_numpy as rw

#region Task 01
def GenerateRandomWord():
    wordList = rw.get_random_word()
    return random.choice(wordList)
#endregion

#region Task 02
def PlayGame():
    print("Hello")
#endregion

if __name__ == "__main__":
    PlayGame()