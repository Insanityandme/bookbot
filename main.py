def main():
    book_path = "books/frankenstein.txt"

    text = get_book_text(book_path)
    num_words = get_num_words(text) 
    chars_dict = get_chars_dict(text)
    chars_list_of_dicts = []

    for char in chars_dict:
        if char.isalpha():
            chars_list_of_dicts.append(
                {"letter": char, "num": chars_dict[char]}
            )

    chars_list_of_dicts.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    for elem in chars_list_of_dicts:
        print(f"The {elem['letter']} was found {elem['num']} times")

    print("--- End report ---")

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

def get_num_words(text):
    words = text.split()

    return len(words)

def get_chars_dict(text):
    chars = {}

    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]

main()
