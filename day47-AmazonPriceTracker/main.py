import requests
import smtplib
from bs4 import BeautifulSoup

threshold_val = 1500
product_url = 'https://www.amazon.com.tr/Philips-HF3505-01-%C4%B1%C5%9F%C4%B1kl%C4%B1-Wake-UP-Wecktoene/dp/B00VAA1IRS/ref=zg_bs_12501894031_sccl_1/259-2438719-7280836?th=1'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,tr;q=0.8"
}

response = requests.get(product_url
    , headers=headers)

data = response.text
soup = BeautifulSoup(data, "lxml")
price = soup.find(name="span", class_="a-price-whole")
price = float(price.get_text().strip(','))


from_addr = "thirtydays03@gmail.com"
password = "qfuldnvkkjbccidn"
to_addrs = "thirthydays03@yahoo.com"
if price <= threshold_val:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Transport Layer Security, decrypted the email and makes it impossible to read
        connection.login(user=from_addr, password=password)
        connection.sendmail(from_addr=from_addr, to_addrs=to_addrs,
                            msg=f"Subject:Amazon Price\n\n"
                                f"Price of the product you are watching dropped the threshold: {threshold_val} TL!\n"
                                f"link: {product_url}")