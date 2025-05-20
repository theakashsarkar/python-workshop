class Notification:
    def send(self, message):
        print(f"Sending message: {message}")

def log_notification(notification_obj):
    def wrapper(message):
        print(f"[LOG] About to send message")
        notification_obj.send(message)
        print(f"[LOG] Message sent")
    return wrapper

def timestamp_notification(notification_obj):
    def wrapper(message):
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        notification_obj.send(f"[{timestamp}] {message}")
    return wrapper

if __name__ == "__main__":
    notifier = Notification()
    log_notifier = log_notification(notifier)
    log_notifier("hello world")

    timestamped_notifier = timestamp_notification(notifier)
    timestamped_notifier("Hello World")

    logged_timestamped = log_notification(timestamp_notification(notifier))
    logged_timestamped("Hello World")
