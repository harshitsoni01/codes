from selenium import webdriver

driver = webdriver.Chrome(executable_path= "C:/chromedriver_win32/chromedriver.exe")
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
count = int(input('Enter the count : '))
msg = input("enter your message :")

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_3uMse')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_1U1xa')
    button.click()
