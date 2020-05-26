dai = int(input("nhập độ dài cạnh dài của hình chữ nhật: "))
rong = int(input("nhập độ dài cạnh ngắn của hình chữ nhật: "))
list1 = []
swap = True
i = 0
while swap:
    dn = 2**i
    if dai >= dn and rong>= dn:
        list1.append(dn)
        i += 1
    else:
        swap = False
slg0 = 0
print("hình có độ dài",dai,"x",rong,"được tạo bởi:")
for j in range(len(list1)-1,-1,-1):
    num = list1[j]
    slg1 = dai // num
    slg2 = rong // num
    slg3 = slg1*slg2 - slg0*4
    slg0 = slg1*slg2
    print(slg3,"hình vuông cỡ",num,"x",num)