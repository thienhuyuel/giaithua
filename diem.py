dsmon=['toán','lý','hoá','sinh','anh','văn','sử','địa']
d=[]
for i in range(8):
	print('Nhập điểm môn',dsmon[i])
	n=float(input())
	d.append(n)
print(d)
A=d[0]+d[1]+d[2]
B=d[0]+d[2]+d[3]
C=d[5]+d[6]+d[7]
D=d[0]+d[5]+d[4]