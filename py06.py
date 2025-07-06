#input
name = input('ป้อนชื้อ : ')
year_born = input('ปีเกิด :')
salary = float(input('เงินเดือน :'))

print(f'สวัสดีคุณ {name}')
print(f'คุณเกิดปี พ.ศ.{year_born} ตอนนี้คุณอายุ {2568 - int(year_born)} ปี' )
print(f'เงินเดือน{year_born} บาท คิดภาษี 7% เป็นเงิน {(salary) * 7 / 100} บาท' )