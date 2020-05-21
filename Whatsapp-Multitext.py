from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r"C:\Python\chromedriver.exe")
driver.maximize_window()                        
driver.get('https://web.whatsapp.com/')

if __name__ == "__main__":
    while True:
        input('Enter anything after scanning QR code..  Hit ENTER to start')

        names = []  
        na=input("Enter your Friend's name and Number: ")
        cap=na.title()                                      
        names.extend(cap.split(","))                         
        msg = str(input("Enter your message: "))
        count = int(input("How many times: "))

        for name in names:
            user = driver.find_element_by_xpath(f'//span[@title = "{name}"]').click()

        sleep(2)
        msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

        for i in range(count):
            msg_box.send_keys(msg)
            button = driver.find_element_by_xpath('//button[@class="_35EW6"]').click()
        