from plyer import notification
import requests
from bs4 import BeautifulSoup
import time




def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "./covidIcon.ico",
        timeout = 6
    )

def getData(url):
	r = requests.get(url)
	return r.text
if __name__ == "__main__":
	while True:
	    myHtmlData = getData('https://www.mohfw.gov.in/')
	    soup = BeautifulSoup(myHtmlData, 'html.parser')

	    myDataStr = ""
	    for tr in soup.find_all('tbody')[1].find_all('tr'):
	    	myDataStr += tr.get_text()
	    myDataStr = myDataStr[1:]

	    itemList = myDataStr.split("\n\n")

	    states = ['Weat Bengal', 'Maharashtra', 'Uttar Pradesh']
	    for item in itemList[0:22]:
	    	dataList = item.split('\n')
	    	if dataList[1] in states:
	    		nTitle = 'Cases of Covid-19'
	    		nText = f"state{dataList[1]}\nIndian :{dataList[2]} & Foreign: {dataList[3]}\ncured: {dataList[4]}\nDeath: {dataList[5]}"
	    		notifyMe(nTitle, nText)
	    		time.sleep(2)

	    time.sleep(3600)