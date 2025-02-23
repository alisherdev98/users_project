from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client["users"]

users = db['users']

# user_data = {"name": "Алексей", "age": 28, "email": "alex@mail.com"}
# insert_result = users.insert_one(user_data)
# print("ID вставленного документа:", insert_result.inserted_id)


# users_list = [
#     {"name": "Мария", "age": 32, "city": "Москва"},
#     {"name": "Иван", "age": 25, "hobbies": ["футбол", "гитара"]}
# ]
# insert_many_result = users.insert_many(users_list)
# print("IDs вставленных документов:", insert_many_result.inserted_ids)
#
# all_users = users.find()
# for user in all_users:
#     print(user)
#
#
# query = {"age": {"$gt": 30}}  # Возраст больше 30
# result = users.find(query)
# print("Пользователи старше 30 лет:")
# for user in result:
#     print(user)
#
#
# result = users.find({}, {"name": 1, "city": 1, "_id": 0})
# for user in result:
#     print(user)
#
#
# users.update_one(
#     {"name": "Алексей"},
#     {"$set": {"age": 29, "status": "active"}}
# )
#
# users.update_many(
#     {"age": {"$lt": 30}},
#     {"$inc": {"age": 1}}  # Увеличить возраст на 1
# )
#
# users.delete_one({"name": "Иван"})
#
#
users.delete_many({"name": "Мария"})