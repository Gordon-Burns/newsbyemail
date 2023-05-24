import requests
from send_email import send_email

topic = "tesla"

url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&sortBy=publishedAt&" \
      "apiKey=890603a55bfa47048e4490069ebee18c&" \
      "language=en"

# Make Request
request = requests.get(url)

# Get the data as a dictionary
content = request.json()

# Access the title and url
body = ""
for article in content["articles"][0:10]:
    if article["title"] is not None:
        body = "Subject: Todays News" + "\n" + body + article["title"] + "\n" \
               + str(article["url"]) + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)
