import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items
    
    @property
    def number_items(self):
        return self.__number_items
    
    def add_item_to_cheque(self, name):
        if (name == 0) or (len(name) > 40):
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.name_items.append(name)
            self.__number_items += 1
    
    def delete_item_from_check(self, name):
        if name not in self.name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.name_items.remove(name)
            self.number_items -= 1

    def check_amount(self):
        total = []
        for name in self.name_items:
            for key, value in self.__item_price.items():
                if name == key:
                    total.append(value)
        total_sum = 0
        for i in total:
            total_sum += i
        if len(total) > 10 :
            return total_sum * 0.9
        else:
            return total_sum
    
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for name in self.name_items:
            for key, value in self.__tax_rate.items():
                if name == key:
                    if value == 20:
                        twenty_percent_tax.append(name)
                        total.append(self.__item_price[name])
        if len(total) > 10:
            return sum(total)*0.9*0.2
        else:
            return sum(total)*0.2
    
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for name in self.name_items:
            for key, value in self.__tax_rate.items():
                if name == key:
                    if value == 10:
                        ten_percent_tax.append(name)
                        total.append(self.__item_price[name])
        if len(total) > 10:
            return sum(total)*0.9*0.1
        else:
            return sum(total)*0.1
    
    def total_tax(self):
        total_nds = self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()
        print(total_nds)
        return total_nds
    
    @staticmethod
    def get_telephone_number(telephone_number):
        if type(telephone_number) is not int:
            raise ValueError('Необходимо ввести цифры')
        elif len(str(telephone_number)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        else:
            return f'+7{telephone_number}'

    @staticmethod    
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()
        date = (
            ['часы', ((lambda x: x.hour))], 
            ['минуты', ((lambda x: x.minute))], 
            ['день', ((lambda x: x.day))], 
            ['месяц', ((lambda x: x.month))], 
            ['год', ((lambda x: x.year))]
            )
        for element in date:
            name = element[0]
            value = element[1]
            date_and_time.append(f'{name}: {value(now)}')
        return date_and_time


