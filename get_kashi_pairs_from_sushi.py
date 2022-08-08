import time
from selenium import webdriver
from selenium.webdriver.common.by import By

base_url = 'https://app.sushi.com/kashi'
browser = webdriver.Chrome('C:\\Users\\Zanyar\\Downloads\\chromedriver.exe')
browser.get(base_url)
browser.maximize_window()
time.sleep(10)

x = input("Create a wallet and connect it to Sushiswap and choose your network\n"
          "if you do this works, please Enter your selected network:\n"
          " (Please enter 'AVAX' for AVALANCHE and 'BSC' for Binance Smart Chain")

lastHeight = browser.execute_script("return document.body.scrollHeight")
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)
    newHeight = browser.execute_script("return document.body.scrollHeight")
    if newHeight == lastHeight:
        break
    lastHeight = newHeight

pairs = browser.find_elements(By.XPATH, "//div[@class='text-base leading-5 font-bold flex gap-1 text-high-emphesis']")
pairs_list = []
for pair in pairs:
    pairs_list.append(pair.text)

fixed_pairs_list = []
for tokens in pairs_list:
    fixed_pairs_list.append(tokens.replace('\n', ''))

info = browser.find_elements(By.XPATH, "//div[@class='text-base leading-5 font-bold text-high-emphesis']")

info_list = []
for i in info:
    info_list.append(i.text)
    
pool_address = browser.find_elements(By.XPATH,
                                "//div[@class='hover:bg-dark-900/40 hover:cursor-pointer grid grid-cols-7 overflow-x-auto']")

address_list = []
for i in pool_address:
    address_list.append(i.get_attribute('href'))

print(len(info_list))
print(len(fixed_pairs_list))
print(len(address_list))

with open(r'info_list_'+x+'.txt', 'w') as info:
    for item in info_list:
        info.write("%s\n" % item)

with open(r'pairs_list_'+x+'.txt', 'w') as pairs:
    for item in fixed_pairs_list:
        pairs.write("%s\n" % item)

with open(r'address_list_'+x+'.txt', 'w') as address:
    for item in address_list:
        address.write("%s\n" % item)
        
print('Done')
