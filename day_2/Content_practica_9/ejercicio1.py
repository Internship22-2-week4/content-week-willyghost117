password = '2Fj(jjbFsuj'
password2 = 'eoZiugBf&g9'

def contraseniaValida (user_password) :
    global password
    global password2

    if user_password == password or user_password == password2 :
        #print(user_password)
        return True 
    else:
        return False

print(contraseniaValida('2Fj(jjbFsuj'))
print(contraseniaValida('eoZiugBf&g9'))
print(contraseniaValida('hola'))
print(contraseniaValida(''))