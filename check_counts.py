import sqlite3

conn = sqlite3.connect("output/asana_simulation.sqlite")

print("Users:", conn.execute("SELECT COUNT(*) FROM users").fetchone()[0])
print("Tasks:", conn.execute("SELECT COUNT(*) FROM tasks").fetchone()[0])

conn.close()
