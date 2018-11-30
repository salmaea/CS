import sys
num_of_char = 0
num_of_words = 0
num_of_lines = 0
for filename in sys.argv[1:]:
    with open(filename, 'r') as file:
        text = file.read()
        num_of_char = num_of_char + len(text)
        words = text.split()
        num_of_words = num_of_words + len(words)
        num_of_lines = num_of_lines + text.count('\n')
print(num_of_char, num_of_words, num_of_lines, filename)
