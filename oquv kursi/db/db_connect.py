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
            user=getenv("user")
        )

        cursors = db.cursor()
        cursors.execute(query)

        query_type = ["insert", "update", "delete", "create"]

        if type in query_type:
            db.commit()

            if type == "insert":
                return "[INFO] Inserted successfully"
            elif type == "update":
                return "[INFO] Updated successfully"
            elif type == "delete":
                return "[INFO] Deleted successfully"
            elif type == "create":
                return "[INFO] Created successfully"
            else:
                return "[ERROR]"
        else:
           return cursors.fetchall()