from django.db import models


class Booking(models.Model):
  Name = models.CharField(max_length=255)
  No_of_guests = models.SmallIntegerField()
  BookingDate = models.DateTimeField()

  class Meta:
    unique_together = ('Name', 'BookingDate')

  def __str__(self):
    return f'{self.Name} - {self.No_of_guests} guest(s)'


class Menu(models.Model):
  Title = models.CharField(max_length=255, unique=True)
  Price = models.DecimalField(max_digits=10, decimal_places=2)
  Inventory = models.SmallIntegerField()

  def __str__(self):
    return f'{self.Title} : {str(self.Price)}'
