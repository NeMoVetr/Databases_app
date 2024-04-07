from django import forms

from .models import Hotel, Room, HotelEmployee, Booking, \
    Review, Event, Client, Cancellation, Payment, Service


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'


class HotelEmployeeForm(forms.ModelForm):
    class Meta:
        model = HotelEmployee
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class CancellationForm(forms.ModelForm):
    class Meta:
        model = Cancellation
        fields = '__all__'


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


