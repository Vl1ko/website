from django.db import models

class Response(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_female = models.CharField(max_length=200, blank=True, null=True, verbose_name='Фамилия заявителя')
    order_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Имя заявителя')
    order_secname = models.CharField(max_length=200, blank=True, null=True, verbose_name='Отчество заявителя')
    city = models.CharField(max_length=200, blank=True, null=True, verbose_name='Населенный пункт заявителя')
    email = models.CharField(max_length=200, blank=True, null=True, verbose_name='Email заявителя')
    status = models.CharField(max_length=200, blank=True, null=True, verbose_name='Статус заявителя')
    female_r = models.CharField(max_length=200, blank=True, null=True, verbose_name='Фамилия Аниматора')
    name_r = models.CharField(max_length=200, blank=True, null=True, verbose_name='Имя Аниматора')
    secname_r = models.CharField(max_length=200, blank=True, null=True, verbose_name='Отчество Аниматора')
    age_r = models.CharField(max_length=200, blank=True, null=True, verbose_name='Возраст Аниматора')
    prof_r = models.CharField(max_length=200, blank=True, null=True, verbose_name='Профессия/род занятий Аниматора')
    job_r = models.CharField(max_length=200, blank=True, null=True, verbose_name='Место работы/учебы Аниматора')
    vk = models.CharField(max_length=200, blank=True, null=True, verbose_name='Страница VK Аниматора')
    tel_r = models.CharField(max_length=200, blank=True, null=True, verbose_name='Телефон Аниматора')
    email_r = models.CharField(max_length=200, blank=True, null=True, verbose_name='Email Аниматора')
    region_r = models.CharField(max_length=200, blank=True, null=True, verbose_name='Регион Аниматора')
    city_r = models.CharField(max_length=200, blank=True, null=True, verbose_name='Населенный пункт Аниматора')
    residents_r = models.CharField(max_length=200, blank=True, null=True, verbose_name='Количество жителей в Регионе')
    gl1 = models.CharField(max_length=10000, blank=True, null=True, verbose_name='Глава 1')
    gl2 = models.CharField(max_length=10000, blank=True, null=True, verbose_name='Глава 2')
    gl3 = models.CharField(max_length=10000, blank=True, null=True, verbose_name='Глава 3')
    gl4 = models.CharField(max_length=10000, blank=True, null=True, verbose_name='Глава 4')
    gl5 = models.CharField(max_length=10000, blank=True, null=True, verbose_name='Глава 5')
    q1 = models.CharField(max_length=10000, blank=True, null=True, verbose_name='Что делает эту историю уникальной')
    q2 = models.CharField(max_length=10000, blank=True, null=True, verbose_name='Продолжение истории')
    q3 = models.CharField(max_length=10000, blank=True, null=True, verbose_name='Последователи')
    q4 = models.CharField(max_length=10000, blank=True, null=True, verbose_name='Единичный ли случай')
    ph1= models.CharField(max_length=10000, blank=True, null=True, verbose_name='Ссылка на фото героя')
    ph2 = models.CharField(max_length=10000, blank=True, null=True, verbose_name='Ссылка на материалы')
    
    def __str__(self):
        return str(self.order_dt)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'