"""
the utility to load user information to the database from a csv file
"""
import io
import csv
from datetime import datetime
from django.contrib import messages

from .models import User


def user_import(request, file):
    decoded_file = file.read().decode('utf-8')
    io_string = io.StringIO(decoded_file)
    csv_reader = csv.DictReader(io_string)
    user_objects = []
    for row in csv_reader:
        print(row)
        try:
            user_objects.append(User(
                first_name=row['FirstName'],
                last_name=row['LastName'],
                username='{}_{}'.format(row['FirstName'], row['LastName']),
                birth_date=datetime.strptime(row['BirthDate'], '%Y/%m/%d'),
                registration_date=datetime.strptime(row['RegistrationDate'], '%Y/%m/%d')
            ))
        except:
            messages.error(request, f'Document has invalid data for row {row}.')
    try:
        User.objects.bulk_create(user_objects, batch_size=100)
    except:
        messages.error(request, 'Document has invalid data.')
