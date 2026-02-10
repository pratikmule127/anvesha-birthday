import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_USER = os.environ["EMAIL_USER"]
EMAIL_PASS = os.environ["EMAIL_PASS"]
TO_EMAIL   = os.environ["TO_EMAIL"]

subject = "🌙 Today feels different…"

body = """
किञ्चित् अपि प्रतीक्षते… 🌙

Some days arrive quietly,
yet stay longer than expected.

Open it when you feel ready:
https://pratikmule127.github.io/anvesha-birthday/

— PD
"""

msg = MIMEMultipart()
msg["From"] = EMAIL_USER
msg["To"] = TO_EMAIL
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain", "utf-8"))

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(EMAIL_USER, EMAIL_PASS)
server.send_message(msg)
server.quit()

print("✅ Birthday mail sent")
