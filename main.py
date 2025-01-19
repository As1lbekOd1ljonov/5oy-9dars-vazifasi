import redis

try:
    db = redis.Redis(host="localhost", port=6379, db=0)
    db.ping()
except redis.ConnectionError as e:
    print("Redis serveriga ulanib bo'lmadi. Iltimos, serverni tekshiring.")
    exit()

# Vazifa 1
db.set("name", "Toxir")
a = db.get("name")
print(a.decode("utf-8"))  # Bajaring va "utf-8" ga o'giring

# Vazifa 2
if db.exists("name"):
    db.set("name", "Sobir")
    b = db.get("name")
    print(b.decode("utf-8"))

# Vazifa 3
db.setex("key2", 10, "value2")
print(db.get("key2").decode("utf-8"))

# Vazifa 4
if db.exists("name"):
    name_value = db.get("name").decode("utf-8") + "_updated"
    db.set("name", name_value)
    print(db.get("name").decode("utf-8"))

# Vazifa 5
db.set("counter", 0)
db.incr("counter")
db.incrby("counter", 5)
print(int(db.get("counter")))

# Vazifa 6
db.decr("counter")
db.decrby("counter", 2)
print(int(db.get("counter")))

# Vazifa 7
print(db.ttl("key2"))
print(bool(db.exists("name")))

# Vazifa 8
db.mset({"last_name": "Toxirov", "first_name": "Toxir"})
values = db.mget("last_name", "first_name")
print([v.decode("utf-8") for v in values])

# Vazifa 9
db.set("phone_number", "")
db.append("phone_number", "+998885960804")
print(db.get("phone_number").decode("utf-8"))

# Vazifa 10
a = db.getrange("name", 0, 10)
print(a.decode("utf-8"))

# Vazifa 11
db.setrange("name", 0, "Replaced")
print(db.get("name").decode("utf-8"))

# Vazifa 12
db.delete("key2")
print(bool(db.exists("key2")))

# Vazifa 13
a = db.getset("name", "new_final_value")
print(a.decode("utf-8"))
print(db.get("name").decode("utf-8"))

# Vazifa 14
print(db.strlen("name"))

# Vazifa 15
db.set("key5", "value5", nx=True)
print(db.get("key5").decode("utf-8"))

# Vazifa 16
print(db.getset("name", "atomic_value").decode("utf-8"))

# Vazifa 17
db.set("key6", "1,2,3,4,5")
values = db.get("key6").decode("utf-8").split(",")
print(values)

# Vazifa 18
print(db.type("name"))

# Vazifa 19
print([key.decode("utf-8") for key in db.keys("T*")])

db.close()



