from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
# from login_gmail_selenium.util.profiles.google_profile import GoogleProfile
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


classDict = {'title':'._mHead4__big_1m15n_825',
             'probnum':'._mCardPara_1m15n_835',
             }


# class Webpage():
#     def __init__(self,pagetitle):
#         pgsource = webdriver.Firefox()
#         # pgsource.
#         pgsource.get(f"https://www.codechef.com/practice/{pagetitle}")
#         time.sleep(5)
#         self.pagetitle= pagetitle
#         self.htcode = BeautifulSoup(pgsource.page_source)

#     def showCode(self):
#         return self.htcode.prettify()
    
# website = Webpage("basic-math-python")
# print(website.htcode.body.prettify())





# 'rjxanime@gmail.com'
# 'rj885592555souwal*664@rj'






pgsource = webdriver.Firefox()
pgsource.get(f"https://www.codechef.com/practice/basic-math-python")

loginButtonExist = WebDriverWait(pgsource,10).until(EC.element_to_be_clickable((By.CLASS_NAME,'m-login-button-no-border')))
print(loginButtonExist)

# htcode = BeautifulSoup(pgsource.page_source,features="lxml")



# loginbutton = htcode.select("._m-login-container--desktop_1bo7b_1984")
# print(loginbutton)

logID= pgsource.find_element(By.ID, "edit-name")
logID.send_keys("rjxanime")
logPass = pgsource.find_element(By.ID, "edit-pass")
logPass.send_keys('Rj@885592555')
logSub = pgsource.find_element(By.CLASS_NAME, "edit-submit-button")
logSub.click()
time.sleep(5)



title = htcode.find_all('._mCardPara_1m15n_835')
print(title)
for elem in title:
    print(elem.prettify())
    print("\n")
    print(elem[0].get_text())
    print("\n"*3)