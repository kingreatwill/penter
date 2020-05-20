# http://docs.peewee-orm.com/en/latest/peewee/quickstart.html#quickstart
# https://github.com/coleifer/peewee
from peewee import *

db = SqliteDatabase('people.db')


class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db  # This model uses the "people.db" database.


class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db  # this model uses the "people.db" database


db.connect()
db.create_tables([Person, Pet])

from datetime import date

uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
uncle_bob.save()  # bob is now stored in the database
grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1))
herb = Person.create(name='Herb', birthday=date(1950, 5, 5))
grandma.name = 'Grandma L.'
grandma.save()  # Update grandma's name in the database.
herb.save()

grandma_s = Person.select().where(Person.name == 'Grandma L.').get()
print(grandma_s)



