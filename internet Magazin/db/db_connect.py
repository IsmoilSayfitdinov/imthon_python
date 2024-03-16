import psycopg2 as database
from dotenv import load_dotenv
from os import getenv


load_dotenv()
class Dbconnect:
    @staticmethod
    def connect(query, type):
        db = database.connect(
            database=getenv("database"),
            host=getenv("host"),
            password=getenv("password"),
            user=getenv("user"),
        )

        cursors = db.cursor()
        cursors.execute(query)

        data = ["insert", "update", "delete", "create"]

        if type in data:
            db.commit()

            if type == "insert":
                return "[INFO] Insert Success"
            elif type == "update":
                return "[INFO] Update Success"
            elif type == "delete":
                return "[INFO] Delete Succses"
            elif type == "create":
                return "[INFO] Create Success"
            else:
                return "[ERROR]"
        else:
            return cursors.fetchall()
