from string import ascii_letters


def get_missed(group):
    f_litter = group[0]
    l_litter = group[-1]

    f_piece = ascii_letters.index(f_litter)
    l_piece = ascii_letters.index(l_litter)

    complete = ascii_letters[f_piece : l_piece + 1]

    result = ""

    for letter in complete:
        if letter not in group:
            result += letter
            if letter == "z":
                break
    return result


print(get_missed("fghijl"))
