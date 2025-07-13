#control ep3
#break หยุดทำงานในลูปทันที
#continue ไปไปไปปไปไป

#break
for x in range(1,6) :
    print(f'Timmy {x}')
    if x == 3 :
        break
print(f'END {x}')
print('----------------') 

#continue
for x in range(1,6) :
    print(f'Timmy {x}')
    if x == 3 :
        continue
    print(f'T {x}')
print(f'END {x}')
print('----------------') 
