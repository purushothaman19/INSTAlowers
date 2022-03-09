from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

chrome_driver_path = '/Users/purush/Development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

username = "YOUR USERNAME"
PASSWORD = "YOUR {PASSWORD}"

insta_url = 'https://www.instagram.com'
driver.get(insta_url)

''' Login '''

try:

    time.sleep(2)
    email = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    email.send_keys(username)

    password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    password.send_keys(PASSWORD)

    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()

    ''' searching for the account '''

except NoSuchElementException:

    login = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button')
    login.click()

    time.sleep(2)
    email = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    email.send_keys(username)

    password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    password.send_keys(PASSWORD)

    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()

time.sleep(3)
search_bar = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search_bar.send_keys('YOUR FAV ACCOUNT')

time.sleep(2)
required_account = driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div'
    '[2]/div/div[1]/a/div')
required_account.click()

''' getting the followers '''

time.sleep(3)
followers = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
followers.click()

''' squashing the followers button '''

time.sleep(1)
total_no_of_followers = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li['
                                                     '2]/a/span').get_attribute('title').replace(',', '')

time.sleep(2)

div = 3
check = 8
for i in range(1, int(total_no_of_followers)):

    try:
        follow_status = driver.find_element_by_xpath(
            f'/html/body/div[5]/div/div/div[2]/ul/div/li[{i}]/div/div[{div}]/button'). \
            text

        if follow_status == 'Follow':
            follow = driver.find_element_by_xpath(f'/html/body/div[5]/div/div/div[2]/ul/div/li[{i}]/div/div['
                                                  f'{div}]/button')

            if i == check:
                follow.send_keys(Keys.END)
                check += 5
                continue

            time.sleep(1)

            try:
                follow.click()
            except StaleElementReferenceException:
                i += 1
                continue

        elif follow_status == 'Following' or 'Requested':

            follow = driver.find_element_by_xpath(f'/html/body/div[5]/div/div/div[2]/ul/div/li[{i}]/div/div['
                                                  f'{div}]/button')

            if i == check:
                follow.send_keys(Keys.END)
                check += 1
                print("scroll")
                continue

            i += 1
            continue

    except NoSuchElementException:
        i += 1
        div = 2
        print("no")
        continue
