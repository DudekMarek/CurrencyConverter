
class Currency():
    dolar_course: float

    def __init__(self, dolar_course: float, name: str):
        self.name = name
        self.dolar_course = dolar_course

    def return_dict(self):
        return {self.name:self.dolar_course}
    
    def convert_to_dollar(self, quantity: float):
        return round(quantity * self.dolar_course, 2)
    
    def convert_to_another_currency(self, another_currency: 'Currency', quantity: float):
        dollar_equvivalent = self.convert_to_dollar(quantity=quantity)

        return round(dollar_equvivalent / another_currency.dolar_course, 2)
