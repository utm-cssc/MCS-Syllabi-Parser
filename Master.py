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


def loadChromeDriver():
    if not isfile('Master/chromedriver.exe') and isfile('Master/chromedriver.dat'):
        file = list(open('Master/chromedriver.dat'))
        data = literal_eval(file[0])
        n = 'Master/chromedriver.exe'
        Icon = data
        icondata = zlib.decompress(b64decode(Icon))
        tempFile = n
        iconfile = open(tempFile,"wb")
        iconfile.write(icondata)
        iconfile.close()
        print('built ChromeDriver')
    if not isfile('Master/chromedriver.dat'):
        print('ERROR:NO DATA FILE')

def createBrowser(url = '', headless=False, blockImages=True, hideConsole = False, downloadDirectory=None):
    loadChromeDriver()
    chromeOptions = ChromeOptions()
    if blockImages: prefs = {"profile.managed_default_content_settings.images":2}; chromeOptions.add_experimental_option("prefs",prefs)
    if headless: chromeOptions.add_argument("--headless"); chromeOptions.add_argument("--window-size=1920x1080")
    if downloadDirectory: chromeOptions.add_argument("download.default_directory="+downloadDirectory)
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

def Pkill(string='chromedriver.exe'):
    import psutil
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == string:
            proc.kill()
