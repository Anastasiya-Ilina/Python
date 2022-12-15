def password():
    p = input("Введите пароль: ")
    if len(p) < 6:
        print('Пароль меньше 6 знаков')
        return False
    elif "".join(p).lower() == 'password':
        print('Слишком простой пароль')
        return False
    elif not any(p1.isdigit() for p1 in p):
        print('Пароль должен содержать цифру')
        return False
    elif all(p2.isdigit() for p2 in p):
        print('Пароль не должен состоять только из цифр')
        return False
    else:
        print('Ваш пароль принят')
        return True

password()
