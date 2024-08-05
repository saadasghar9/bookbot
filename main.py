def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = get_char_count(text)
    char_sort_list = char_sort(char_counts) 
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for item in char_sort_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
    # def sort_on(dict):
    #     return dict["num"]
    # char_counts.sort(reverse=True, key=sort_on)
    # print(char_counts)
    
def sort_on(e):
    return e["num"]
def char_sort(num_char):
    sorted_list = []
    for ch in num_char:
        sorted_list.append({"char":ch, "num":num_char[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
def get_char_count(text):
    characters = {}
    lowered_case = text.lower()
    for i in lowered_case:
        if i in characters:
            characters[i] += 1
        else:
            characters[i] = 1
    return characters


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
