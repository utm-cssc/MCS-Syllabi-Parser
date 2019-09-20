from Master import createBrowser
from getpass import getpass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

SyllabiDirectory = 'Syllabi/'
SessionSelectID = 'session_cd'
DepartmentSelectID = 'department_id'

def gatherSyllabi(browser, username, password):
    userName = WebDriverWait(browser,60).until(EC.presence_of_element_located((By.ID, 'username')))
    passwordName = WebDriverWait(browser,60).until(EC.presence_of_element_located((By.ID, 'password')))
    userName.send_keys(username)
    passwordName.send_keys(password)
    passwordName.submit()
    WebDriverWait(browser,60).until(EC.presence_of_element_located((By.ID, 'fippa')))
    return

def setSelect(select_id, option_value):
    select = Select(driver.find_element_by_id(select_id))
    select.select_by_value(option_value)
    return

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
    departments = ['7', '27', '38']
    browser = createBrowser(url='https://student.utm.utoronto.ca/CourseInfo/index.php',
                            headless=False,
                            blockImages=False,
                            hideConsole=False)
    gatherSyllabi(browser)
    setSelect(SessionSelectID, value)
    for department in departments:
        setSelect(DepartmentSelectID, department)
        WebDriverWait(browser,60).until(EC.presence_of_element_located((By.XPATH, "//input[@value='Search']")))
    
            
