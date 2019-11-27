#import stack from this directory
from stack import Stack

def div_by_two(integer):
    s = Stack()

    while integer > 0:
        remainder = integer % 2
        s.push(remainder)
        integer = integer // 2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num

# uncomment to test
# print(div_by_two(123))
# print(div_by_two(1000))
# print(div_by_two(876))