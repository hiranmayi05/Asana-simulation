import uuid

def gen_teams(conn):
    org_id = conn.execute(
        "SELECT org_id FROM organizations"
    ).fetchone()[0]

    teams = ["Engineering", "Marketing", "Operations"]

    for t in teams:
        conn.execute(
            "INSERT INTO teams VALUES (?,?,?,?)",
            (str(uuid.uuid4()), org_id, t, t)
        )

    conn.commit()
