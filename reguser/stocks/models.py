from django.db import models

class Stock(models.Model):
    stock_symbol = models.CharField(max_length=200, primary_key=True)
    date = models.DateField()
    timezone = models.CharField(max_length=200)
    predicted_price = models.FloatField()
    currency = models.CharField(max_length=200)
    
    class Meta:
        db_table = "stock_data"
        
    def __str__(self):
        return self.stock_symbol

    
