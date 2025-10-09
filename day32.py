import smtplib
from email.message import EmailMessage

def send_email(sender_email, app_password, to_email, subject, message):
    try:
        msg = EmailMessage()
        msg.set_content(message)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = to_email

        # Connect to Gmail SMTP server
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, app_password)
            smtp.send_message(msg)

        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("=== Email Sender App ===")
    sender = input("Enter your Gmail address: ")
    password = input("Enter your app password: ")
    receiver = input("Enter receiver email: ")
    subject = input("Enter subject: ")
    message = input("Enter message: ")

    send_email(sender, password, receiver, subject, message)
