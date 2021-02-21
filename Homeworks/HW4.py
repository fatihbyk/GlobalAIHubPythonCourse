import random as rnd

class word:
    def get_word(self):
        self.word_list = ["perfect", "python", "programming", "replacement","learner","candidate","tutorial","hacking","book"]
        self.word = rnd.choice(self.word_list)
        return self.word
class game:
    def __init__(self,word):
        self.word_as_list=[]
        self.word_guesses=[]
        self.chances=5

    def guessed_true_or_false(self,letter,get_word):
        self.word_guesses.append(letter)
        for letter in get_word:
            if letter in self.word_guesses:
                print(letter,end=" ")
            else:
                print("_",end=" ")
    def guess_whole_word(self,guessed_word,get_word):
        if (guessed_word==get_word):
            print("\nCongratulations ! You found the word !!")
        else:
            print("Wrong Answer !! Please try again!!")
            self.chances -= 1

class main(word):
    w = word()
    get_word = w.get_word()
    g = game(get_word)
    done=False
    print("lets play hangman!!")
    while (not done) :
        guess = str(input("please guess a character:"))
        g.guessed_true_or_false(guess,get_word)
        YesorNo=str(input("\nDo you want to guess whole word? If yes, please enter y "))
        if(YesorNo=='y'):
            whole_word=str(input("\nPlease enter whole word :"))
            g.guess_whole_word(whole_word,get_word)
        if guess not in get_word:
            g.chances -=1
            if g.chances==0:
                break
        print("Your remaining guesses :",g.chances)
        done=True
        for letter in get_word:
            if letter not in g.word_guesses:
                done=False
    if done:
        print("\nCongratulations ! You found the word !!")
    else:
            print("\nSorry , You lost The word was ",get_word)





