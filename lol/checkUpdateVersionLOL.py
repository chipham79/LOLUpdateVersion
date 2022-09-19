from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import datetime
from re import search
from selenium.webdriver.common.by import By
import maildemo
import slack_bot

def checkStringContainSubString(substring, fullstring):
    if search(substring, fullstring):
        return True

    return False



currentDate = datetime.datetime.now()
#Formart date
currentDateFormat = currentDate.strftime("%d/%m/%Y") 

#General Infor
linkUpdateLOL = "https://lienminh.garena.vn/download"
updateManualDesc = "div.currentVersion div.remind"

#Email Infor
fromEmail = "notification.lmht@gmail.com"
password = "srnydajuzmoaqyat"
toEmail = "" # Input the email that you want to send to. 

subject= "A new version of League of Legends has been released."
body = f"WARNING: NEW VERSION IS COMINGGGGGGGGGGGGGG. Please update right now!. Link to download: {linkUpdateLOL}"      


#Set up headless broswer
options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)


# Direct to link
driver.get(linkUpdateLOL)

#Get string Cập Nhật Thủ Công
desc = driver.find_element(By.CSS_SELECTOR, updateManualDesc).text

#Check currentdate contain in update desctiption version
result = checkStringContainSubString(currentDateFormat, desc)

#Khởi tạo ban đầu
em = maildemo.EmailService(fromEmail, password, toEmail, subject, body) 

if( result ):    
    em.setContent()
    em.sendEmail()
    slack_bot.sendMessageToSlack(body)
else:
    body = "NO VERSION UPDATE TODAY !!!!!!!!!!!!!!!!!!!! YEAH"
    em.setBody(body)
    em.setContent()
    em.sendEmail()
    slack_bot.sendMessageToSlack(body)


