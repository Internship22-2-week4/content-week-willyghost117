PASSWORD = '12345'



def password_required(func):
    def wrapper () :
        password = input('What is your password ? ')

        if password == PASSWORD:
            return func()
        else:
            print ('the password is incorrect')
    return wrapper

@password_required
def nees_password():
    print('La consetraseña es correcta')

if __name__ == '__main__':

    nees_password()