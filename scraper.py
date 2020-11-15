import requests
from bs4 import BeautifulSoup
import smtplib
import time
import os

# testing with an available product
randomAvailableProductURL = 'https://www.amazon.nl/introductie-van-echo-4e-generatie-internationale-versie-met-hoogwaardig-geluid-smart-home-hub-en-alexa-houtskool-nederlandse-taal-niet-beschikbaar/dp/B085H3DKLT?ref_=Oct_s9_apbd_obs_hd_bw_bHraEtj&pf_rd_r=HTCE2EV5DXWK0ZEXWA60&pf_rd_p=99c91168-a5b4-5886-a2cc-55901204da66&pf_rd_s=merchandised-search-11&pf_rd_t=BROWSE&pf_rd_i=16366041031'

PS5URL = 'https://www.amazon.nl/Sony-PlayStation-PlayStation%C2%AE5-Console/dp/B08H93ZRK9/ref=sr_1_2?dchild=1&pd_rd_r=b650841f-fb85-4101-abbb-81b8ef8e567a&pd_rd_w=9JcQs&pd_rd_wg=q227G&pf_rd_p=0a56d51a-3836-41ed-bef3-b0c27e77df24&pf_rd_r=FBTG5A1MHW1FC32F8H2D&qid=1604245314&s=videogames&sr=1-2'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

def check_availability():
    page = requests.get(PS5URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    availability = soup.find(id="availability") #look for the element which tells us if the product is available
    if availability is not None:
        fullstring = availability.get_text(strip=True)
        substring = "niet"
        if substring in fullstring:
            print(availability.get_text(strip=True))
        else:
            send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(os.getenv('USER'), os.getenv('PASSWORD'))

    subject = 'PS5 availability'
    body = 'PS5 is available, check the amazon link! \n {}'.format(PS5URL)

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(os.getenv('USER'), os.getenv('RECEIVER'), msg)

    print('Email has been sent!')

    server.quit()

check_availability()
