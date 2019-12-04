'''
brute force method (stupid)
'''
import time
start = time.time()
# fact 2 range
puzzle = '134564-585159'
min_range, max_range = puzzle.split('-')
min_range, max_range = int(min_range), int(max_range)


# fact 1 len == 6
def six_digits(xxx):
    word = str(xxx)
    return len(word) == 6


# fact 3 at teast two same digits
def same_digits(xxx):
    word = str(xxx)
    given = [word[i] == word[i + 1] for i in range(len(word) - 1)]
    return any(given)


# fact 4 never decrease
def asc_digits(xxx):
    word = str(xxx)
    given = [int(word[i]) <= int(word[i + 1]) for i in range(len(word) - 1)]
    return all(given)


count = 0
for num in range(min_range, max_range):
    if six_digits(num) and same_digits(num) and asc_digits(num):
        count += 1
print(count)


print('czas: ', time.time() - start)
