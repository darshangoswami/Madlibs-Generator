with open('Madlibs_Generator/story.txt', 'r') as f:
  story = f.read()

words = set()
start_of_word = -1

word_start = '<'
word_end = '>'

for i, char in enumerate(story):
  if char == word_start:
    start_of_word = i

  if char == word_end and start_of_word != -1:
      word = story[start_of_word: i + 1]
      words.add(word)
      start_of_word = -1

answers = {}

for word in words:
   answer = input("Enter a word for " +  word + ":")

   answers[word] = answer

print(answers)