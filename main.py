from stats import get_num_words
from stats import get_num_chars_dict
from stats import sort_dict
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    path_to_file = sys.argv[1]
    with open(path_to_file,encoding="utf-8-sig") as f:
        text = f.read()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    chars_dict_list_sorted = sort_dict(get_num_chars_dict(text))
    for k in chars_dict_list_sorted:
        char = k["char"]
        if char.isalpha():
            print(f"{k["char"]}: {k["num"]}")
    print("============= END ===============")

main()