import os
from datetime import date
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Secrets from GitHub Actions
EMAIL_USER = os.environ["EMAIL_USER"]
EMAIL_PASS = os.environ["EMAIL_PASS"]
TO_EMAIL   = os.environ["TO_EMAIL"]

# Automatic letter generation
letters_folder = "letters"
year = date.today().year
letter_file = f"{letters_folder}/{year}.html"

os.makedirs(letters_folder, exist_ok=True)

if not os.path.isfile(letter_file):
    content = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>{year}</title>
  <link rel="stylesheet" href="../assets/style.css">
</head>
<body>
  <div class="center">
    <h2 class="slow">🌙 {year}</h2>
    <p class="fade">
      Some moments do not ask for attention.
    </p>
    <p class="fade delay">
      They arrive quietly,<br>
      and stay longer than expected.
    </p>
    <p class="fade delay">
      May this year be gentle with you.
    </p>
    <p class="tiny">
      — Someone who noticed
    </p>
  </div>
</body>
</html>"""
    with open(letter_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Letter for {year} created automatically.")
else:
    print(f"Letter for {year} already exists.")

# Prepare email
link = f"https://pratikmule127.github.io/anvesha-birthday/letters/{year}.html"

subject = "🌙 Today feels different…"

body = f"""
किञ्चित् अपि प्रतीक्षते… 🌙

Some days arrive quietly,
yet stay longer than expected.

Open it when you feel ready:
{link}

— PD
"""

msg = MIMEMultipart()
msg["From"] = EMAIL_USER
msg["To"] = TO_EMAIL
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain", "utf-8"))

# Send email
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(EMAIL_USER, EMAIL_PASS)
server.send_message(msg)
server.quit()

print("✅ Birthday mail sent")
