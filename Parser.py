from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def get_bosses():
    res_check = []
    death_dict = {}
    new_format = "%d.%m.%Y"
    old_format = '%Y-%m-%d'
    bosses_dict = {'Baium': 4, 'Antharas': 8, 'Valakas': 8, 'Orfen': 3, 'Queen': 2, 'Core': 1, 'Ant': 2}

    # Настройка аргументов и опций
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 FireFox/84.0")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.headless = True

    # Парсинг
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    browser.get('https://ru.asterios.tm/index.php?cmd=rss&serv=2&filter=epic')
    block = browser.find_element(By.CLASS_NAME, 'center')
    all_bosses = block.find_elements(By.TAG_NAME, 'a')

    # Все записи записываем в список
    for boss in all_bosses:
        res_check.append(boss.text)

    # На основе списка формируем словарь из даты и имени босса
    for i in list(reversed(res_check)):
        x, y, z, u, *o = i.split(" ")
        for p in o:
            # death_dict[p] = [x]
            death_dict[p] = (
                    datetime.datetime.strptime(x, old_format) + datetime.timedelta(days=bosses_dict[p])).strftime(
                new_format)
            continue
    # Удаление лишнего босса Core. Queen Ant добавляется как 2 босса, Ant удаляем, а ключ Queen заменяем на Queen Ant
    del death_dict['Ant']
    del death_dict['Core']
    death_dict['Queen Ant'] = death_dict.pop('Queen')
    return death_dict
