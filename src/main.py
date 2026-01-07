from database import init_db
from generators.organizations import gen_org
from generators.teams import gen_teams
from generators.users import gen_users
from generators.projects import gen_projects
from generators.sections import gen_sections
from generators.tasks import gen_tasks

def main():
    conn = init_db()

    print("[STEP] Generating organization")
    gen_org(conn)

    print("[STEP] Generating teams")
    gen_teams(conn)

    print("[STEP] Generating users")
    gen_users(conn)

    print("[STEP] Generating projects")
    gen_projects(conn)

    print("[STEP] Generating sections")
    gen_sections(conn)

    print("[STEP] Generating tasks")
    gen_tasks(conn)

    conn.close()
    print("Database generated successfully")

if __name__ == "__main__":
    main()
