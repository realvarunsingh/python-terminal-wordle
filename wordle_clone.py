import datetime
import random

# pass in a lowercase and no whitespace guess and the real word
# returns an array of g, y, or - where g is green, y is yellow, - is not there
# O(n)
def check_guess(guess, real_word):
    assert len(guess) == len(real_word)

    real_letters = set(real_word)
    real_counts = {}
    for char in real_word:
        real_counts[char] = real_counts.get(char, 0) + 1
    output_list = ['']*5
    for i,char in enumerate(guess):
        if char in real_letters and real_counts[char]>0:
            real_counts[char] -= 1
            if guess[i] == real_word[i]:
                output_list[i] = 'g'
            else:
                output_list[i] = 'y'
        else:
            output_list[i] = '-'
    return output_list


def game_loop(real_word):
    wordle_guesses_file = open('./wordle_list_answers.txt')
    valid_guesses = set(wordle_guesses_file.read().split('\n'))
    wordle_guesses_file.close()

    for guess_num in range(6):

        guess_input = ''
        while (guess_input not in valid_guesses or len(guess_input) != 5):
            guess_input = input('Enter guess ({}/6): '.format(guess_num+1))
            if guess_input == 'exit':
                break
            elif guess_input not in valid_guesses:
                print('Not a valid guess.')
        if guess_input == 'exit':
            break
        
        guess_result = check_guess(guess_input.strip().lower(), real_word)
        print(str(guess_result) + '\n')
        if all([x == 'g' for x in guess_result]):
            print("Well done! You guessed the word: {}! \n".format(real_word))
            break
        elif guess_num == 5:
            print("Unfortunately, you could not guess the word. It was {}! \n".format(real_word))

def main():
    random.seed(str(datetime.date.today()))
    wordle_words_file = open('./wordle_list_answers.txt')
    word_list = wordle_words_file.read().split('\n')
    todays_word = random.choice(word_list)
    wordle_words_file.close()
    game_loop(todays_word)

if __name__ == "__main__":
    main()