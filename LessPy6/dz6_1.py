def cod():
    l = ['п', 'роб', 'ни', 'к', '1']
    s = ''
    print('Список строк: ', l)
    for i in l:
        s += i
    print('Закодированная последовательность:', s.encode('utf-8'))

cod()

def decod():
    c = b'\xd0\xbf\xd1\x80\xd0\xbe\xd0\xb1\xd0\xbd\xd0\xb8\xd0\xba1'.decode('utf-8')
    print('Декодированная последовательность:', c)

decod()
