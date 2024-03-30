from django.db import models
#-------------for car details---------#
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=[('Available', 'Available'), ('Rented', 'Rented')])
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)
    Rent_per_day=models.IntegerField(default='20000')  

    def __str__(self):
        return f"{self.make} {self.model} - {self.license_plate}"
    
#-------------for signin-----------#
class usermanage(models.Model):
    name=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    Adress=models.TextField()
    phonenumber=models.CharField(max_length=100)
    licensenumber=models.CharField(max_length=100)
    Age=models.IntegerField()

# ----------for location pickup and dropoff------#
class location(models.Model):
    pickuplocation=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.pickuplocation
      
class location2(models.Model):
    Dropoflocation=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.Dropoflocation    
    
# ---------for booking--------#
class Booking(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
    ]
    Name = models.CharField(max_length=50)
    model = models.ForeignKey(Car, on_delete=models.CASCADE)
    Rental_start_date = models.DateField()
    Rental_end_date = models.DateField()
    pickuplocation = models.ForeignKey(location, on_delete=models.CASCADE,related_name='pickup_bookings')
    Dropoflocation = models.ForeignKey(location2, on_delete=models.CASCADE,related_name='dropoff_bookings')
    Rental_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"{self.Name} - {self.Rental_status}"

