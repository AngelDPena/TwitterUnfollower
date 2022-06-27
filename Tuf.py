from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

usr = " "
pw = " "


def unfollow():
    driver = webdriver.Firefox()
    driver.get("http://twitter.com/login")
    driver.implicitly_wait(2)
    driver.maximize_window()

    login = driver.find_element_by_css_selector(
        "#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(6) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-iphfwy.r-s1qlax.r-ttdzmv > div > input")
    login.click()
    sleep(0.5)
    login.send_keys(usr)
    sleep(0.5)

    password = driver.find_element_by_css_selector(
        "#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(7) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-iphfwy.r-s1qlax.r-ttdzmv > div > input")
    password.click()
    sleep(0.5)
    password.send_keys(pw)
    sleep(0.5)
    password.send_keys(Keys.ENTER)

    driver.implicitly_wait(3)
    driver.get("https://twitter.com/" + usr + "/following")

    sleep(3)
    x = 0
    y = 50
    z = 0
    for x in range(y):
        for z in range(10):
            sleep(1)
            following = driver.find_element_by_xpath(
                "/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div[" + str(z + 1) + "]/div/div/div/div[2]/div[1]/div[2]/div")
            # /html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div
            following.click()
            # /html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div
            sleep(0.2)
            unfollow = driver.find_element_by_css_selector("#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-1kihuf0.r-18u37iz.r-1pi2tsx.r-1777fci.r-1pjcn9w.r-xr3zp9.r-1xcajam.r-ipm5af.r-9dcw1g > div.css-1dbjc4n.r-1awozwy.r-kemksi.r-1867qdf.r-1jgb5lz.r-pm9dpa.r-1rnoaur.r-d9fdf6.r-mfjstv.r-13qz1uu > div.css-1dbjc4n.r-18u37iz.r-13qz1uu > div.css-18t94o4.css-1dbjc4n.r-urgr8i.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-16y2uox.r-1w2pmg.r-ero68b.r-1gg2371.r-1ny4l3l.r-1fneopy.r-o7ynqc.r-6416eg.r-lrvibr > div > span > span")
            unfollow.click()
            sleep(0.2)
        driver.refresh()
        driver.implicitly_wait(1)
    driver.close()


unfollow()
