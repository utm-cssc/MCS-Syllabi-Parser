from Master import createBrowser
from getpass import getpass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

SyllabiDirectory = 'Syllabi/'

def gatherSyllabi(browser, username, password):
    userName = WebDriverWait(browser,60).until(EC.presence_of_element_located((By.ID, 'username')))
    passwordName = WebDriverWait(browser,60).until(EC.presence_of_element_located((By.ID, 'password')))
    userName.send_keys(username)
    passwordName.send_keys(password)
    passwordName.submit()





if __name__ == '__main__':
    username = input("Username: ")
    password = getpass()
    term = input("Fall, Winter, Summer?: ").strip().title()
    year = input("Year: ").strip()
    if term not in ('Fall','Winter','Summer'):
        print('Incorrect Term: Require "Fall", "Winter" or "Summer"')
        return
    try:
        int(year)
    except:
        print('Incorrect Year: Require Integer')
        return
    value = year
    if term == 'Fall':
        value += '9'
    elif term == 'Winter':
        value += '1'
    elif term == 'Summer':
        value += '5'
    browser = createBrowser(url='https://student.utm.utoronto.ca/CourseInfo/index.php?session_cd=20199&department_id=7',
                            headless=False,
                            blockImages=False,
                            hideConsole=False)
   
