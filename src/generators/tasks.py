from faker import Faker
import uuid, datetime, random
from config import EMPLOYEE_COUNT

TASKS_PER_USER = 15  # realistic enterprise load

fake = Faker()

def gen_tasks(conn):
    sections = [r[0] for r in conn.execute("SELECT section_id FROM sections")]
    users = [r[0] for r in conn.execute("SELECT user_id FROM users")]

    total_tasks = EMPLOYEE_COUNT * TASKS_PER_USER

    for _ in range(total_tasks):
        conn.execute(
            "INSERT INTO tasks VALUES (?,?,?,?,?,?,?,?,?,?,?)",
            (
                str(uuid.uuid4()),
                None,
                random.choice(sections),
                None,
                fake.sentence(),
                fake.text(),
                random.choice(users),
                fake.date_between(start_date="-30d", end_date="+60d"),
                random.choice([0, 1]),
                datetime.datetime.utcnow(),
                None
            )
        )

    conn.commit()
