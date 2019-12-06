from e04_1 import six_digits, asc_digits, same_digits, min_range, max_range
import time
import re


# adjacent matching not part of larger group
# 123444 => False
# 111122 => True
def not_larger_group(xxx):
    word = str(xxx)
    res = re.compile(r'(\d)\1')     # looking for repetitives digits
    groups = res.findall(word)
    triplets = 0
    for digit in groups:            # looking for triplets
        if digit * 3 in word:
            triplets += 1
    if triplets < len(groups):      # eg 123444 triplets=1 = groups=1 => False
        return True                 # eg 111122 triplets=1 < groups=2 => True
    else:
        return False


if __name__ == '__main__':
    start = time.time()
    count = 0
    for num in range(min_range, max_range):
        if six_digits(num) and same_digits(num) and asc_digits(num) and not_larger_group(num):
            count += 1
    print(count)
    print('czas: ', time.time() - start)
