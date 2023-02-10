file_name = 'text.txt'

def read_file():
    f = open(file_name, 'r')
    text = f.read()
    f.close()
    return text

def get_list_of_word(text):
    text2 = ''
    for char in text:
        if char.isalpha() or char.isnumeric() or char == ' ':
            text2 += char
    words = text2.split(' ')
    return words

def find_longest_and_shortest(words):
    min_len = len(min(words, key = len))
    max_len = len(max(words, key = len))
  
    shortest = []
    longest = []

    for w in words:
        if len(w) == min_len:
            shortest.append(w)
        if len(w) == max_len:
            longest.append(w)

    return shortest, longest

text = read_file()
words = get_list_of_word(text)
shortest, longest = find_longest_and_shortest(words)

print("longest = " + str(longest))
print("shortest = " + str(shortest))