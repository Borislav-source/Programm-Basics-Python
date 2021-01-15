# # # word = input()
# # # a = ''
# # #
# # # for i in range(len(word) -1, -1, -1 ):
# # #     a = word[i]
# # #     print(a)
# #
# # print(0 % 3)
#
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# for i in range(1, len(list1) + 1):
#     print(list2[:i] + list1[i:])
# 0 for _ in range(10)
# new_list = [1, 1, 2, 2, 3, 2, 0, 1, 0, 3]
# for i in range(len(new_list)):
#     new_list[i] = new_list[i] * 2
# print(new_list)
# a = '3'
# a= int(a)
# print(a)


# def swap(element, i, j):
#     return ''.join((element[:i], element[j], element[i+1:j], element[i], element[j+1:]))
#
#
# message = input().split()
# for element in message:
#     if 0 < int(element[2]) < 9:
#         element = (chr(int(element[:3])) + element[3:])
#         print(swap(element, 1, len(element)-1))
# index = 2
# value = 1
# b=[]
# a = [1, 5, 2, 3, 4, 6, 7, 8]
# # for i in range (a[index - value], a[index + value]):
# #     b.append(i)
# # # a.remove(a[index - value])
# # print(b)
#
# a = [1, 5, 2, 3, 4, 6, 7, 8, 9, 10]
# print(len(a))
# a = a[:index - value] + a[index + value + 1:]
# print(a)
# if index + value <= len(targets) and index - value >= 0:
#     targets = targets[:index - value] + targets[index + value + 1:]

# value = 4
# a = 'asdfghj'
# print(a[:value] + a[value + 1:])

targets = list(map(int, input().split()))
data = input()
while not data == 'End':
    data = data.split()
    command = data[0]
    index = int(data[1])
    value = int(data[2])
    if command == 'Shoot':
        if len(targets) > index >= 0:
            targets[index] -= value
            if targets[index] <= 0:
                targets.remove(targets[index])
    elif command == 'Add':
        if len(targets) > index >= 0:
            targets.insert(index, value)
        else:
            print('Invalid placement!')
    elif command == 'Strike':
        if index + value < len(targets) and index - value >= 0:
            targets = targets[:index - value] + targets[index + value + 1:]
        else:
            print('Strike missed!')
    data = input()
[print(targets[trg], end='|') if trg < len(targets) - 1 else print(targets[trg]) for trg in range(len(targets))]