import shelve

print("shelve --- Python 对象持久化")

with shelve.open('spam') as db:
    db['eggs'] = 'eggs'

with shelve.open('spam') as db:
    print(db['eggs'])