with open("C:/Users/Manny/Documents/python_project_practice/Batch_2/story.txt", "r") as f:
    story = f.read()

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ") # can only use comma on PRINT statements, not on INPUT statements
    answers[word] = answer # dict[i], where i is a single input/key

for word in words:
    story = story.replace(word, answers[word])

print(story)