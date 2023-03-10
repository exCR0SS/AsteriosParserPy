from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from settings import bosses_respawn_days_setting


def get_bosses(link_serv):
    __link = link_serv
    __res_check = []
    __death_dict = {}
    __new_format = "%d.%m.%Y"
    __old_format = '%Y-%m-%d'
    # bosses_dict = {'Baium': 4, 'Antharas': 8, 'Valakas': 8, 'Orfen': 3, 'Queen': 2, 'Core': 1, 'Ant': 2}
    __bosses_respawn_days = bosses_respawn_days_setting

    # Настройка аргументов и опций
    __options = webdriver.ChromeOptions()
    __options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 FireFox/84.0")
    __options.add_argument("--disable-blink-features=AutomationControlled")
    __options.add_argument("--no-sandbox")
    __options.headless = True

    # Парсинг
    __browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=__options)
    __browser.get(__link)
    __block = __browser.find_element(By.CLASS_NAME, 'center')
    __all_bosses = __block.find_elements(By.TAG_NAME, 'a')

    # Все записи записываем в список
    for boss in __all_bosses:
        __res_check.append(boss.text)

    # На основе списка формируем словарь из даты и имени босса
    for i in list(reversed(__res_check)):
        x, y, z, u, *o = i.split(" ")
        for p in o:
            # __death_dict[p] = [x]
            __death_dict[p] = (
                    datetime.datetime.strptime(x, __old_format) + datetime.timedelta(
                days=__bosses_respawn_days[p])).strftime(__new_format)
            continue
    # Удаление лишнего босса Core. Queen Ant добавляется как 2 босса, Ant удаляем, а ключ Queen заменяем на Queen Ant
    if 'Core' in __death_dict:
        del __death_dict['Core']
    del __death_dict['Ant']
    __death_dict['Queen Ant'] = __death_dict.pop('Queen')
    return __death_dict
