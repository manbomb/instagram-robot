from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import numpy as np
import urllib
from urllib.request import urlopen
import cv2
import time
import pyautogui as pyag
import os
import random as rd
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-u", "--user", required=True, help="usuário para fazer login")
ap.add_argument("-p", "--pass", required=True, help="senha para fazer login")
args = vars(ap.parse_args())

labelsPath = os.path.sep.join(['./yolo-coco/', "coco.names"])
LABELS = open(labelsPath).read().strip().split("\n")

np.random.seed(42)
COLORS = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")

weightsPath = os.path.sep.join(['./yolo-coco/', "yolov3.weights"])
configPath = os.path.sep.join(['./yolo-coco/', "yolov3.cfg"])

print("[INFO] loading YOLO from disk...")
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)


def url_to_image(url):
	resp = urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	return image

def url_from_scode(driver,code):
	driver.get('http://127.0.0.1/Insta%20Robot/insta_url.php?q='+str(code))

	element = driver.find_element_by_css_selector('span.result')

	result = element.text

	return result

def scode_from_tag(driver,tag):
	driver.get('http://127.0.0.1/Insta%20Robot/insta_tag.php?q='+str(tag))
	element = driver.find_element_by_css_selector('body')
	txt = element.text
	list_urls = txt.split('\n')

	print("\nScodes from TAG "+str(tag)+"\n")

	return list_urls

def login_insta(driver,user,passw):
	driver.get('https://www.instagram.com/accounts/login/')

	time.sleep(5)
	
	user_inp = driver.find_element_by_xpath("//input[@name='username']")
	user_inp.send_keys(user)
	pass_inp = driver.find_element_by_xpath("//input[@name='password']")
	pass_inp.send_keys(passw)
	btt_sub = driver.find_element_by_xpath("//div[text()='Entrar']")
	btt_sub.click()

	time.sleep(5)
	
	btts = driver.find_elements_by_tag_name("button")
	btt_notnow = btts[len(btts)-2]
	btt_notnow.click()

	print("\nLogin: "+str(user)+":"+str(passw)+"\n")

def log(scode,comment):
	f = open("log.txt", "a")
	f.write(str(scode)+" : "+str(comment)+"\n")
	f.close()


def comment_post(driver,scode):
	driver.get('https://www.instagram.com/p/'+str(scode))

	time.sleep(5)
	
	txt = driver.find_element_by_class_name('Ypffh')
	txt.click()

	list_comm = open("comment_pidao.txt", "r")
	list_comm = list_comm.read().split("\n")
	comment = list_comm[rd.randint(0,len(list_comm)-1)]

	pyag.write(comment)
	pyag.press('enter')

	print("\n"+str(scode)+" : "+str(comment)+"\n")
	log(scode,comment)

	time.sleep(3)

def if_exist_comm(scode):
	if scode == '':
		return False

	f = open("log.txt", "r")
	f = f.read()

	if str(scode) in f:
		return True
	else:
		return False


opts = Options()
opts.headless = True

#driver = Chrome(options=opts, executable_path='chromedriver.exe')
driver = Chrome(executable_path='chromedriver.exe')

login_insta(driver,args["user"],args["pass"])

lista = open("tags.txt", "r")
lista = lista.read().split("\n")

for j in range(0,len(lista)):

	list_scodes = scode_from_tag(driver, lista[j])

	for i in range(0,len(list_scodes)):
		if not if_exist_comm(list_scodes[i]):
			comment_post(driver,list_scodes[i])