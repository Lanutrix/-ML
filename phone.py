from datetime import datetime, date


class Phone:
    def __init__(self, model: str = "Mi A2", year: date = date(2018, 7, 24)) -> None:
        self.__model = model
        self.__year = year

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @model.setter
    def model(self, value):
        if isinstance(value, str):
            self.__model = value
        else:
            raise TypeError('Это не строка')

    @year.setter
    def year(self, value):
        if isinstance(value, date):
            self.__year = value
        else:
            raise TypeError('Это не дата')


ph = Phone()
print(ph.model)
print(ph.year)
print()

ph.model = "LolИ"
ph.year = date(2009, 1, 1)
print(ph.model)
print(ph.year)
print()


class IPhone(Phone):
    def __init__(self, model: str = "IPhone 13", year: date = date(2021, 9, 14)) -> None:
        super().__init__(model, year)
        self.__os = "IOS 13"

    @property
    def os(self):
        return self.__os

    @os.setter
    def os(self, value):
        if isinstance(value, str):
            if value.split()[-1].isdigit():
                nos = int(value.split()[-1])
                if int(self.__os.split()[-1]) < nos:
                    self.__os = value
                    print("Обновление прошло успешно")
                elif int(self.__os.split()[-1]) == nos:
                    raise TypeError('Это текущая версия ОС')
                else:
                    raise TypeError('Это старая версия ОС')
            else:
                raise TypeError('Это неправильная запись версии ОС')
        else:
            raise TypeError('Это не строка')


iph = IPhone()

print(iph.model)
print(iph.year)
print(iph.os)
print()

iph.model = "IPhone 15"
iph.year = date(2023, 9, 12)
iph.os = "IOS 15"

print(iph.model)
print(iph.year)
print(iph.os)

iph.os = "IOS 15"
iph.os = "IOS 14"
iph.os = "IOS"
