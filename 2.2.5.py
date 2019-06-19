import os 
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

first_name = browser.find_element_by_css_selector('input[placeholder="Введите имя"]')
first_name.send_keys("Jam")

last_name = browser.find_element_by_css_selector('input[placeholder="Введите фамилию"]')
last_name.send_keys("Jacson")

email = browser.find_element_by_css_selector('input[name="email"]')
email.send_keys("test@test.com")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
file_btn = browser.find_element_by_css_selector('input[type="file"]')
file_btn.send_keys(file_path)

btn=browser.find_element_by_css_selector('button')
btn.click()
#element.send_keys(file_path)