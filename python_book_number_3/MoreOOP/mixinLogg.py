class LoggingMixin:
    def log(self, message):
        print(f"Log: {message}")

class DatabaseConnection:
    def connect():
        print(f"connect Database")

class User(DatabaseConnection, LoggingMixin):
    
    def save(self):
        self.log("Saveing user the database")
        self.connect()

user = User()
user.save()