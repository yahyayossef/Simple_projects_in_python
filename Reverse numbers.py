def reverse_number(numbers):
    numbers = str(numbers)
    list_numbers = []
    for i in range(1, len(numbers) + 1):
        list_numbers.append(int(numbers[-i]))

    return list_numbers


print(reverse_number(75655))
