import sqlite3
import os

def init_db():
    # Absolute project root
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Output directory
    output_dir = os.path.join(project_root, "output")
    os.makedirs(output_dir, exist_ok=True)

    # Absolute DB path
    db_path = os.path.join(output_dir, "asana_simulation.sqlite")
    print(f"[DB PATH] {db_path}")

    # Connect
    conn = sqlite3.connect(db_path)

    # Load schema
    schema_path = os.path.join(project_root, "schema.sql")
    print(f"[SCHEMA PATH] {schema_path}")

    with open(schema_path, "r", encoding="utf-8") as f:
        schema_sql = f.read()

    conn.executescript(schema_sql)
    conn.commit()

    # VERIFY tables exist
    tables = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall()
    print("[TABLES AFTER SCHEMA]:", tables)

    return conn
