import attrs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from pyautogui import write as typeWrite
from pyautogui import hotkey as sendSpecialKey
import time


validArgs = ['python','cpp','java','go','rust','c-sharp','c',
             'basic-math-cpp','basic-math-python','arrays-python',
             'greedy-algorithms','dynamic-programming',
             'time-complexity-python','python-dsa-intermediate-puzzles']
"""
A set of valid arguments in initialisation of Problempage class
"""


class Problempage():
    """
    The class scrapes web data from given codechef problem page.

    Args:
    pagename: str - problem page name 
              (example valid arguments
              in validArgs variable)
    """


    def __init__(self,pagename):
        self.driver = webdriver.Firefox()
        self.driver.get(f"https://www.codechef.com/practice/{pagename}")
        self.pagename = pagename


    def login(self,id: str="rjxanime", passw: str="Rj@885592555"):
        """
        Function is used to log into codechef to access more data
        
        Args: id: (default='rjxanime')
              passw: (default='Rj@885592555')"""
        #Click Login
        loginButtonExist = WebDriverWait(self.driver,10).until(
        EC.element_to_be_clickable((By.CLASS_NAME,"_m-login-button-no-border_1bo7b_1993")))
        loginButtonExist.click()

        #wait for page load
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,'edit-name')))
        
        #Enter Credentials and Login
        typeWrite(id)
        sendSpecialKey("tab")
        typeWrite(passw)
        sendSpecialKey("Enter")
        time.sleep(2)


    def scrapeData(self):
        """
        ScrapeData returns the data it scrapes from 
        the webpage in form of a dictionary with 
        labelled key value pairs.

        Output format:
        Title
        Description
        Number of Panels
        List of Panels : [Name,description,problems,[problem name, problem status]]
        """
        #take soup
        soup = BeautifulSoup(self.driver.page_source,"html.parser")
        
        #initialise dictionary for storing data
        data = {}
        
        title = soup.find(attrs={'class':'_mHead4__big_1m15n_825'})
        # print(title.get_text())
        data['Title'] = title.get_text()

        description = soup.find(attrs={'class':'_left_card_1m15n_231 _width80_1m15n_228'}).find(attrs={"class":"_mCardPara_1m15n_835"})
        # print(description.get_text())
        data['Description'] = description.get_text()




























        
        # panelcolumn = soup.find(attrs={"class":'_lRow800_1m15n_755 _lMarginTop__28_1m15n_773 undefined'})
        # allPanels = panelcolumn.findAll(attrs={"id":'panel1a-header'})
        # for panel in allPanels:
        #     print(panel.prettify())
        #     paneltitle = panel.find(attrs={'class':'_moduleCard__head_1m15n_487'})
        #     paneldesc = panel.find(attrs={'class':'_mCardPara_1m15n_835'})

        #     panelProblemList = panel.find(attrs={'class':'_tableContainer_1m15n_362'})
        #     print(panelProblemList)
        #     totalPanelDetail = [paneltitle.get_text(),paneldesc.get_text()]
        #     problemList = []
        #     for panelProblem in panelProblemList:
        #         problemName = panelProblem.find(attrs={'class':'_problemName_1m15n_404'}).get_text()
        #         problemState = panelProblem.find(attrs={'class':'_statusIcon_1m15n_423'})
        #         if "unattempted" in problemState:
        #             problemState = "Unattempted"
        #         if "locked" in problemState:
        #             problemState = "Locked"
        #         problemList.append([problemName,problemState.get_text()])
        #     totalPanelDetail.append(problemList[1:])

        #     print(panel.get_text())
        #     print("\n")


        return data






def main():
    for arg in ['python']:
        page = Problempage(arg)
        page.login()
        data = page.scrapeData()
        for key,value in data.items():
            # print(f"{key} : {value}")
            pass



if __name__ == "__main__":
    main()