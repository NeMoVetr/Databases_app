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

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)

        self.fields['hotel_id'].queryset = self.fields['hotel_id'].queryset.values_list('id', flat=True)


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)

        self.fields['client_id'].queryset = self.fields['client_id'].queryset.values_list('id', flat=True)
        self.fields['room_id'].queryset = self.fields['room_id'].queryset.values_list('id', flat=True)


class HotelEmployeeForm(forms.ModelForm):
    class Meta:
        model = HotelEmployee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(HotelEmployeeForm, self).__init__(*args, **kwargs)

        self.fields['hotel_id'].queryset = self.fields['hotel_id'].queryset.values_list('id', flat=True)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        self.fields['hotel_id'].queryset = self.fields['hotel_id'].queryset.values_list('id', flat=True)
        self.fields['client_id'].queryset = self.fields['client_id'].queryset.values_list('id', flat=True)


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)

        self.fields['booking_id'].queryset = self.fields['booking_id'].queryset.values_list('id', flat=True)


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

        self.fields['hotel_id'].queryset = self.fields['hotel_id'].queryset.values_list('id', flat=True)


class CancellationForm(forms.ModelForm):
    class Meta:
        model = Cancellation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CancellationForm, self).__init__(*args, **kwargs)

        self.fields['booking_id'].queryset = self.fields['booking_id'].queryset.values_list('id', flat=True)


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)

        self.fields['hotel_id'].queryset = self.fields['hotel_id'].queryset.values_list('id', flat=True)
