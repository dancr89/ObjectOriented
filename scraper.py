import json
import re
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep

colors = []

def data_values_from_string(string):
    pattern = r'[0-9]+%?'
    matches = re.findall(pattern, string)

    if len(matches) > 0:
        return matches

    return []



if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Chrome(executable_path='C:\\Users\\Asus\\Downloads\\chromedriver_win32\\chromedriver.exe', options=options)
    driver.get('https://htmlcolorcodes.com/')

    agree_button = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, './/button[text()="AGREE"]')))
    agree_button.click()

    soup = BeautifulSoup(driver.page_source, features='html.parser')

    header_elemets = soup.find('header', {'id': 'flat'})
    color_elements = header_elemets.find_all('div', class_='js-color')


    for color_element in color_elements:
        data_hex = color_element.get('data-hex')
        data_rgb = color_element.get('data-rgb')
        data_hsl = color_element.get('data-hsl')

        rgb_values = data_values_from_string(data_rgb)
        hsl_values = data_values_from_string(data_hsl)

    colors.append({
        'hex': data_hex,
        'rgb': {
            'r': rgb_values[0],
            'g': rgb_values[1],
            'b': rgb_values[2],
        },
        'hsl': {
            'h': hsl_values[0],
            's': hsl_values[1],
            'l': hsl_values[2],
        }
    })

    #write to file
    print('colors', colors)
    with open('colors.json', 'w') as json_file:
        json.dump(colors, json_file, indent=4)

    driver.close()

