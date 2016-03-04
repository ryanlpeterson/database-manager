import sys

print("Enter word: ")

word = sys.stdin.readline()

while (word != "1"):

    print(len(word))

    print("Enter word: ")

    word = sys.stdin.readline()