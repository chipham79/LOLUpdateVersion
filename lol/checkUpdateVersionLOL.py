from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import datetime
from re import search
from selenium.webdriver.common.by import By
import maildemo
import slack_bot


def checkStringContainSubString(actualString, expString):
    if (actualString == expString):
        return True
    print(f"Actual String: {actualString}, and Expected String {expString}")
    return False


currentDate = datetime.datetime.now()
# Formart date
currentDateFormat = currentDate.strftime("%Y-%m-%d")

# General Infor
linkUpdateLOL = "https://lienminh.garena.vn/download"
updateManualDesc = "//div[@class='section history']/div[@class='content']/div[@class='row'][1]/div[@class='column'][1]"

# Email Infor
fromEmail = "notification.lmht@gmail.com"
password = "srnydajuzmoaqyat"
toEmail = ""  # Input the email that you want to send to.

subject = "A new version of League of Legends has been released."
body = f"WARNING: NEW VERSION IS COMINGGGGGGGGGGGGGG. Please update right now!. Link to download: {linkUpdateLOL}"


# Set up headless broswer
options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)


# Direct to link
driver.get(linkUpdateLOL)

# Get string Cập Nhật Thủ Công
desc = driver.find_element(By.XPATH, updateManualDesc).text

# Check currentdate contain in update desctiption version
result = checkStringContainSubString(currentDateFormat, desc)

# Khởi tạo ban đầu
em = maildemo.EmailService(fromEmail, password, toEmail, subject, body)

if(result):
    slack_bot.sendMessageToSlack(body)
    print("Success")
else:
    print("No version update today")
