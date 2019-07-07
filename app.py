# Scroll all the way to the bottom(Line 85 and 87) to insert your login info/hashtag to automate free likes on instagram
# In hoping doing so will get you free likes/follows on your profiles as well

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time
import random

class InstagramBot:
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.bot = webdriver.Chrome()

  def login(self):
    bot = self.bot
    bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

    try:

      emailSelector = "#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input"
      passwordSelector = "#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input"
      submitBtnSelector = "#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB > button"
      
      
      element = WebDriverWait(bot,20).until(
          EC.presence_of_element_located((By.CSS_SELECTOR, "#react-root > section > main > div > article > div > div:nth-child(1) > h1")))
      
      print("before locate input")

      email = WebDriverWait(bot,20).until(
          EC.presence_of_element_located((By.CSS_SELECTOR, emailSelector)))

      password = WebDriverWait(bot,20).until(
          EC.presence_of_element_located((By.CSS_SELECTOR, passwordSelector)))

      submitBtn = WebDriverWait(bot,20).until(
          EC.presence_of_element_located((By.CSS_SELECTOR, submitBtnSelector)))
      
      print("before clear input")
      email.clear()
      password.clear()

      print("before sendkeys input")
      email.send_keys(self.username)
      password.send_keys(self.password)
      submitBtn.click()

      nextLogo = WebDriverWait(bot,20).until(
          EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.oJZym > a > div > div.cq2ai > span')))
    
    except TimeoutException:
      print("shats loading")

  def like_post(self, hashtag):
    bot = self.bot
    bot.get('https://www.instagram.com/explore/tags/' + hashtag + '/')

    time.sleep(3)

    for i in range(1,3):
      bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(random.randint(2,15))
    print("before posts")
    
    hrefs = bot.find_elements_by_tag_name('a')
    links = [elem.get_attribute('href') for elem in hrefs]

    for link in links:
      bot.get(link)
      bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
      try:
        time.sleep(random.randint(1,20))
        bot.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[1]/button').click()
        time.sleep(random.randint(18,40))
      except Exception as e:
        time.sleep(2)


user = InstagramBot('<INSERT_USERNAME>', '<INSERT_PASSWORD>')
user.login()
user.like_post('<INSERT_HASHTAG_TO_LIKE')