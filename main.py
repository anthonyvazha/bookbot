def count_words(text):
    return len(text.split())

def read_file():
    with open('books/frankenstein.txt', 'r') as file:
        return file.read()

def count_characters(content):
    count_chars = {}
    for char in content:
        char = char.lower()
        if char in count_chars:
            count_chars[char] += 1
        else:
            count_chars[char] = 1

    return count_chars

    

def main():
    content = read_file()
    count_words(content)
    count_characters(content)

    # Print the content of the file
    print(content)
    print(count_words(content))
    print(count_characters(content))

main()