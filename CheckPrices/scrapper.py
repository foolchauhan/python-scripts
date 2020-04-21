'''
Packages to install::
pip install requests bs4

for User-Agent google search my user agent

Price Id = priceblock_ourprice or priceblock_saleprice
Product Title Id = productTitle
Availability Id = availability


Allowed less secure apps for sending email :: I didn't do that, I use the below method

Google App Password : Mail : <Your client> : <Your App Password>

'''

import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/dp/B081BCWRGX/ref=cm_sw_em_r_mt_dp_U_HrUMEbAC9JYV9'
URL2 = 'https://www.amazon.in/Nestle-Everyday-Dairy-Whitener-Pouch/dp/B00NYZQX9A/ref=lp_21246948031_1_1?srs=21246948031&ie=UTF8&qid=1587215763&sr=8-1'

headers = {
    "User-Agent" : " Search google for your User Agent <My User-Agent>" 
}
def checkPrice():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    title = soup.find(id="productTitle").get_text().strip()

    price = soup.find(id="priceblock_ourprice").get_text().strip() if soup.find(id="priceblock_ourprice") is not None else soup.find(id="priceblock_saleprice").get_text().strip() if soup.find(id="priceblock_saleprice") is not None else soup.find(id="availability").find("span").get_text().strip() if soup.find(id="availability") is not None else None

    availability = soup.find(id="availability").find("span").get_text().strip() if soup.find(id="availability") is not None else '0'

    if "unavailable" not in price and price is not None:
        # send_mail()


    # print(title)
    # print(price[1:].strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('<yourmail@mail.com>', '<Your App Password>')
    subject = "The price fell down!"
    body = 'Check the amazon link :: https://www.amazon.in/dp/B081BCWRGX/ref=cm_sw_em_r_mt_dp_U_HrUMEbAC9JYV9'
    msg = f"Subject: {subject} \n\n {body}"
    
    server.sendmail(
        '<senders email>',
        '<receievr mail>',
        msg
    )
    print('Hey, email has been sent')
    server.quit()
