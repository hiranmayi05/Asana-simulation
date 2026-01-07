import os
from dotenv import load_dotenv

load_dotenv()

EMPLOYEE_COUNT = int(os.getenv("EMPLOYEE_COUNT", 7500))
