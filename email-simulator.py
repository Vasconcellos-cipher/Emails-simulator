import datetime


class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timestamp = datetime.datetime.now()
        self.read = False

    def mark_as_read(self):
        self.read = True

    def display_full_email(self):
        self.mark_as_read()

        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    def __str__(self):
        status = 'Read' if self.read else 'Unread'

        return (
            f"[{status}] "
            f"From: {self.sender.name} | "
            f"Subject: {self.subject} | "
            f"Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
        )


class Inbox:
    def __init__(self):
        self.emails = []

    def receive_email(self, email):
        self.emails.append(email)

    def list_emails(self):
        if not self.emails:
            print('Your inbox is empty.\n')
            return

        print('\nYour Emails:')

        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')

    def read_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return

        actual_index = index - 1

        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return

        self.emails[actual_index].display_full_email()

    def delete_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return

        actual_index = index - 1

        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return

        del self.emails[actual_index]

        print('Email deleted.\n')


class User:
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body):
        email = Email(
            sender=self,
            receiver=receiver,
            subject=subject,
            body=body
        )

        receiver.inbox.receive_email(email)

        print(f'Email sent from {self.name} to {receiver.name}!\n')

    def check_inbox(self):
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    def read_email(self, index):
        self.inbox.read_email(index)

    def delete_email(self, index):
        self.inbox.delete_email(index)


def main():
    tory = User("Tory")
    ramy = User("Ramy")

    users = {
        "Tory": tory,
        "Ramy": ramy
    }

    # Emails automáticos
    tory.send_email(
        ramy,
        "Hello",
        "Hi Ramy, just saying hello!"
    )

    ramy.send_email(
        tory,
        "Re: Hello",
        "Hi Tory, hope you are fine."
    )

    # Primeiro mostra as inbox
    print("\n=== Inboxes ===")
    tory.check_inbox()
    ramy.check_inbox()

    # Pergunta se quer enviar email
    send_choice = input("\nDo you want to send a new email? (yes/no): ")

    if send_choice.lower() == "yes":

        sender_name = input("Sender (Tory/Ramy): ")
        receiver_name = input("Receiver (Tory/Ramy): ")
        subject = input("Subject: ")
        body = input("Body: ")

        if sender_name in users and receiver_name in users:

            sender = users[sender_name]
            receiver = users[receiver_name]

            sender.send_email(receiver, subject, body)

        else:
            print("Invalid users.\n")

    # Ler email
    read_choice = input("\nDo you want to read an email? (yes/no): ")

    if read_choice.lower() == "yes":

        user_name = input("Which inbox? (Tory/Ramy): ")

        if user_name in users:

            user = users[user_name]

            user.check_inbox()

            try:
                email_number = int(input("Enter email number to read: "))

                user.read_email(email_number)

            except ValueError:
                print("Please enter a valid number.\n")

        else:
            print("Invalid user.\n")

    # Deletar email
    delete_choice = input("\nDo you want to delete an email? (yes/no): ")

    if delete_choice.lower() == "yes":

        user_name = input("Which inbox? (Tory/Ramy): ")

        if user_name in users:

            user = users[user_name]

            user.check_inbox()

            try:
                email_number = int(input("Enter email number to delete: "))

                user.delete_email(email_number)

                print("\nUpdated Inbox:")
                user.check_inbox()

            except ValueError:
                print("Please enter a valid number.\n")

        else:
            print("Invalid user.\n")


if __name__ == '__main__':
    main()