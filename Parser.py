from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from settings import bosses_respawn_days_setting
from settings import link_events
from selenium.webdriver.support.ui import Select
import time


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

    # Из записей формируем список
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
    # Удаление лишнего босса Core. Queen Ant добавляется как 2 босса, Ant удаляем, а ключ Queen заменяем на Queen Ant.
    # переписаны на if чтобы избежать KeyError, когда боссы ещё не убиты (актуально для переоткрытия серверов)
    if 'Core' in __death_dict:
        del __death_dict['Core']
    if 'Ant' in __death_dict:
        del __death_dict['Ant']
    if 'Queen' in __death_dict:
        __death_dict['Queen Ant'] = __death_dict.pop('Queen')
    return __death_dict


# def get_castles_siege():
#     __link = link_events
#     __servers_dict = {}
#     __castles_dict = {}
#     # __serv = serv
#
#     # Настройка аргументов и опций
#     __options = webdriver.ChromeOptions()
#     __options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 FireFox/84.0")
#     __options.add_argument("--disable-blink-features=AutomationControlled")
#     __options.add_argument("--no-sandbox")
#
#     # Парсинг
#     __browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=__options)
#     __browser.get(__link)
#     __block = __browser.find_element(By.CLASS_NAME, 'tx3')
#     # __all_castles = __block.find_elements(By.TAG_NAME, 'a')
#     __button_castles = __block.find_element(By.XPATH, "// *[ @ id = 'page_contents'] / div[1] / a[5]").click()
#
#     __block_serv_castles = __browser.find_elements(By.CLASS_NAME, 'vubor')
#     __change_serv = __block_serv_castles(by=By.CLASS_NAME, value='option')
#     # __change_serv = __block.find_elements(By.CLASS_NAME, 'vubor')
#     __select_serv = Select(__change_serv)
#     __select_serv.select_by_value('2')
#     __button_serv = __block_serv_castles.find_element(By.XPATH, '/html/body/div/div[3]/div/div/table/tbody/tr/td[2]/div[1]/div[3]/form/p/a').click()
#     time.sleep(10)
