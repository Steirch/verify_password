passwords = input('请输入密码：')

#将每个列表以逗号分隔,并以列表形式储存 
password_list = passwords.split(',')
print(password_list)    #以列表形式返回密码组 


#检测六个要求是否都满足
little,captial,num,spe=0,0,0,0
for i in range(len(password_list)):
    if len(password_list[i])<6 or len(password_list[i])>12:  #判断密码长度的两个条件
        continue    #若密码长度不对直接跳出循环
        
    s = str(password_list[i])  #将每个密码转换为字符串形式进行判断 
    for a in s:
        if a>='a' and a<='z':
            little += 1
        if a>='A' and a<='Z':
            captial += 1
        if '0'<=a<='9':
            num += 1
        if a=='@' or a=='#' or a=='$' or a=='*':
            spe+=1
    if little>0 and captial>0 and num>0 and spe>0:
        print(password_list[i]) 
    little,captial,num,spe=0,0,0,0    
        
        