password = 'a123456'
e = 3
while True: 
    ps = input('輸入密碼:')
    if ps == password:
        print('登入成功')
        break
    else:
        e = e - 1
        print('密碼錯誤 還有', e,  '次機會')
        if e == 0:
            break