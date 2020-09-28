from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Survey(models.Model):
    STATUS = [
        ('Creature of Comfort','Creature of Comfort'),
        ('Protector of Habit','Protector of Habit'),
        ('Navigator of Discomfort','Navigator of Discomfort'),
        ('Pioneer of Curiosity','Pioneer of Curiosity'),
        ('Challenger of Norms','Challenger of Norms'),
        ('Bastion of Cohesion','Bastion of Cohesion'),
    ]
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    score = models.IntegerField()
    archive = models.CharField(max_length=200,null=True,choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}_{}'.format(self.customer.name,self.id)