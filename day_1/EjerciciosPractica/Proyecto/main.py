clients = 'pablo,ricardo,'

def create_client (client_name):
    global clients
    if client_name not in clients:
        clients += client_name
        _add_comma()
    else: 
        print('Client alredy is in the client s list') 


def list_clients():
    global clients  
    print(clients)


def _add_comma():
    global clients
    clients +=','  

def _get_name_client():
    return input('What is the client name? ')

def update_client(client_name, updated_client_name):
    global clients
    if client_name in clients:
       clients = clients.replace(client_name+',',updated_client_name+',')
    else:
        print('Client is not in clients list')

def _serch_client(client_name):
   # global clients
    clients_list = clients.split(',')
    print(clients_list)
    for client in clients_list:
        if client != client_name:
            continue
        else :
            return True

def delete_client(client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name+',','')
    else: 
        print('Client is not in clients list')


def _print_welcome():
    print('Welcome to platzi ventas')
    print('#'*20)
    print('Whath would you like todo today?  ')

    print('[C]reate client')
    print('[R]read clients')
    print('[U]pdate')
    print('[D]elete client')
    print('[S]erch')


if __name__ == '__main__':
    _print_welcome()

    commando = input()
    commando = commando.upper()

    if commando == 'C':
        client_name = _get_name_client()
        create_client(client_name)
        list_clients()

    elif commando == 'D':
        client_name = _get_name_client()
        delete_client(client_name)
        list_clients()

    elif commando == 'U':
        client_name = _get_name_client()
        updated_client_name = input('What is the updated client name')
        update_client(client_name, updated_client_name)
        list_clients()

    elif commando == 'S':
        client_name = _get_name_client()
        found = _serch_client(client_name)
        if found:
            print('The client is in the client s list')
        else:
            print('The client {} es not in the client s list'.format(client_name))

    elif commando == 'R':
        list_clients()

    else:
        print('INVALID COMMAND')
    
