# list_a = []

# while True:
#     input_a = input("구매할 과일을 입력하세요 : ")

#     list_a.append(input_a)

#     print(list_a)

#     if not len(list_a) == 5 :
#         if input_a in list_a:
#             index_a = list_a.index(input_a)
#             list_a.pop()
#             print(f'{input_a}는 이미 있습니다.')
#     else:
#         break


#######################
list_a = []

while len(list_a) < 5:
    input_a = input("구매할 과일을 입력하세요 : ")

    if input_a in list_a:
        print(f'{input_a}는 이미 있습니다.')
    else:
        list_a.append(input_a)

    print(list_a)


# 24