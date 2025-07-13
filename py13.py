#Function4
# 4. function ที่มี parameter และมี return
# parameter คือ ตัวแปรประเภทหนึ่ง ที่รับข้อมูลมาใช้ได้เฉพาะใน function นั้นๆ เท่านั้น

def calsquareArea(width,height):
    area = width * height
    return area

def calTraingleArea(base,hight):
    return base * hight / 2


print(f'SquareArea width 10 height 20 : {calsquareArea(10,20)}')
print('------------------------------------------------------------')
print(f'TraingleArea base 5 hight 100 : {calTraingleArea(5,100)}')
print('------------------------------------------------------------')
