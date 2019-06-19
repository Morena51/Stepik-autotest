import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')

num1=browser.find_element_by_css_selector('#num1').text
num2=browser.find_element_by_css_selector('#num2').text
answer=str(int(num1)+int(num2))
print(answer)
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_visible_text(answer)  # ищем элемент x+y

button=browser.find_element_by_css_selector('button')
button.click()
