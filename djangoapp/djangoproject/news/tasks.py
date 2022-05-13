from django_uwsgi.decorators import timer
from django_eventstream import send_event
from faker import Faker

fake = Faker()

@timer(3, target='spooler')
def generate_a_message(num):
    date = fake.date_time_this_year()
    title = fake.sentence() 
    send_event('news', 'message', {'date': date, 'title':title})
