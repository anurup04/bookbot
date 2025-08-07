import sys

def word_count(text):
    text_in_words = text.split()
    total_count = len(text_in_words)
    return total_count

def char_count(text):
    char_dict = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1   
    return char_dict

def sort_on(items):
    return items["num"]

def list_from_dict(dict):
    count_list = []
    for key in dict:
        count_list.append({"name":key,"num":dict[key]})
    return count_list


def make_report(total_count,char_dict):
    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {total_count} total words")
    print("--------- Character Count -------")
    final_list = list_from_dict(char_dict)
    final_list.sort(reverse=True, key=sort_on)
    for member in final_list:
        print(f"{member['name']}: {member['num']}")
    print("============= END ===============")
    return None
