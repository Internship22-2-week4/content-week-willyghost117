import random

ciclo = 0

def binary_search(data, target, low, high):
    if low > high:
        return False
    global ciclo
    mid = (low + high) // 2
    #ciclo = ciclo+1
    print('ciclo')
    print(mid)
    if target == data[mid]:
        #print(mid)
        return True

    elif target < data[mid]:
        return binary_search(data,target, low, mid - 1)
    else:
        return binary_search(data, target, mid + 1, high)


if __name__== '__main__':

    data = [random.randint(0,100)for i in range (10)]

    data.sort()

    print(data)
    
    target = int(input('what number would you like to find ?'))
    found = binary_search(data, target, 0, len(data) -1)

    print(found)