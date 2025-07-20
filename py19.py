
class car :
    #data  member
    brand = ""
    model = ""
    whell = 0

    def letgo(self):
        print('letgo')

obA = car()        
obB = car()        
obZ = car()        

#เรียกใช้
obA.brand = 'Honda'
print(obA.brand)
obB.whell = 1
print(obB.whell + obZ.whell)
obZ.letgo()