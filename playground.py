import random
from time import sleep








def main():


    # String Slicing
    words = ["Wet Pussy", "Big Fat Old Mantits", "Brady and Noah are genius", "I wanna fuck Selena Gomez",
             "biiiiiiiiiiiiiiiiiiiiiig boooooooooooooooooooty biiiiiiiiiiiiiiiiiiitches"]

    # Like lists, we can enumerate strings, then we can easily slice them at all indices
    while(True):
        word = random.choice(words)
        for index, curchar in enumerate(word):
            print(word[:index]+curchar)
            sleep(.01)

        for index, curchar in enumerate(word):
            print(word[index:])
            sleep(.01)


    return





























if __name__ == "__main__":
    main()