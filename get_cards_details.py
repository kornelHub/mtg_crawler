import csv
from selenium import webdriver
import os
from selenium.webdriver.common.by import By

def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = True
    driver = webdriver.Chrome(f'{os.getcwd()}/chromedriver.exe', options=chrome_options)
    base_url = 'https://gatherer.wizards.com/Pages/Card/Details.aspx?printed=true&multiverseid={}'
    f = open("./output.csv", "w")
    writer = csv.writer(f, delimiter=';')

    for i in range(1, 296):
        print(i)
        driver.get(base_url.format(i))
        card_name = driver.find_element(By.XPATH, "//*[contains(text(), 'Card Name')]/parent::*/ div[2]")
        types = driver.find_element(By.XPATH, "//*[contains(text(), 'Types')]/parent::*/ div[2]")
        try:
            mana_cost = driver.find_elements(By.XPATH, "//div[contains(text(), 'Mana Cost')]/parent::*/div[2]/img")
        except:
            pass
        try:
            card_text = driver.find_element(By.XPATH, "//*[contains(text(), 'Card Text')]/parent::*/ div[2]/div")
        except:
            pass
        try:
            power_toughnes = driver.find_element(By.XPATH, "//*[contains(text(), 'P/T')]/parent::*/parent::*/ div[2]")
        except:
            pass
        try:
            flavor_text = driver.find_element(By.XPATH, "//*[contains(text(), 'Flavor Text')]/parent::*/ div[2]/div")
        except:
            pass
        rarity = driver.find_element(By.XPATH, "//*[contains(text(), 'Rarity')]/parent::*/ div[2]/span")
        expansion = driver.find_element(By.XPATH, "//*[contains(text(), 'Expansion')]/parent::*/ div[2]/div/a[2]")
        artist = driver.find_element(By.XPATH, "//*[contains(text(), 'Artist')]/parent::*/ div[2]/a")

        if len(driver.find_elements(By.XPATH, "//*[contains(text(), 'P/T')]/parent::*/parent::*/ div[2]")) > 0:
            writer.writerow([
                i,
                get(card_name),
                get(types),
                get_mana_cost(mana_cost),
                get(card_text) if len(driver.find_elements(By.XPATH, "//*[contains(text(), 'Card Text')]/parent::*/ div[2]/div")) > 0 else "-",
                get(power_toughnes) if len(driver.find_elements(By.XPATH, "//*[contains(text(), 'P/T')]/parent::*/parent::*/ div[2]")) > 0 else "-",
                get(flavor_text) if len(driver.find_elements(By.XPATH, "//*[contains(text(), 'Flavor Text')]/parent::*/ div[2]/div")) > 0 else "-",
                get(rarity),
                get(expansion),
                get(artist)
            ])

        elif "Land" == driver.find_element(By.XPATH,"//*[contains(text(), 'Types')]/parent::*/ div[2]").text:
             writer.writerow([
                 i,
                 get(card_name),
                 get(types),
                 get(card_text) if len(driver.find_elements(By.XPATH, "//*[contains(text(), 'Card Text')]/parent::*/ div[2]/div")) > 0 else "-",
                 get(flavor_text) if len(driver.find_elements(By.XPATH, "//*[contains(text(), 'Flavor Text')]/parent::*/ div[2]/div")) > 0 else "-",
                 get(rarity),
                 get(expansion),
                 get(artist)
            ])
        else:
            writer.writerow([
                i,
                get(card_name),
                get(types),
                get_mana_cost(mana_cost),
                get(card_text) if len(driver.find_elements(By.XPATH, "//*[contains(text(), 'Card Text')]/parent::*/ div[2]/div")) > 0 else "-",
                get(flavor_text) if len(driver.find_elements(By.XPATH, "//*[contains(text(), 'Flavor Text')]/parent::*/ div[2]/div")) > 0 else "-",
                get(rarity),
                get(expansion),
                get(artist)
                ])

def get(element):
    try:
        return element.text
    except:
        return "-"

def get_mana_cost(web_elements_list):
    mana_cost=''
    for x in web_elements_list:
        symbol = x.get_attribute('alt')
        if symbol == "Blue":
            mana_cost += 'U'
        elif symbol == "Variable Colorless":
            mana_cost += 'X'
        else:
            mana_cost += symbol[0]
    return mana_cost


if __name__ == '__main__':
    main()