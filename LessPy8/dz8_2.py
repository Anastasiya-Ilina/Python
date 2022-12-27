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
        
