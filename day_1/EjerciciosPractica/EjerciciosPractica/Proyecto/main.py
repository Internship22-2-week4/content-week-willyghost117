import sys
clients = [
    {
        'name' : 'Pablo',
        'company' : 'Google',
        'email'  :  'pablo@google.com',


    },
    {
        'name' : 'Ricardo',
        'company' : 'Facebook',
        'email' : 'ricardo@facebook',
    }
]

def create_client (client):
    global clients
    if client not in clients:
        clients.append(client)
    else: 
        print('Client alredy is in the client s list') 


def list_clients():
    for idx, client in enumerate(clients):
        print('{uid}|{name}|{company}|{email}'.format(uid=id, name=client['name'], company = ['company'], email = ['email'] ))
        #print('{}:{}'.format(idx,client['name']))
    # global clients  
    #print(clients)
 
def _get_client_field(field_name):
    field = None
    while not field:
        field = input ('What is the client {}?'.format(field_name))

    return field 

"""
def _get_name_client():
    client_name = None
    while not client_name:
        client_name= input('What is the client name? ')
        if client_name == 'exit':
            client_name = None
            break
    if not client_name:
            sys.exit()
    return client_name
"""

def update_client(client_id, updated_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        print('Client not in client\'s list')

def _serch_client(field_name, client_data):
   # global clients
    for client in clients:
        if client[client_name] != client_data :
            continue
        else :
            return True

def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client

def delete_client(client_id):
    global clients
    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx] 
            break


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
        client  = {
            'name': _get_client_field('name'),
            'company' : _get_client_field('company'),
            'email' : _get_client_field('email'),
        } 

        create_client(client)
        list_clients()

    elif commando == 'D':
        client_id = _get_name_client()
        delete_client(client_name)
        list_clients()

    elif commando == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()
        update_client(client_id, updated_client)
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
    
