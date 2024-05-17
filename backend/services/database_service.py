from config import config
from dao.database_connection import DatabaseConnection

dao = DatabaseConnection(
    host=config.get("database", "database.host"),
    user=config.get("database", "database.user"),
    password=config.get("database", "database.password"),
    database=config.get("database", "database.dbname")
)
try:
    dao.connect()
    print("User DB connection successful")
except Exception as e:
    print("User DB (user) connection error:", e)
