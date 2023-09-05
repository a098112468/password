password = 'a123456'
e = 3
while e > 0: 
    ps = input('輸入密碼:')
    if ps == password:
        print('登入成功')
        break
    else:
        e = e - 1
        print('密碼錯誤')
        if e > 0:
            print('還有', e, '次機會')
