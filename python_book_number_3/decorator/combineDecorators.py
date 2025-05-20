class Notification:
    def send(self, message):
        print(f"Sending notification: {message}")

def log_notification(notification_obj):
    def wrapper(message):
        print(f"[LOG] About to send message") 
        if hasattr(notification_obj, 'send'):
            notification_obj.send(message)
        else:
            notification_obj(message)
        print(f"[LOG] Message sent")
    return wrapper

def timestamped_notification(notification_obj):
    def wrapper(message):
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if hasattr(notification_obj, 'send'):
            notification_obj.send(f"[{timestamp}] {message}")
        else:
            notification_obj(f"[{timestamp}] {message}")
    return wrapper

def file_logged_notification(notification_obj):
    def wrapper(message):
        file_name = "log.txt"
        mode = "a"
        if hasattr(notification_obj,'send'):
            notification_obj.send(f'{message}')
            with open(file_name, mode) as f:
                f.write(f" {message}\n")
        else:
            notification_obj(message)
            with open(file_name, mode) as f:
                f.write(f"{message}\n")
    return wrapper

if __name__ == "__main__":
    notifier = Notification()
    # notifier_file = file_logged_notification(timestamped_notification(notifier))
    # notifier_file("Hello, world!")
    # logged_timestamped = log_notification(timestamped_notification(notifier))
    # logged_timestamped("Combined decorators!")
    # log_notification(timestamped_notification(notifier))("Hello, world!")
    # timestamped = timestamped_notification(notifier)  # Creates timestamp wrapper)
    # timestamped_notification(file_logged_notification(timestamped))("file logged")
    # timestamped("Hello, world!")  # Calls timestamp wrapper

    file_logged = file_logged_notification(timestamped_notification(notifier))('Hello, world!')    

# Step 2: Outer decorator
    # notifier_file = file_logged_notification(timestamped)  # Creates file logging wrapper
    # print(notifier_file)

# Step 3: Call the composed decorators
    # notifier_file("Hello, world!") 
