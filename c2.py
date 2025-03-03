import re

sum_number = 0
file = open("regex_sum_1458553.txt", "r")
while True:
    content = file.readline()
    if not content:
        break
    numbers = re.findall("\d+", content)
    if numbers:
        for number in numbers:
            sum_number += int(number)
print(sum_number)
file.close()
