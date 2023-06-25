from faker import Faker
from faker.providers import profile
from datetime import datetime, timedelta, date
from rich import print
from rich.table import Table

from weekday_translate import weekday_translate

table = Table(title='Дні народження\nна наступному тижні', style='#ed156c')
table.add_column('День поздоровлення', style='#f50000')
table.add_column('Іменинник', justify='center', style='#2124de')

fake = Faker("uk-UA")
fake.add_provider(profile)

Faker.seed(8)

data = []
for i in range(300):  #якщо поставити range більше 750 виникає помилка: ValueError: day is out of range for month??
    prof = fake.profile()
    data.append({'name': prof['name'],
                'birthday': prof['birthdate']})


WEEKDAYS = dict(Monday=[],
                Tuesday=[],
                Wednesday=[],
                Thursday=[],
                Friday=[],
                Saturday=[],
                Sunday=[])


def get_period() -> tuple[date, date]:
    current_date = datetime.now()
    start_period = current_date + timedelta(days=5-current_date.weekday())
    return start_period.date(), (start_period + timedelta(6)).date()


def get_weekday(friend):
    return friend['birthday'].strftime("%A")


def check_friends(friends_list: list):
    # print(data)
    current_year = datetime.now().year
    for friend in friends_list:
        birthday = friend['birthday']
        if isinstance(birthday, datetime):
            birthday = birthday.date()
        dt = date(birthday.year, birthday.month, birthday.day).replace(year=current_year)
        start, end = get_period()
        if start <= dt <= end:
            if get_weekday(friend) in ['Saturday', 'Sunday']:
                WEEKDAYS['Monday'].append(friend['name'])
            else:
                WEEKDAYS[get_weekday(friend)].append(friend['name'])
    for day, value in WEEKDAYS.items():
        if len(value) > 0:
            table.add_row(str(weekday_translate(day)), str(value[0]))
    print(table)


if __name__ == '__main__':
    check_friends(data)
