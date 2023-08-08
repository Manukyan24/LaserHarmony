
"""-----------------------------------"""


def check_if_bin(num, i):
    return num & (0x01 << i) == 2**i

#print(check(200,7))


"""-----------------------------------"""

def none_zero_list(num):
    arr = []
    for i in range(7): 
        arr.append(i) if check_if_bin(num, i) else arr
    return arr

arr = [55,62,65,73,82,87,98]


#print(none_zero_list(20))


































# data = 20

# binData = format(data, "b")
# print(binData)

# strBinData = str(binData)
# print(strBinData)

# dataList = list(strBinData)
# print(dataList)
# for i in range(7-len(dataList)):
#     dataList.insert(0,0)

# print(dataList)

# for i in range(len(dataList)):
#     if dataList[i] == "1":
#         print(True)
#     else:
#         print(False)

#betwise oprator
