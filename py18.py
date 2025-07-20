listData1 = [10, 20 ,30, 40, 10 ] #มี5ข้อมูล
tupData1 = (10, 20 ,30, 40, 10 ) #5ข้อมูล
settData1 = {10, 20 ,30, 40, 10 } #4ข้อมูล
dictData1 ={
    'name' : 'Timmy',
    'age' : '20',
    'is_studen' : True,
    'score' : [82,81],
    10017 : 'JJ'
}
print(dictData1['name'])
print(dictData1[10017])
print(dictData1['score'][1])
dictData1[10017] = 'jimmy'
print(dictData1[10017])