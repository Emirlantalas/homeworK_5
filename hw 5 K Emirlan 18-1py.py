# написать валидацию на Номера Транспартов
# будет класс ValidCarNumber —> будет метод is_valid(self, number)
# который принимает 1 аргумент number и проверяет на валидность то есть:
# Input:
#
#     01KG777BAD
#     hhh777hhh
#
# Output:
#
#     Номер валидный!
#     Номер не валидный!
import re
class ValidCarnumber:
    def __init__(self,number):
        self.number = number

    def is_valid(self):
        self.is_valid = re.search(r"([0-9]{2})([A-Z]{2})([0-9]{3})([A-Z]{3})", self.number)
        if self.is_valid:
            print("car number  valid!")
        else:
            print("car number invalid")

valid = ValidCarnumber(input("tranposrt number: "))
valid.is_valid()