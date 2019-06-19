import math
from selenium import webdriver
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/math.html')

x_element=browser.find_element_by_css_selector('#input_value')
x = x_element.text
y=calc(x)
answer_element=browser.find_element_by_css_selector('#answer')
answer_element.send_keys(y)

check_element=browser.find_element_by_css_selector('#robotCheckbox')
check_element.click()

robot_element=browser.find_element_by_css_selector('#robotsRule')
robot_element.click()

button=browser.find_element_by_css_selector('button')
button.click()
