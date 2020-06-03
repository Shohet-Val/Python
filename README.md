# Python
palindrom_lst = []
for i in range(101, 999):
    print('i =',i)
    for j in range(i, 999):
        multi_IJ = str(i * j)
        #
        palindrom = multi_IJ[::-1]#
        print(i, '*', j, '=', str(i * j))
        #print(palindrom)
        if palindrom == multi_IJ:
            palindrom=int(palindrom)
            print(palindrom)
            palindrom_lst.append(palindrom)
print(palindrom_lst)
#количество таких чисел
print()
#
print(max(palindrom_lst))
