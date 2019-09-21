import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base64 import b64decode
from ast import literal_eval
from os.path import isfile, abspath
import zlib
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver

def createBrowser(url = '', headless=False, blockImages=True, hideConsole = False, downloadDirectory=None) -> WebDriver:
     if not isfile('Master/chromedriver.exe'):
         print("Missing chromedriver.exe file")
         return None
    chromeOptions = ChromeOptions()
    prefs = {}
    if blockImages: 
        prefs["profile.managed_default_content_settings.images"] = 2
        
    if headless: 
        chromeOptions.add_argument("--headless")
        chromeOptions.add_argument("--window-size=1920x1080")
    
    if downloadDirectory: 
        prefs["download.default_directory"] = downloadDirectory+'\\'
        prefs["directory_upgrade"] = True
    
    if downloadDirectory or blockImages:
        chromeOptions.add_experimental_option("prefs",prefs)
    
    chrome_serv = webdriver.myService('path--to--exe.exe')
    chrome_serv.service_args = ["hide_console", ]
    if isfile('Master/chromedriver.exe'):
        drive = abspath("Master/chromedriver.exe")
        if hideConsole:
            browser = webdriver.myWebDriver(executable_path=drive, chrome_options=chromeOptions, service_args=chrome_serv.service_args)
        else:
            browser = webdriver.myWebDriver(executable_path=drive, chrome_options=chromeOptions)
        
    else:
        if hideConsole:
            browser = webdriver.myWebDriver(chrome_options=chromeOptions, service_args=chrome_serv.service_args)
        else: browser = webdriver.myWebDriver(chrome_options=chromeOptions)
    if url:
        browser.get(url)
    return browser

def Pkill(string='chromedriver.exe') -> None:
    import psutil
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == string:
            proc.kill()
