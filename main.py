import re

def count_words(text):
    return len(text.split())

def read_file():
    with open('books/frankenstein.txt', 'r') as file:
        return file.read()

def count_characters(content):
    content = re.sub(r'[^a-zA-Z]', '', content)

    count_chars = {}
    for char in content:
        char = char.lower()
        if char in count_chars:
            count_chars[char] += 1
        else:
            count_chars[char] = 1
    return count_chars

def sorted_list(count_characters):
    sort_list = []

    for letter, frequency in count_chars.items():
        sort_list += {}


def print_ans(word_count,count_chars):

    sorted_count_chars = sorted(count_chars.items(), key=lambda item: item[1], reverse=True)
    
    print('--- Begin report of books/frankenstein.txt ---')
    print(f"\n {word_count} words found in the document.")

    for letter,frequency in sorted_count_chars:
        print(f"The '{letter}' character was found {frequency} times")

    print('--- End report ---')



    

def main():
    content = read_file()
    # count_words(content)
    # count_characters(content)
    word_count = count_words(content)
    count_chars = count_characters(content)

    print_ans(word_count, count_chars)
    
    # Print the content of the file
    # print(content)
    # print(count_words(content))
    # print(count_characters(content))

main()