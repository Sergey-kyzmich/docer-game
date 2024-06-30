import database
database.database().add_user(user={"name":"name", "money":5000, "level":0})
print(database.database().get_all())