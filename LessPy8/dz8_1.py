class Animals:
    ''' Класс, который включает
    общие признаки и поведения животных'''

    def __init__(self, size, type, habitat, number_of_paws):
        '''
        :param size: размер
        :param type: тип (хордовые, моллюски и т.д)
        :param habitat: среда обитания
        :param number_of_paws: количестко конечностей
        '''
        self.size = size
        self.type = type
        self.habitat = habitat
        self.number_of_paws = number_of_paws

class Mammals(Animals):
    ''' Класс, который включает
    общие признаки и поведения млекопитающих'''

    def __init__(self, size, type, habitat, number_of_paws, subclass, infraclasses, type_of_limbs):
        '''

        :param size: размер
        :param type: тип
        :param habitat: среда обитания
        :param number_of_paws: количество конечностей
        :param subclass: отряд (хищники, парнокопытные и т.д)
        :param infraclasses: семейства (кошачье, заячье и т.д)
        :param type_of_limbs: тип конечностей (лапы, копыта и т.д)
        '''
        super().__init__(size, type, habitat, number_of_paws)
        self.subclass = subclass
        self.infraclasses = infraclasses
        self.type_of_limbs = type_of_limbs

class Human(Mammals):
    ''' Класс, который включает
    общие признаки и поведения человека'''

    def __init__(self, size, type, habitat, number_of_paws, subclass, infraclasses, type_of_limbs, name, age, abode):
        '''

        :param size: размер
        :param type: тип
        :param habitat: среда обитания
        :param number_of_paws: количество конечностей
        :param subclass: отряд (хищники, парнокопытные и т.д)
        :param infraclasses: семейства (кошачье, заячье и т.д)
        :param type_of_limbs: тип конечностей (лапы, копыта и т.д)
        :param name: имя
        :param age: возраст
        :param abode: место жительства
        '''
        super().__init__(size, type, habitat, number_of_paws, subclass, infraclasses, type_of_limbs)
        self.name = name
        self.age = age
        self.abode = abode

class Cat(Mammals):
    ''' Класс, который включает
    общие признаки и поведения кошки'''

    def __init__(self, size, type, habitat, number_of_paws, subclass, infraclasses, type_of_limbs, color, name):
        '''

        :param size: размер
        :param type: тип
        :param habitat: среда обитания
        :param number_of_paws: количество конечностей
        :param subclass: отряд (хищники, парнокопытные и т.д)
        :param infraclasses: семейства (кошачье, заячье и т.д)
        :param type_of_limbs: тип конечностей (лапы, копыта и т.д)
        :param color: окрас
        :param name: кличка
        '''
        super().__init__(size, type, habitat, number_of_paws, subclass, infraclasses, type_of_limbs)
        self.color = color
        self.name = name

class Dog(Mammals):
    ''' Класс, который включает
    общие признаки и поведения собаки'''

    def __init__(self, size, type, habitat, number_of_paws, subclass, infraclasses, type_of_limbs, name, wool_length):
        '''

        :param size: размер
        :param type: тип
        :param habitat: среда обитания
        :param number_of_paws: количество конечностей
        :param subclass: отряд (хищники, парнокопытные и т.д)
        :param infraclasses: семейства (кошачье, заячье и т.д)
        :param type_of_limbs: тип конечностей (лапы, копыта и т.д)
        :param name: кличка
        :param wool_length: длинна шерсти
        '''
        super().__init__(size, type, habitat, number_of_paws, subclass, infraclasses, type_of_limbs)
        self.name = name
        self.wool_length = wool_length
        
