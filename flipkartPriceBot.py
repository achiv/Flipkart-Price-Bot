from bs4 import BeautifulSoup
import requests
import lxml

item = "https://www.flipkart.com/da-vinci-code/p/itmfg24kndjycqyr?pid=9780552161275&lid=LSTBOK9780552161275GP16CT&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=5a5933bb-51e8-44bf-8eea-65f3785ee5d1.9780552161275.SEARCH&ppt=sp&ppn=sp&ssid=bxvc9l69eo0000001609837023803&qH=e8532ad8e7593e4a"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
    }

response = requests.get(item, headers = header)
soup = BeautifulSoup(response.content, "lxml")

price = soup.select_one(selector = "#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div:nth-child(2) > div > div.dyC4hf > div.CEmiEU > div > div._30jeq3._16Jk6d").getText()
final_price = float(price.split("₹")[1])
print(final_price)

import smtplib

title = soup.find(class_="B_NuCI").getText().strip()
title = title.encode('ascii', 'ignore').decode('ascii')
print(title)

requiredPrice = 320.00

if final_price < requiredPrice:
    message = f"{title} is now {final_price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("YOUR_EMAIL", "YOUR_PASSWORD")
        connection.sendmail(from_addr="YOUR_EMAIL", to_addrs="YOUR_EMAIL", msg = f"Subject: Price Alert\n\n{message}\n{item}")











# Write your code here :-)
