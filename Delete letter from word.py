def remove_char(sentence, char):
    sentence = sentence.replace(char.lower(), "")
    return sentence.replace(char.upper(), "")


print(remove_char("Yahya", "Y"))
