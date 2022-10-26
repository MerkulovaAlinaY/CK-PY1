import random


def get_unique_list_numbers(_) -> list[int]:
    global list_unique_numbers
    list_numbers = []
    for i in range(15):
        list_numbers.append(random.randint(-10, 10))
        list_unique_numbers = list(set(list_numbers))
    return list_unique_numbers


list_unique_numbers = get_unique_list_numbers(list(set()))
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))