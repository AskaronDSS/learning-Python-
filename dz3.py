class assessment:
    def __init__(self, name):
        self.name = name
        self.failed = []
        self.passed = []
        self.error_prof = False
    # def values_75(self): # Проставить правильные оценки исходя из описания задачи
    #     for key_d, val_d in self.name.items():
    #         if val_d[0] >= 75 :
    #             print(f'{key_d}, <<Passed>>\tValue:{val_d[0]}')
    #         else:
    #             print(f'{key_d}, <<Failed>>\tValue:{val_d[0]}')
    # def values_73_78(self): #Проставить правильные оценки исходя из задания ко второй группе студентов
    #     for key_d, val_d in self.name.items():
    #         if val_d[0] >= 73 and val_d[0] <= 78:
    #             print(f'{key_d}, <<Passed>>\tValue:{val_d[0]}')
    #         else:
    #             print(f'{key_d}, <<Failed>>\tValue:{val_d[0]}')
    def subsequence(self):
        for key_d, val_d in self.name.items():
            if val_d[1] == 'Passed':
                self.passed.append(val_d)
            else:
                self.failed.append(val_d)
        for fail in self.failed:
            for pas in self.passed:
                if fail[0] > pas[0]:
                    self.error_prof = True
                    break
        return self.failed,self.passed,self.error_prof
    def print_result(self):
        error_prof = self.error_prof
        if error_prof == True:
            max_passed = max(self.passed)
            min_passed = min(self.passed)
            print(f'Профессор допускал ошибки при выставлении результатов теста.\n'
                  f'Потому что минимальная оценка которой поставили "Здал" - {min(self.passed)}\n'
                  f'А максимальная не сдача - {max(self.failed)}\n'
                  f'Порог сдачи от {min_passed[0]} - {max_passed[0]}')
        else:
            print(f'Профессор не допустил ошибок при проверки тестов.')


students = {'Student 1':(78,'Failed'),
            'Student 2':(82,'Passed'),
            'Student 3':(97,'Passed'),
            'Student 4':(86,'Passed'),
            'Student 5':(67,'Passed'),
            'Student 6':(75,'Passed'),
}
student_2 = {
            'Student 1_1':(84,'Passed'),
            'Student 2_2':(78,'Passed'),
            'Student 3_3':(65,'Failed'),
            'Student 4_4':(90,'Passed'),
            'Student 5_5':(72,'Failed'),
}

stud1 = assessment(students)
stud2 = assessment(student_2)

# stud1.values_75()
# stud2.values_73_78()
print('->Первая группа студентов \n')
stud1.subsequence()
stud1.print_result()
print()
print('->Вторая группа студентов \n')
stud2.subsequence()
stud2.print_result()
