import sqlite3

conn = sqlite3.connect("rpg_db.sqlite3")

conn.row_factory = sqlite3.Row
curs = conn.cursor()

# 1). How many total Characters are there
query = """
SELECT COUNT(name) FROM charactercreator_character;
"""
results = curs.execute(query).fetchall()
print("total Characters:", results[0]['COUNT(name)'])

# 2). How many of each specific subclass?
subclass = ['charactercreator_cleric', 'charactercreator_fighter',
'charactercreator_mage', 'charactercreator_thief']
for character_class in subclass:
    query = f'SELECT COUNT(character_ptr_id) FROM {character_class}'
    results = curs.execute(query).fetchall()
    print(f'Each specific Subclass {character_class}:', results[0]
    ['COUNT(character_ptr_id)'])

query = "SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer"

results = curs.execute(query).fetchall()
print('Each specific Subclass charactercreator_mage:', results[0]['COUNT(mage_ptr_id)'])

# 3). How many total Items?
query = "SELECT COUNT(item_id) FROM charactercreator_character_inventory"
results = curs.execute(query).fetchall()
print('total Items:', results[0]['COUNT(item_id)'])
total_items = results[0]['COUNT(item_id)']

# 4). How many of the Items are weapons? How many are not?
query = 'SELECT COUNT(item_ptr_id) FROM armory_weapon'
results = curs.execute(query).fetchall()
print('Items are weapons:', results[0]['COUNT(item_ptr_id)'])
print('Items are NOT weapons:', total_items-results[0]['COUNT(item_ptr_id)'])

# 5). How many Items does each character have? (Return first 20 rows)

query = """
SELECT
character_id,
COUNT(item_id)
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;
"""

results = curs.execute(query).fetchall()
for ii in range(len(results)):
    print('Character', results[ii][0], 'has', results[ii][1], 'items.')


# 6).How many Weapons does each character have? (Return first 20 rows)
query = """
SELECT
character_id,
COUNT(item_id)
FROM charactercreator_character_inventory 
JOIN armory_weapon 
ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY character_id
LIMIT 20;
"""
results = curs.execute(query).fetchall()
for ii in range(len(results)):
    print('Character', results[ii][0], 'has', results[ii][1], 'weapons')

# 7). On average, how many Items does each Character have?

query = """
SELECT COUNT(item_id)
FROM charactercreator_character_inventory
GROUP BY character_id;
"""

results = curs.execute(query).fetchall()
items = 0
for i in range(len(results)):
    items += results[i][0]
average = items / len(results)
print('Average amount of items per each character:', average)


# 8). On average, how many Weapons does each character have?

query = """
SELECT
COUNT(item_id)
FROM charactercreator_character_inventory
Join armory_weapon
ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY character_id
"""

results = curs.execute(query).fetchall()
weapons = 0
for ii in range(len(results)):
    weapons += results[ii][0]

average_weapon = weapons / len(results)
print('Average amount of weapons per each character:', average_weapon)

