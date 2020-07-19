from django.db import models

class Customer(models.Model):
    customer = models.CharField(max_length = 100)
    item = models.CharField(max_length = 100)
    total = models.IntegerField(default = 0)
    quantity = models.IntegerField()
    date = models.DateTimeField()


    def __str__(self):
        return f"{self.customer} bought {self.item}"
    
     
