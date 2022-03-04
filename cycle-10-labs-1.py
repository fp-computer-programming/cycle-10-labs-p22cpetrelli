#author CJP 03/04/2022
def num(number):
    x = 1
    while x < number:
        number = number + x
        x += 1
        return number

print(num(6))
print(num(4))
print(num(10))