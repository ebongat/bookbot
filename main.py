def main():
    book_path = "books/frankenstein.txt"
    text = get_book_contents(book_path)
    word_count = get_word_count(text)
    letters, symbols = get_character_count(text)
    letter_count = sort_dictionary(letters)
    symbol_count = sort_dictionary(symbols)
    print(f"---Getting report on {book_path}---\n")
    print(f"There are {word_count} words found in the document.\n")
    for letter, count in letter_count:
        print(f"{letter} is found {count} times.")
    for symbol, count in symbol_count:
        print(f"{symbol} is found {count} times.")
    print("\n---End of Report---")


def get_book_contents(path):
    with open(path) as file:
        return file.read()

def get_word_count(text):
    word_list = text.split()
    return len(word_list)

def get_character_count(text):
    lowered_text = text.lower()
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letter_counts = {}
    symbol_counts = {}
    for char in lowered_text:
        if char in alphabet_list:
            letter_counts[char] = letter_counts.get(char, 0) + 1 
        else:
            symbol_counts[char] = symbol_counts.get(char, 0) + 1
    return letter_counts, symbol_counts

def sort_dictionary(dict):
    sorted_dictionary = sorted(dict.items(), key=lambda item:item[1], reverse=True)
    return sorted_dictionary

main()
