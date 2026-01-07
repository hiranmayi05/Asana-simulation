from faker import Faker
import uuid, datetime
from config import EMPLOYEE_COUNT

fake = Faker()

def gen_users(conn):
    org_id = conn.execute(
        "SELECT org_id FROM organizations"
    ).fetchone()[0]

    teams = [r[0] for r in conn.execute("SELECT team_id FROM teams")]

    for i in range(EMPLOYEE_COUNT):
        uid = str(uuid.uuid4())
        conn.execute(
            "INSERT INTO users VALUES (?,?,?,?,?,?)",
            (
                uid,
                org_id,
                fake.name(),
                fake.email(),
                fake.job(),
                datetime.datetime.utcnow()
            )
        )

        conn.execute(
            "INSERT INTO team_memberships VALUES (?,?)",
            (teams[i % len(teams)], uid)
        )

    conn.commit()
