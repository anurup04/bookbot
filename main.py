import sys 
from stats import word_count
from stats import char_count
from stats import make_report
from stats import sort_on
from stats import list_from_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
        num_words = word_count(text)
        num_char = char_count(text)
        make_report(num_words,num_char)


main()
