class Human:
    ''' Класс, который включает общие признаки человека'''

    def __init__(self, name, age, company):
        '''

        :param name: имя
        :param age: возраст
        :param company: место работы
        '''
        self.name = name
        self.age = age
        self.company = company


class Student(Human):
    ''' Класс, который включает общие признаки студента'''

    def __init__(self, name, age, company, education, number_of_works_done):
        '''
        
        :param name: имя
        :param age: возраст
        :param company: место работы
        :param education: образование
        :param number_of_works_done: число выполненных заданий
        '''
        super().__init__(name, age, company)
        self.education = education
        self.number_of_works_done = number_of_works_done

Anna = Student('Anna', 20, 'YarGu', 'mathematical', 5)
Artem = Student('Artem', 30, 'Rostelecom', 'physical', 7)
print('У Анны выполнено ', Anna.number_of_works_done, 'заданий')
print('У Артема выполнено ', Artem.number_of_works_done, 'заданий')

if Anna.__eq__(Artem):
    print('Артем выполнила больше заданий')
else:
    print('Анна выполнил больше заданий')
    
