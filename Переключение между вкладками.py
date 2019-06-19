import math
from selenium import webdriver
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')
button=browser.find_element_by_css_selector('button')
button.click()
confirm = browser.switch_to.alert
confirm.accept()

new_window = browser.window_handles[1] # Получаем имя новой вкладки
browser.switch_to.window(new_window) #Переключаемся на вторую вкладку
x_element=browser.find_element_by_css_selector('#input_value')
x = int(x_element.text)
print(x)
y=calc(x)
answer_element=browser.find_element_by_css_selector('#answer')
answer_element.send_keys(y)

button2=browser.find_element_by_css_selector('button')
button2.click()