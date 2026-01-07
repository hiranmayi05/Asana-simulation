import uuid, datetime

def gen_org(conn):
    conn.execute(
        "INSERT INTO organizations VALUES (?,?,?,?)",
        (
            str(uuid.uuid4()),
            "Acme SaaS",
            "acme.com",
            datetime.datetime.utcnow()
        )
    )
    conn.commit()
