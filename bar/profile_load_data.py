from django.core.management import call_command
from django.db import connection


call_command('load_data')
print(len(connection.queries))
