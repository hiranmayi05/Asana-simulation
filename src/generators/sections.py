import uuid

def gen_sections(conn):
    projects = conn.execute("SELECT project_id FROM projects")
    for p in projects:
        for i, s in enumerate(["To Do", "In Progress", "Done"]):
            conn.execute(
                "INSERT INTO sections VALUES (?,?,?,?)",
                (str(uuid.uuid4()), p[0], s, i)
            )
    conn.commit()
