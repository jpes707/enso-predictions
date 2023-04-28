import os
import re
import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.pmel.noaa.gov/cgi-tao/cover.cgi?P1=wind&P2=hf&P3=1979&P4=1&P5=20&P6=2023&P7=4&P8=21&P9=ascii&P10=None&P11=anonymous&P12=anonymous&P13=anonymous&P14=anonymous&P15=buoy&P16=disdel_drupal&P17=mean&P18=mean&P19=tser&P20=var&P21=2n137e&P22=5n137e&P23=8n137e&P24=0n147e&P25=2n147e&P26=5n147e&P27=5s156e&P28=2s156e&P29=0n156e&P30=2n156e&P31=5n156e&P32=8n156e&P33=8s165e&P34=5s165e&P35=2s165e&P36=0n165e&P37=2n165e&P38=5n165e&P39=8n165e&P40=8s180w&P41=5s180w&P42=2s180w&P43=0n180w&P44=2n180w&P45=5n180w&P46=8n180w&P47=8s170w&P48=5s170w&P49=2s170w&P50=0n170w&P51=2n170w&P52=5n170w&P53=8n170w&P54=8s155w&P55=5s155w&P56=2s155w&P57=0n155w&P58=2n155w&P59=5n155w&P60=8n155w&P61=5s140w&P62=2s140w&P63=0n140w&P64=2n140w&P65=5n140w&P66=9n140w&P67=8s125w&P68=5s125w&P69=2s125w&P70=0n125w&P71=2n125w&P72=5n125w&P73=8n125w&P74=8s110w&P75=5s110w&P76=2s110w&P77=0n110w&P78=2n110w&P79=5n110w&P80=8n110w&P81=8s95w&P82=5s95w&P83=2s95w&P84=0n95w&P85=2n95w&P86=5n95w&P87=8n95w&script=disdel/deliv-buoy-disdel-v79.csh')
res.raise_for_status()
html = res.content

print(html)

soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a', href=re.compile(r'\.ascii'))

base_url = 'https://www.pmel.noaa.gov'
download_path = '/Users/johnny/Downloads/wind'

if not os.path.exists(download_path):
    os.makedirs(download_path)

for link in links:
    file_url = base_url + link['href'].strip()
    print(file_url)
    file_name = os.path.join(download_path, os.path.basename(link['href']))

    response = requests.get(file_url)
    response.raise_for_status()

    with open(file_name, 'wb') as f:
        f.write(response.content)

    print(f'Downloaded {file_name}')
