from tinydb import TinyDB, Query
from tinydb.operations import delete
db = TinyDB('database.json')
User = Query()

db.update(delete('age'), User.age.exists())
db.insert({'name': 'John', 'age': 22})
db.insert({'name': 'Johnny', 'age': 7})
db.insert({'name': 'Bob', 'age': 3})

print(db.search((User.name == 'John')))
