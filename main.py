from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import requests
import random
import undetected_chromedriver.v2 as uc
import os
import pyautogui


def lay_ip(): # Hàm để lấy IP Privater Vip 16k/ngày của https://tinsoftproxy.com/
    api_key = open('api_key.txt','r',encoding='utf-8')
    api_key = api_key.read() # Lấy api_key để sử dụng 
    url_get_ip = 'http://proxy.tinsoftsv.com/api/changeProxy.php?key='+api_key
    ip_about = requests.get(url_get_ip).json()
    try:
        ip = ip_about['proxy'] # Lấy IP
        print(ip)
        return ip
    except:
        time_dely = ip_about['next_change']
        print('Vui lòng đợi '+str(time_dely)+'s để lấy IP mới')
        time.sleep(int(time_dely))
        return lay_ip()
def khoitao():
    opts = uc.ChromeOptions()
    opts.add_argument('--incognito')
    opts.add_argument(f'--proxy-server='+lay_ip())
    return uc.Chrome(options=opts)

def runnow():
    name = open('name.txt','r',encoding='utf-8').read().splitlines()
    mail = open('gmail.txt','r',encoding='utf-8').read().splitlines()
    vi = open('vi.txt','r',encoding='utf-8').read().splitlines()
    nb = min(len(vi),len(mail))
    for i in range(3,nb):
        try:
                driver = khoitao()
                driver.maximize_window()
                driver.get('https://sweepwidget.com/view/37647-8nctwjyh/8u4fuq-37647')
                time.sleep(15)
                pyautogui.scroll(random.randint(-500,0))
                time.sleep(1)
                pyautogui.scroll(random.randint(200,600))
                time.sleep(1)
                pyautogui.scroll(random.randint(-500,0))
                time.sleep(1)
                pyautogui.scroll(random.randint(200,600))
                pyautogui.scroll(-2000)
                time.sleep(1)
                pyautogui.moveTo(x=random.randint(696, 1202),y=random.randint(124, 142),duration=0.26)
                pyautogui.click()
                time.sleep(1)
                pyautogui.typewrite(random.choice(name),interval=0.37)
                time.sleep(2)
                pyautogui.moveTo(x=random.randint(695,1199),y=random.randint(217, 230),duration=0.31)
                pyautogui.click()
                time.sleep(2)
                pyautogui.typewrite(mail[i],interval=0.47)
                time.sleep(1)
                pyautogui.moveTo(x=random.randint(698, 1195),y=random.randint(270, 297),duration=0.2)
                pyautogui.click()
                time.sleep(5)


                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[1]/div/div[1]/div[2]').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[1]/div/div[2]/div[1]/div/div/a').click()
                time.sleep(2)
                
                driver.switch_to.window(driver.window_handles[0])
                
                time.sleep(1)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[1]/div/div[2]/div[2]/div/div/input[1]').send_keys(random.choice(name))
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[1]/div/div[2]/div[2]/div/div/input[1]').send_keys(Keys.ENTER)
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[1]/div/div[1]/div[2]').click()


                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[2]/div/div[1]/div[2]').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[2]/div/div[2]/div[1]/div/div/a').click()
                time.sleep(2)
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(1)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[2]/div/div[2]/div[2]/div/div/input[1]').send_keys(random.choice(name))
                time.sleep(1)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[2]/div/div[2]/div[2]/div/div/input[1]').send_keys(Keys.ENTER)
                time.sleep(1)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[2]/div/div[1]/div[2]').click()
                time.sleep(1)

                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[3]/div/div[1]/div[2]').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[3]/div/div[2]/div[1]/div/div/a').click()
                time.sleep(2)
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[3]/div/div[2]/div[2]/div/div/input[1]').send_keys(random.choice(name))
                time.sleep(1)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[3]/div/div[2]/div[2]/div/div/input[1]').send_keys(Keys.ENTER)
                time.sleep(1)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[3]/div/div[1]/div[2]').click()
                time.sleep(1)

                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[4]/div/div[1]/div[2]').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[4]/div/div[2]/div[1]/div/div/a').click()
                time.sleep(1)
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[4]/div/div[2]/div[2]/div/div/input[1]').send_keys(random.choice(name))
                time.sleep(1)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[4]/div/div[2]/div[2]/div/div/input[1]').send_keys(Keys.ENTER)
                time.sleep(1)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[4]/div/div[1]/div[2]').click()
                time.sleep(1)


                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[5]/div/div[1]/div[2]').click()
                time.sleep(1)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[5]/div/div[2]/div[1]/div/div/a').click()
                time.sleep(2)
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(3)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[5]/div/div[2]/div[2]/div/div/input[1]').send_keys(random.choice(name))
                time.sleep(1)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[5]/div/div[2]/div[2]/div/div/input[1]').send_keys(Keys.ENTER)
                time.sleep(1)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[5]/div/div[1]/div[2]').click()
                time.sleep(1)


                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[6]/div/div[1]/div[2]').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[6]/div/div[2]/div/div/div/div/input[1]').send_keys(vi[i])
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[6]/div/div[2]/div/div/div/div/input[1]').send_keys(Keys.ENTER)
                time.sleep(2)
                u = open('gmail.txt','r',encoding='utf-8').read().splitlines()[1:]
                updategmail = '\n'.join(u)
                u1 = open('gmail.txt','w',encoding='utf-8')
                u1.write(updategmail)
                u1.close()
                z = open('vi.txt','r',encoding='utf-8').read().splitlines()[1:]
                vizz = '\n'.join(z)
                z1 = open('vi.txt','w',encoding='utf-8')
                z1.write(vizz)
                z1.close()
                time.sleep(5)
                driver.quit()
        except:
                u = open('gmail.txt','r',encoding='utf-8').read().splitlines()[1:]
                updategmail = '\n'.join(u)
                u1 = open('gmail.txt','w',encoding='utf-8')
                u1.write(updategmail)
                u1.close()
                z = open('vi.txt','r',encoding='utf-8').read().splitlines()[1:]
                viz = '\n'.join(z)
                z1 = open('vi.txt','w',encoding='utf-8')
                z1.write(viz)
                z1.close()
                driver.quit()
        
runnow()