def add_commands_and_underscore(number):
    if len(str(number)) <= 3:
        return number
    else:
        length = len(str(number))
        number_after = int(str(number)[: length - 3])
        return f"{number:_d}\r{number_after:,d}"


print(add_commands_and_underscore(78789989))
