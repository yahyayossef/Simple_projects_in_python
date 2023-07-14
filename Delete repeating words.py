text = input("Enter the text:- ")


def dis_repetition(l_str) -> list:
    for word in l_str:
        word.lower()
        index = l_str.index(word)

        for o_word in l_str[index + 1:]:
            o_word.lower()
            if word == o_word:
                l_str.reverse()
                l_str.remove(o_word)
                l_str.reverse()

    return " ".join(l_str)


text = dis_repetition(text.split())
print(text)
