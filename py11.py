#Function2
# 2. function ที่มี parameter และไม่มี return
# parameter คือ ตัวแปรประเภทหนึ่ง ที่รับข้อมูลมาใช้ได้เฉพาะใน function นั้นๆ เท่านั้น
def CMN (name , age) :
    print('-------------')
    print(f'Hi {name}')
    print(f'your age : {age}')
    print('-------------')

def sumN(n1 , n2) :
    print('------------------------------')
    print(f'{n1} + {n2} = { n1 + n2}')
    print('------------------------------')

CMN('Timmy',20)
sumN(10, 15)