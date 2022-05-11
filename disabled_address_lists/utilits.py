import datetime


class DateAndTime:
    
    @classmethod
    def set_default_date(cls):
        '''Получение текущей даты и возврат строки с датой
        в фомате дд.мм.гггг'''
        offset = datetime.timedelta(hours=3)
        tz = datetime.timezone(offset, name='МСК')
        date = datetime.datetime.now(tz=tz).timetuple()[:3]
        year, month, day = list(map(DateAndTime().__add_zero, date))
        return f'{day}.{month}.{year}'
    
    
    @classmethod
    def set_default_datetime(cls):
        '''Получение текущей даты и возврат строки с датой и временем
        в формате дд.мм.гггг-чч.мм'''
        offset = datetime.timedelta(hours=3)
        tz = datetime.timezone(offset, name='МСК')
        dt = datetime.datetime.now(tz=tz).timetuple()[:5]
        year, month, day, hour, minute = list(map(DateAndTime().__add_zero, dt))
        return f'{day}.{month}.{year}-{hour}.{minute}'

    
    def __add_zero(self, number):
        '''добавляет ноль перед числом если оно меньше 10
        например из 2 получается 02'''
        number = str(number)
        if len(number) == 1:
            return f'0{number}'
        return number












if __name__ == '__main__':
    print(DateAndTime.set_default_datetime())


