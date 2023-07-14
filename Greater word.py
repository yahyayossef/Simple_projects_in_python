sentence = input("Enter the text:- ")

chopped_sentence = sentence.split()


def greater():
    last_word = ""
    bigger_word = ""
    for i in chopped_sentence:
        if len(i) > len(last_word):
            bigger_word = i
        last_word = i
    return bigger_word


print(greater())
