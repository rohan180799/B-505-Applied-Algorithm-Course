e = [121, 345, 436, 234, 667, 535]
unit = []
tens = []
hundreds = []
d = []


def counting(e, exp):
    sorted_arr = [0 for i in range(len(e))]

    count = [0] * (10)

    for i in range(0, len(e)):
        index = e[i] // exp
        count[index % 10] += 1

    for i in range(1, len(count)):
        count[i] = count[i] + count[i - 1]

    for i in range(len(e)):
        index = e[i] // exp
        sorted_arr[count[index % 10] - 1] = e[i]
        count[index % 10] -= 1

    for i in range(0, len(sorted_arr)):
        e[i] = sorted_arr[i]

    print (e)


# for i in range(0, len(e)):
#     unit.append(e[i] % 10)
# print (unit)
#
# for i in range(0, len(e)):
#     tens.append(e[i] % 100)
# print (tens)
#
# for i in range(0, len(e)):
#     hundreds.append(e[i] % 1000)
# print (hundreds)


# def get_digits(n):
#     digits = [n % 10]
#     n = n // 10
#     while n > 0:
#         digits.insert(0, n % 10)
#         n = n // 10
#     return digits
#
#
# for i in range(0, len(e)):
#     d.append(get_digits(e[i]))
# print (d)
#
# for i in range(0, len(d)):
#     for j in range(0, len(d[i])):
#         if j == 0:
#             hundreds.append(d[i][j])
#         if j == 1:
#             tens.append(d[i][j])
#         if j == 2:
#             unit.append(d[i][j])
# # print (unit)
# print (tens)
# # print (hundreds)
#
# # insertion(unit, c, s)
# # insertion(tens, c, s)
# insertion(hundreds, c, s)


def radixSort(arr):
    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp1 = 1
    while max1 / exp1 > 0:
        counting(e, exp1)
        exp1 *= 10


radixSort(e)
