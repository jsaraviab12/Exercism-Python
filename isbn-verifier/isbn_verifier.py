def is_valid(isbn):
    isbn = (isbn.replace('-',''))

    if len(isbn) != 10:
        return  False
    
    aux = 0

    for (i, num) in enumerate(isbn):
        if num.isnumeric():
            aux += int(num) * (10 - i)
        elif i == 9 and num is 'X':
            aux += 10
        else:
            return False

    return aux % 11 == 0
