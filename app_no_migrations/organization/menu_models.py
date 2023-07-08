from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название', default='')
    sort = models.IntegerField(verbose_name='Сортировка', default='', blank=True)
    url = models.CharField(max_length=255, verbose_name='URL', default='', blank=True)

    def __str__(self):
        return self.name

    def get_menu_data(self):
        return dict(
            id=self.id,
            name=self.name,
            sort=self.sort,
            url=self.url
        )


    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'