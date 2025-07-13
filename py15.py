# function แบบ default parameter
# default parameter คือ พารามิเตอร์ที่มีการกำหนดค่า default ให้มัน
# โดยเวลาเรียกใช้ฟังก์ชัน หากไม่ส่งค่าให้พารามิเตอร์ตัวนั้น จะใช้ค่า default ที่กําหนดไว้
#             0   1  2   3
#            -4  -3  -2  -1
listdata1 = [10, 20, 30, 40]
#             0  1      2      3      4
#            -5  -4     -3    -2     -1
listdata2 = [10, 20, 'Timmy',True, [1, 2, 3] ]
print(listdata1[2])
print(listdata1[-2])
print('---------------')
print(listdata2[3])
listdata2[3] = False
print(listdata2[-2])

print(listdata2[-1])
listdata2[-1][0]=111
listdata2[-1][1]=222
listdata2[-1][2]=333
print(listdata2[-1])
