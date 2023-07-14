def repeat(numbers):
    numbers = str(numbers)
    l_num = []
    count_num = 0
    repeating = ""
    for number in numbers:
        if number not in l_num:
            if count_num == numbers.count(number):
                repeating = "No common value"
            elif count_num < numbers.count(number):
                count_num = numbers.count(number)
                repeating = number
            l_num.append(number)
    return repeating


print(repeat(4040400555))
