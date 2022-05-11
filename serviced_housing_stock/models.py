from django.db import models



class ServiceAddressModel(models.Model):
    ''''''
    city = models.CharField(max_length=200, 
                            default='Сегежа',
                            verbose_name='город')
    street = models.CharField(max_length=200,
                            verbose_name='улица')
    house = models.CharField(max_length=10,
                            verbose_name='номер дома')
    # примичание к адресу
    note = models.CharField(max_length=250, 
                                    verbose_name='примечание', 
                                    blank=True,
                                    default='-')
    
    class Meta:
        verbose_name = 'обслуживаемый адрес'
        verbose_name_plural = 'обслуживаемые адреса'



    def __str__(self):
        return f'ул.{self.street} д.{self.house}'






