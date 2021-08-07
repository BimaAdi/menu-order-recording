from django.db import models

class Order(models.Model):

    table_number = models.CharField(max_length=50)
    order_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order'

    def __str__(self):
        return f'{self.table_number} {self.order_date}'

class OrderMenu(models.Model):

    menu_name = models.CharField(max_length=50)
    price = models.IntegerField()
    qty = models.IntegerField()
    order = models.ForeignKey('Order', related_name='order_menus', on_delete=models.CASCADE)

    class Meta:
        db_table = 'order_menu'
        