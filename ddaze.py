
class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"


class Notifier:
    def send(self, recipient, message: str):
        raise NotImplementedError("Subclasses must implement this method")


class EmailNotifier(Notifier):
    def send(self, recipient, message: str):
        
        print(f"Sending email to {recipient.email}: {message}")

class SMSNotifier(Notifier):
    def send(self, recipient, message: str):
       
        print(f"Sending SMS to {recipient.phone_number}: {message}")

class NotificationService:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def notify(self, recipient, message: str):
        self.notifier.send(recipient, message)

def main():
    user_email = User("Ali", "ali@gmail.com")
    user_sms = User("Bob", "bob@mail.com")
    user_sms.phone_number = "+71234567890"  

 
    email_notifier = EmailNotifier()
    sms_notifier = SMSNotifier()

    notification_service_email = NotificationService(email_notifier)
    notification_service_sms = NotificationService(sms_notifier)

    
    notification_service_email.notify(user_email, "This is an email notification.")

   
    notification_service_sms.notify(user_sms, "This is an SMS notification.")

if __name__ == "__main__":
    main()
