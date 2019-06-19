import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

# говорим Selenium проверять в течение 15 секунд, пока цена не станет=10 000
price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"10000 RUR")
    )
button_price=browser.find_element_by_css_selector('#book')
print(button_price.get_attribute('disabled'))
print(button_price.get_attribute('onclick'))
button_price.click()
x_element=browser.find_element_by_css_selector('#input_value')
x = int(x_element.text)
print(x)
y=calc(x)
answer_element=browser.find_element_by_css_selector('#answer')
answer_element.send_keys(y)

button_solve = browser.find_element_by_css_selector("#solve")
print(button_solve.get_attribute('id'))
print(button_solve.get_attribute('disabled'))
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)

#check_element=browser.find_element_by_css_selector('#robotCheckbox')
#check_element.click()

#robot_element=browser.find_element_by_css_selector('#robotsRule')
#robot_element.click()

button_solve.click()
