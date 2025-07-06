# output statement Ep.02
name = 'chimha'
print("aaaa",1111,25 + 15,True,"wooow",name)
#ใช้ + ขั้น จะไม่เว้นวัค
print("aaaa" +str (1111) +str (25 + 15) +str (True) + "wooow" + name)
#format() **ไม่ใช่string ใส่ใน{}
print('AAA {} {} {} woow {}'.format(1111,25 + 15,True,name))
#f-string
print(f'AAA {1111} {25+15} {True} woow {name}')
