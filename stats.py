def get_num_words(text):
    word_list = []
    word_list = text.split()
    return len(word_list)

def get_num_chars_dict(text):
    chars = {}
    text = text.lower()
    for c in text:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def sort_on(d):
    return d["num"]

def sort_dict(chars_dict):
    chars_dict_list = []
    for k in chars_dict:
        chars_dict_list.append({"char":k,"num":chars_dict[k]})
    chars_dict_list.sort(reverse=True,key=sort_on)
    return chars_dict_list
