list1 = [1,3,4,16,32,8,64,4,128,2,256,32]

print("các cặp số có tích bằng 256 ở list 1 là:")
for i in range(len(list1)):
    num1 = list1[i]
    list1[i]=0
    for j in range(len(list1)):
        num2 = list1[j]
        if num1*num2 == 256:
            list1[j]=0
            print(num1,"và",num2, "ở vị trí số",i+1,"và",j+1)
            num1 = num2 = 0

list2 = [12,2,4,2,128,64,16,7,1,64,32,16,5,8]

print("các cặp số có tích bằng 256 ở list 2 là:")
for i in range(len(list1)):
    num1 = list2[i]
    list2[i]=0
    for j in range(len(list2)):
        num2 = list2[j]
        if num1*num2 == 256:
            list2[j]=0
            print(num1,"và",num2, "ở vị trí số",i+1,"và",j+1)
            num1 = num2 = 0