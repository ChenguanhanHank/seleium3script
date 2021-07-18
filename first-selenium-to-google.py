from selenium import webdriver

chromedriver_path = 'chromedriver.exe'

brower_driver = webdriver.Chrome(chromedriver_path)

brower_driver.get('https://www.google.com/')