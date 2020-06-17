from selenium import webdriver

driver = webdriver.Chrome(executable_path= "C:/chromedriver_win32/chromedriver.exe")
#select the path according to your place of extraction
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
count = int(input('Enter the count : '))
msg = input("enter your message :")

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
#this is to select the name of the user/group
user.click()

msg_box = driver.find_element_by_class_name('_3uMse')#this is to select the "type message" box

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_1U1xa')#this is to click the "send" button
    button.click()
