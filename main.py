from plyer import notification 
import requests
from bs4 import BeautifulSoup as BS
import time

url = 'https://coinmarketcap.com/'
def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="C:/Users/saayu/Desktop/python reminder bot/images/bitcoin.ico",
        timeout=3
    )


if __name__=="__main__":
    while(1):
        page = requests.Session().get(url)
        html_content = requests.Session().get(url).text
        soup = BS(html_content, 'lxml')
        table = soup.find('table', attrs={'class': 'h7vnx2-2 czTsgW cmc-table'})
        data = []
        trs = table.tbody.find_all('tr')
        for i in range(0, 10):
            td = trs[i].find_all('td')

            check_class24=td[4].span.span.get('class')
            check_class7=td[5].span.span.get('class')

            ch24="+"
            ch7="+"
            if (check_class24[0]=='icon-Caret-down'):
                ch="-"

            if (check_class7[0]=='icon-Caret-down'):
                ch7="-"

            record = [td[1].text,td[2].div.a.div.p.text,td[3].text,ch24+td[4].span.text,ch7+td[5].span.text]
            data.append(record)
        req_coins=['Bitcoin','Ethereum','Cardano','Solana','Avalanche']

        for coin in data:
            if coin[1] in req_coins:
                notifText=f"Price: {coin[2]}\n24-hour change: {coin[3]}\n7-day change: {coin[4]}\n"
                print(notifText)
                notifyMe(coin[1],notifText)
                time.sleep(2)  
            # print(resp)
        time.sleep(10)

    
