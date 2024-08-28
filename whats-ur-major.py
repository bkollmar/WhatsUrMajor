from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

url = 'https://lms.dickinson.edu/my/'
s = Service("Path To Chrome Driver")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get(url)

email_address = ''
password = ''

#Input First and Last Name Of The Person
firstName = ''
lastName = ''
fullName = ''

#Log In To Moodle
time.sleep(2)
email_login = driver.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]').send_keys(email_address)
next = driver.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input').click()
time.sleep(1)
pass_login = driver.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input').send_keys(password)
sign_in = driver.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input').click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input'))).click()

#Navigate To Academic Integretity Tutorial
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div/section[1]/div/aside/section[2]/div/div/ul[5]/li[1]/div/div/div/a'))).click()

#Go To Side bar (if it appears) and then go to Participants
participantsButton = '/html/body/div[2]/div[2]/nav[1]/ul/li[2]/a'
triplebarButton = '/html/body/div[2]/nav/div[1]/button'
driver.find_element(By.XPATH, participantsButton).click()

#Click Show All
driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/section[1]/div/div[3]/form/div/div/a').click()

time.sleep(2)

#Click Name
driver.find_element(By.LINK_TEXT, fullName).click()

time.sleep(3)

#Click Show More Classes
driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/section[1]/div/div/div[2]/section[2]/div/ul/li[1]/dl/dd/ul/li[11]/a').click()

#Scrape Classes
classes = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/section[1]/div/div/div[2]/section[2]/div/ul/li[1]').text
print(classes)

#Determine how many of each class participant has taken
math = classes.count('MATH')
econ = classes.count('ECON')
comp = classes.count('COMP')
span = classes.count('SPAN')
anthropology = classes.count('ANTH')
archeology = classes.count('ARCH')
art_history = classes.count('ARTH')
bio = classes.count('BIOL')
chem = classes.count('CHEM')
physics = classes.count('PHYS')
chinese = classes.count('CHIN')
classical = classes.count('CLST')
earth_sci = classes.count('ERSC')
law = classes.count('LAWP')

classArray = [math, econ, comp, span, anthropology, archeology, art_history, bio, chem, physics, chinese, classical, earth_sci, law]
class_dict = {math: 'Math', econ: 'Economics', comp: 'Computer Science', span: 'Spanish', anthropology: 'Anthropology', archeology: 'Archeology', art_history: 'Art History', bio: 'Biology', chem: 'Chemistry', physics: 'Physics', chinese: 'Chinese', classical: 'Classical Studies', earth_sci: ' Earth Sciences', law: 'Law & Policy'}
numOfMostClassesTaken = max(class_dict)
mostTakenClass = class_dict.get(max(class_dict))

print('The classes ' + fullName + ' are takeing are: ' + classes)
print(fullName + "'s major is most likely: " + mostTakenClass)