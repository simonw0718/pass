password='1234'
i=3
while i > 0:
	try_pass = input('請輸入密碼(四碼):')
	if try_pass == password:
		print('登入成功')
		i=0
	else:
	    i=i-1
	    print('密碼錯誤,', '剩餘', i, '次' )

