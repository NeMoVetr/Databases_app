from django.db import models


# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    contact_information = models.CharField(max_length=255)
    description = models.TextField()


class Room(models.Model):
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=1)
    availability = models.BooleanField(default=True)
    description = models.TextField()


class Client(models.Model):
    FIO = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    country_of_residence = models.CharField(max_length=100)
    preferences = models.TextField()


class Booking(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_arrival = models.DateField()
    date_departure = models.DateField()
    count_guests = models.IntegerField()
    status = models.CharField(max_length=50)


class HotelEmployee(models.Model):
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    FIO = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=20)


class Review(models.Model):
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=1)
    comment = models.TextField()
    writing_date = models.DateField()


class Event(models.Model):
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField()
    name_event = models.CharField(max_length=255)
    description = models.TextField()
    venue = models.CharField(max_length=255)


class Cancellation(models.Model):
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    date_and_time_references = models.DateTimeField(auto_now_add=True)


class Service(models.Model):
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    availability = models.BooleanField(default=True)


class Payment(models.Model):
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=1)
    date_and_time = models.DateTimeField(auto_now_add=True)
