from django.db import models

class tea(models.Model):
    name = models.CharField(max_length=100)  # Product name (e.g., Black Tea)
    description = models.TextField(blank=True, null=True)  # Optional description
    image = models.ImageField(upload_to='', blank=True, null=True)  # Optional image
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class teavarient(models.Model):
    varienttype = models.ForeignKey(tea, on_delete=models.CASCADE, related_name='variants',default=1)  # Link to Product
    varientname = models.CharField(max_length=255)
    size = models.CharField(max_length=50)  # Size (e.g., 100g, 250g)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price for this size
    stock = models.PositiveIntegerField(default=0)  # Stock quantity

    def __str__(self):
        return f"{self.varienttype.name} - {self.size}"    