# function แบบ default parameter
# default parameter คือ พารามิเตอร์ที่มีการกำหนดค่า default ให้มัน
# โดยเวลาเรียกใช้ฟังก์ชัน หากไม่ส่งค่าให้พารามิเตอร์ตัวนั้น จะใช้ค่า default ที่กําหนดไว้

def sumN(n1,n2,n3 = 10 ,n4 = 100):
    print(n1 + n2 + n3 + n4)

def CMN(name = 'No-Name'):
    return f'HI Mr.{name}'

print(CMN('Timmt'))  
print(CMN( ))

sumN(10,10,10,10)
sumN(10,10,)