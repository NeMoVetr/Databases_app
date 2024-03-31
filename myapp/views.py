from datetime import datetime

import pandas as pd
from django.shortcuts import render

from .forms import HotelForm, RoomForm, HotelEmployeeForm, BookingForm, \
    ClientForm, ReviewForm, PaymentForm, ServiceForm, EventForm, CancellationForm
from .models import Hotel, Room, HotelEmployee, Booking, \
    Client, Review, Payment, Service, Event, Cancellation


# Create your views here.

def hotel_show(request):
    hotel_set = Hotel.objects.all()

    data = {
        'Название': [hotel.name for hotel in hotel_set],
        'Адрес': [hotel.address for hotel in hotel_set],
        'Рейтинг': [hotel.rating for hotel in hotel_set],
        'Контактная информация': [hotel.contact_information for hotel in hotel_set],
        'Описание': [hotel.description for hotel in hotel_set]
    }

    html_table = pd.DataFrame(data).to_html()
    context = {
        'html_table': html_table,
    }

    return render(request, 'all_hotel.html', context)


def rooms_show(request):
    """Показать список всех номеров"""
    room_set = Room.objects.all()
    data = {
        'Название отеля': [room.hotel_id.name for room in room_set],
        'Тип': [room.type for room in room_set],
        'Цена': [room.price for room in room_set],
        'Доступность': [room.availability for room in room_set],
        'Описание': [room.description for room in room_set],
    }
    html_table = pd.DataFrame(data).to_html()
    context = {'html_table': html_table}
    return render(request, 'all_rooms.html', context)


def clients_show(request):
    """Показать список всех клиентов"""
    client_set = Client.objects.all()

    data = {
        'ФИО': [client.FIO for client in client_set],
        'Email': [client.email for client in client_set],
        'Номер телефона': [client.phone_number for client in client_set],
        'Страна проживания': [client.country_of_residence for client in client_set],
        'Предпочтения': [client.preferences for client in client_set],
    }

    html_table = pd.DataFrame(data).to_html()
    context = {'html_table': html_table}
    return render(request, 'all_clients.html', context)


def bookings_show(request):
    """Показать список всех бронирований"""
    booking_set = Booking.objects.all()

    data = {
        'ФИО клиента': [booking.client_id.name for booking in booking_set],
        'Тип номера': [booking.room_id.type for booking in booking_set],
        'Дата заезда': [booking.date_arrival for booking in booking_set],
        'Дата выезда': [booking.date_departure for booking in booking_set],
        'Количество гостей': [booking.count_guests for booking in booking_set],
        'Статус': [booking.status for booking in booking_set],
    }

    html_table = pd.DataFrame(data).to_html()
    context = {'html_table': html_table}
    return render(request, 'all_bookings.html', context)


def hotel_employee_show(request):
    """Показать список всех сотрудников"""
    hotel_employee_set = HotelEmployee.objects.all()

    data = {
        'Название отеля': [hotelEmployee.hotel_id.name for hotelEmployee in hotel_employee_set],
        'ФИО клиента': [hotelEmployee.FIO for hotelEmployee in hotel_employee_set],
        'Должность': [hotelEmployee.post for hotelEmployee in hotel_employee_set],
        'Контактная информация': [hotelEmployee.contact_information for hotelEmployee in hotel_employee_set],
    }

    html_table = pd.DataFrame(data).to_html()
    context = {'html_table': html_table}
    return render(request, 'all_hotel_employee.html', context)


def review_show(request):
    """Показать список всех отзывы"""
    review_set = Review.objects.all()

    data = {
        'Название отеля': [review.hotel_id.name for review in review_set],
        'ФИО клиента': [review.client_id.FIO for review in review_set],
        'Оценка': [review.amount for review in review_set],
        'Комментарий': [review.comment for review in review_set],
        'Дата написания': [review.writing_date for review in review_set],
    }

    html_table = pd.DataFrame(data).to_html()
    context = {'html_table': html_table}
    return render(request, 'all_review.html', context)


def payment_show(request):
    """Показать список все платежи"""
    payment_set = Payment.objects.all()

    data = {
        'booking_id': [payment.booking_id for payment in payment_set],
        'ФИО клиента': [payment.client_id.FIO for payment in payment_set],
        'Оценка': [payment.amount for payment in payment_set],
        'Дата и время': [payment.date_and_time for payment in payment_set],
    }

    html_table = pd.DataFrame(data).to_html()
    context = {'html_table': html_table}
    return render(request, 'all_payment.html', context)


def service_show(request):
    """Показать список всех услуг"""
    service_set = Service.objects.all()

    data = {
        'Название отеля': [service.hotel_id.name for service in service_set],
        'Название': [service.name for service in service_set],
        'Описание': [service.description for service in service_set],
        'Цена': [service.price for service in service_set],
        'Доступность': [service.availability for service in service_set],

    }

    html_table = pd.DataFrame(data).to_html()
    context = {'html_table': html_table}
    return render(request, 'all_service.html', context)


def event_show(request):
    """Показать список всех мероприятий"""
    event_set = Event.objects.all()

    data = {
        'Название отеля': [event.hotel_id.name for event in event_set],
        'Дата и время': [event.date_and_time for event in event_set],
        'Название мероприятия': [event.name_event for event in event_set],
        'Описание': [event.description for event in event_set],
        'Место проведения': [event.venue for event in event_set],

    }

    html_table = pd.DataFrame(data).to_html()
    context = {'html_table': html_table}
    return render(request, 'all_event.html', context)


def cancellation_show(request):
    """Показать список всех отмен броней"""
    cancellation_set = Cancellation.objects.all()

    data = {
        'booking_id': [cancellation.booking_id for cancellation in cancellation_set],
        'Дата и время отмены': [cancellation.date_and_time_references for cancellation in cancellation_set],
    }

    html_table = pd.DataFrame(data).to_html()
    context = {'html_table': html_table}
    return render(request, 'all_cancellation.html', context)


def hotel_add(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            rating = form.cleaned_data['rating']
            contact_information = form.cleaned_data['contact_information']
            description = form.cleaned_data['description']
            hotel = Hotel(name=name, address=address, rating=rating, contact_information=contact_information,
                          description=description)

            hotel.save()
            message = 'Отель сохранен'
        else:
            message = 'Заполните форму'
    else:
        form = HotelForm()
        message = 'Заполните форму'
    return render(request, 'hotel_form.html', {'form': form, 'message': message})


def room_add(request):
    """Добавить новый номер"""
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            hotel_id = form.cleaned_data['hotel_id']
            type_room = form.cleaned_data['type']
            price = form.cleaned_data['price']
            availability = form.cleaned_data['availability']
            description = form.cleaned_data['description']
            room = Room(hotel_id=hotel_id, type=type_room, price=price, availability=availability,
                        description=description)
            room.save()
            message = 'Номер сохранен'
        else:
            message = 'Заполните форму'
    else:
        form = RoomForm()
        message = 'Заполните форму'
    return render(request, 'room_add.html', {'form': form, 'message': message})


def client_add(request):
    """Добавить нового клиента"""
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            FIO = form.cleaned_data['FIO']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            country_of_residence = form.cleaned_data['country_of_residence']
            preferences = form.cleaned_data['preferences']
            client = Client(FIO=FIO, email=email, phone_number=phone_number, country_of_residence=country_of_residence,
                            preferences=preferences)
            client.save()
            message = 'Клиент сохранен'
        else:
            message = 'Заполните форму'
    else:
        form = ClientForm()
        message = 'Заполните форму'
    return render(request, 'client_add.html', {'form': form, 'message': message})


def booking_add(request):
    """Добавить новое бронирование"""
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            client_id = form.cleaned_data['client_id']
            room_id = form.cleaned_data['room_id']
            date_arrival = form.cleaned_data['date_arrival']
            date_departure = form.cleaned_data['date_departure']
            count_guests = form.cleaned_data['count_guests']
            status = form.cleaned_data['status']
            booking = Booking(client_id=client_id, room_id=room_id, date_arrival=date_arrival,
                              date_departure=date_departure, count_guests=count_guests, status=status)
            booking.save()
            message = 'Бронь сохранена'
        else:
            message = 'Заполните форму'
    else:
        form = BookingForm()
        message = 'Заполните форму'
    return render(request, 'booking_add.html', {'form': form, 'message': message})


def hotel_employee_add(request):
    """Добавить нового сотрудника"""
    if request.method == 'POST':
        form = HotelEmployeeForm(request.POST)
        if form.is_valid():
            hotel_id = form.cleaned_data['client_id']
            FIO = form.cleaned_data['room_id']
            post = form.cleaned_data['date_arrival']
            contact_information = form.cleaned_data['date_departure']

            hotel_employee = HotelEmployee(hotel_id=hotel_id, FIO=FIO, post=post,
                                           contact_information=contact_information)
            hotel_employee.save()
            message = 'Сотрудник сохранена'
        else:
            message = 'Заполните форму'
    else:
        form = HotelEmployeeForm()
        message = 'Заполните форму'
    return render(request, 'hotel_employee_add.html', {'form': form, 'message': message})


def review_add(request):
    """Добавить новый отзыв"""
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            hotel_id = form.cleaned_data['hotel_id']
            client_id = form.cleaned_data['client_id']
            amount = form.cleaned_data['amount']
            comment = form.cleaned_data['comment']
            writing_date = form.cleaned_data['writing_date']

            review = Review(hotel_id=hotel_id, client_id=client_id, amount=amount, comment=comment,
                            writing_date=writing_date)
            review.save()
            message = 'Отзыв сохранен'
        else:
            message = 'Заполните форму'
    else:
        form = ReviewForm()
        message = 'Заполните форму'
    return render(request, 'review_add.html', {'form': form, 'message': message})


def event_add(request):
    """Добавить новое мероприятие"""
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            client_id = form.cleaned_data['client_id']
            date_and_time = form.cleaned_data['date_and_time']
            name_event = form.cleaned_data['name_event']
            description = form.cleaned_data['description']
            venue = form.cleaned_data['venue']
            event = Event(client_id=client_id, date_and_time=date_and_time, name_event=name_event,
                          description=description, venue=venue)
            event.save()
            message = 'Мероприятие сохранено'
        else:
            message = 'Заполните форму'
    else:
        form = EventForm()
        message = 'Заполните форму'
    return render(request, 'event_add.html', {'form': form, 'message': message})


def cancellation_add(request):
    """Добавить новую отмену бронирования"""
    if request.method == 'POST':
        form = CancellationForm(request.POST)
        if form.is_valid():
            booking_id = form.cleaned_data['booking_id']
            date_and_time_references = form.cleaned_data['date_and_time_references']
            cancellation = Cancellation(booking_id=booking_id, date_and_time_references=date_and_time_references)
            cancellation.save()
            message = 'Отмена брони сохранена'
        else:
            message = 'Заполните форму'
    else:
        form = CancellationForm()
        message = 'Заполните форму'
    return render(request, 'cancellation_add.html', {'form': form, 'message': message})


def service_add(request):
    """Добавить новую услугу"""
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            hotel_id = form.cleaned_data['hotel_id']
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            availability = form.cleaned_data['availability']
            service = Service(hotel_id=hotel_id, name=name, description=description, price=price,
                              availability=availability)
            service.save()
            message = 'Услуга сохранена'
        else:
            message = 'Заполните форму'
    else:
        form = ServiceForm()
        message = 'Заполните форму'
    return render(request, 'service_add.html', {'form': form, 'message': message})


def payment_add(request):
    """Добавить новый платёж"""
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            booking_id = form.cleaned_data['booking_id']
            amount = form.cleaned_data['amount']
            date_and_time = form.cleaned_data['date_and_time']

            payment = Payment(booking_id=booking_id, amount=amount, date_and_time=date_and_time)
            payment.save()
            message = 'Платёж сохранен'
        else:
            message = 'Заполните форму'
    else:
        form = PaymentForm()
        message = 'Заполните форму'
    return render(request, 'payment_add.html', {'form': form, 'message': message})


def available_rooms(request):
    """Доступные номера на заданные даты"""
    hotel_id = request.GET.get('hotel_id')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if hotel_id and start_date and end_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        available_room = Room.objects.filter(
            hotel_id=hotel_id,
            availability=True
        ).exclude(
            id__in=Booking.objects.filter(
                date_arrival__lte=end_date,
                date_departure__gte=start_date,
                status='подтвержденная'
            ).values_list('room_id', flat=True)
        )

        data = {
            'Номер комнаты': [room.id for room in available_room],
            'Тип': [room.type for room in available_room],
            'Цена': [room.price for room in available_room],
            'Описание': [room.description for room in available_room]
        }
        df = pd.DataFrame(data)

        html_table = df.to_html()

        context = {'html_table': html_table}

        return render(request, 'available_rooms.html', context)
    return render(request, 'available_rooms.html', {})


def rooms_in_price_range(request):
    """Доступные номера в заданном ценовом диапазоне"""
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # Проверяем, что оба параметра запроса предоставлены
    if min_price and max_price:
        rooms = Room.objects.filter(price__range=(min_price, max_price))

        data = {
            'Название': [room.type for room in rooms],
            'Описание': [room.description for room in rooms],
            'Цена': [room.price for room in rooms]
        }

        df = pd.DataFrame(data)

        html_table = df.to_html()

        context = {'html_table': html_table}

        return render(request, 'rooms_in_price_range.html', context)
    return render(request, 'rooms_in_price_range.html', {})
