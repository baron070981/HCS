from django.db import models

from .utilits import DateAndTime



class AddressModel(models.Model):
    '''Модель адреса отклченного абонента'''
    city = models.CharField(max_length=200, 
                            default='Сегежа',
                            verbose_name='город')
    street = models.CharField(max_length=200,
                            verbose_name='улица')
    house = models.CharField(max_length=10,
                            verbose_name='номер дома')
    # оставшаяся часть адреса(квартира, комната и тп) если есть
    rest_address = models.CharField(max_length=250, 
                                    verbose_name='остаток адреса', 
                                    blank=True,
                                    default='-')
    
    class Meta:
        verbose_name = 'адрес'
        verbose_name_plural = 'адреса'
    
    
    def __str__(self):
        return f'{self.city}, {self.street}, {self.house}, {self.rest_address}'


class DisabledAdressesModel(models.Model):
    '''Модель адресов отключенных за неуплату или по другой причине'''
    # дата и время отключения электричества
    blackout_datetime = models.CharField(max_length=20,
                                         default=DateAndTime.set_default_datetime(),
                                         verbose_name='дата и время отключения')
    # адрес
    city = models.CharField(max_length=200, 
                            default='Сегежа',
                            verbose_name='город')
    street = models.CharField(max_length=200,
                            verbose_name='улица')
    house = models.CharField(max_length=10,
                            verbose_name='номер дома')
    # оставшаяся часть адреса(квартира, комната и тп) если есть
    rest_address = models.CharField(max_length=250, 
                                    verbose_name='остаток адреса', 
                                    blank=True,
                                    default='-')
    # марка счетчика
    meter_brand = models.CharField(max_length=100,
                                   blank=True,
                                   default='-',
                                   verbose_name='марка счетчика')
    # номер счетчика
    number_meter = models.CharField(max_length=30,
                                    blank=True,
                                    default='-',
                                    verbose_name='номер счетчика')
    # номер пломбы
    number_seal = models.CharField(max_length=20,
                                   verbose_name='номер пломбы')
    # показания
    reading = models.CharField(max_length=100,
                               verbose_name='показания счетчика')
    # причина отключения
    reason = models.TextField(max_length=200,
                              blank=True,
                              default='-',
                              verbose_name='причина отключения')
    # способ отключения
    shutdown_method = models.TextField(max_length=250,
                                       blank=True,
                                       default='отключение отходящего фазного провода от счетчика',
                                       verbose_name='способ отключения')
    
    
    class Meta:
        verbose_name = 'отключенный абонент'
        verbose_name_plural = 'отключенные абоненты'
    
    
    def __str__(self):
        s = f'{self.blackout_datetime} : {self.meter_brand}; '
        s2 = f'{self.number_meter}; {self.reading}; {self.number_seal}'
        return s+s2











