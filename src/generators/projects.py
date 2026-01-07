import uuid, datetime

def gen_projects(conn):
    teams = [r[0] for r in conn.execute("SELECT team_id FROM teams")]
    for t in teams:
        conn.execute(
            "INSERT INTO projects VALUES (?,?,?,?,?,?,?)",
            (
                str(uuid.uuid4()),
                t,
                "Sprint Board",
                "Engineering",
                "2025-01-01",
                "2025-03-01",
                datetime.datetime.utcnow()
            )
        )
    conn.commit()
