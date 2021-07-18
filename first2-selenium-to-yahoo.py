from selenium import webdriver

chromedriver_path = 'chromedriver.exe'

brower_driver = webdriver.Chrome(chromedriver_path)

brower_driver.get('https://www.yahoo.com/')


brower_driver.close()
brower_driver.quit()