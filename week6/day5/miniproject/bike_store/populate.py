import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bike_store.settings")
import django
from random import randint

django.setup()
from datetime import date, timedelta
from rent.models import (
    Address,
    Customer,
    VehicleType,
    VehicleSize,
    Vehicle,
    Rental,
    RentalRate,
    RentalStation,
    VehicleAtRentalStation,
)
from faker import Faker

fake = Faker()


# def create_customers(number):
#     for _ in range(number):
#         address = Address(
#             address=fake.street_address(),
#             address2=fake.secondary_address(),
#             city=fake.city(),
#             country=fake.country(),
#             postal_code=fake.zipcode(),
#         )
#         address.save()

#         customer = Customer(
#             first_name=fake.first_name(),
#             last_name=fake.last_name(),
#             email=fake.email(),
#             phone_number=fake.phone_number(),
#             address=address,
#         )
#         customer.save()

#     print(f"CREATED {number} Customers")


# create_customers(100)


def create_fake_address():
    return Address.objects.create(
        address=fake.street_address(),
        city=fake.city(),
        country=fake.country(),
        postal_code=fake.zipcode(),
    )


def create_fake_customer():
    address = create_fake_address()
    return Customer.objects.create(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        phone_number=fake.phone_number(),
        address=address,
    )


def create_fake_vehicle_type():
    return VehicleType.objects.create(name=fake.word())


def create_fake_vehicle_size():
    return VehicleSize.objects.create(name=fake.word())


def create_fake_vehicle():
    vehicle_type = create_fake_vehicle_type()
    vehicle_size = create_fake_vehicle_size()
    return Vehicle.objects.create(
        vehicle_type=vehicle_type,
        date_created=fake.date_this_year(),
        real_cost=randint(50, 500),
        size=vehicle_size,
    )


def create_fake_rental(customer, vehicle):
    return Rental.objects.create(
        rental_date=fake.date_this_year(),
        return_date=fake.date_this_year(),
        customer=customer,
        vehicle=vehicle,
    )


def create_fake_rental_rate():
    vehicle_type = create_fake_vehicle_type()
    vehicle_size = create_fake_vehicle_size()
    return RentalRate.objects.create(
        daily_rate=randint(10, 100),
        vehicle_type=vehicle_type,
        vehicle_size=vehicle_size,
    )


def create_fake_rental_station():
    address = create_fake_address()
    return RentalStation.objects.create(
        name=fake.company(), capacity=randint(5, 50), address=address
    )


def create_fake_vehicle_at_rental_station(rental_station, vehicle):
    return VehicleAtRentalStation.objects.create(
        arrival_date=fake.date_this_year(),
        departure_date=fake.date_this_year(),
        vehicle=vehicle,
    )


def generate_fake_data(num_records):
    for _ in range(num_records):
        customer = create_fake_customer()
        vehicle = create_fake_vehicle()
        rental = create_fake_rental(customer, vehicle)
        rental_rate = create_fake_rental_rate()
        rental_station = create_fake_rental_station()
        vehicle_at_rental_station = create_fake_vehicle_at_rental_station(
            rental_station, vehicle
        )


if __name__ == "__main__":
    num_records = 10
    generate_fake_data(num_records)
    print(f"Generated {num_records} fake records.")
