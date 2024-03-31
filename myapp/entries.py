import csv
from .models import Room, HotelEmployee, Booking, \
    Review, Event, Cancellation, Payment, Service


def import_data_room(file_path):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            room_object = Room(
                hotel_id=row['hotel_id'],
                type=row['type'],
                price=row['price'],
                availability=row['availability'],
                description=row['description']
            )
            room_object.save()


def import_data_hotel_employee(file_path):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            hotel_employee_object = HotelEmployee(
                hotel_id=row['hotel_id'],
                FIO=row['FIO'],
                post=row['post'],
                contact_information=row['contact_information'],
            )
            hotel_employee_object.save()


def import_data_booking(file_path):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            booking_object = Booking(
                client_id=row['client_id'],
                room_id=row['room_id'],
                date_arrival=row['date_arrival'],
                date_departure=row['date_departure'],
                count_guests=row['count_guests'],
                status=row['status'],
            )
            booking_object.save()


def import_data_review(file_path):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            review_object = Review(
                hotel_id=row['hotel_id'],
                client_id=row['client_id'],
                amount=row['amount'],
                comment=row['comment'],
                writing_date=row['writing_date'],

            )
            review_object.save()


def import_data_event(file_path):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            event_object = Event(
                hotel_id=row['hotel_id'],
                date_and_time=row['date_and_time'],
                name_event=row['name_event'],
                description=row['description'],
                venue=row['venue'],

            )
            event_object.save()


def import_data_cancellation(file_path):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cancellation_object = Cancellation(
                booking_id=row['booking_id'],
                date_and_time_references=row['date_and_time_references'],

            )
            cancellation_object.save()


def import_data_payment(file_path):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            payment_object = Payment(
                booking_id=row['booking_id'],
                amount=row['amount'],
                date_and_time=row['date_and_time'],
            )
            payment_object.save()


def import_data_service(file_path):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            service_object = Service(
                hotel_id=row['hotel_id'],
                name=row['name'],
                description=row['description'],
                price=row['price'],
                availability=row['availability'],

            )
            service_object.save()


import_data_room('rooms.csv')