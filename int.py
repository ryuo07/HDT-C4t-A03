prime = int(input("enter a number:"))
count = 0
for i in range(1,int((prime**0.5)//1)+1,1):
    if prime % i == 0 :
        count += 1
if count == 1:
    print(prime, "là số nguyên tố")
else:
    print(prime, "không phải số nguyên tố")