'''
Script som laster ned alle bildene valgt instagram-bruker legger ut og laster opp de som slettes.
'''
import os
import instapy_cli as client
import requests
import shutil
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
load_dotenv()
import os

os.listdir()
os.getcwd()
INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')
USER_TO_FOLLOW = os.getenv('USER_TO_FOLLOW')

url = 'https://www.instagram.com/{}/'.format(USER_TO_FOLLOW)
image_url = 'https://instagram.fsvg1-1.fna.fbcdn.net/v/t51.2885-15/e35/s1080x1080/90085967_829026910950978_' \
          '7207290314169028145_n.jpg?_nc_ht=instagram.fsvg1-1.fna.fbcdn.net&_nc_cat=106&_nc_ohc=sKNKR76hvLQA' \
          'X9GI5MR&oh=d5c528a6e6c7c6e3534e9bfc935a986c&oe=5EA41047'


def download_picture(image_url, image_name):
    image_name = image_name + '.jpg'
    # Open the url image, set stream to True, this will return the stream content.
    resp = requests.get(image_url, stream=True)
    # Open a local file with wb ( write binary ) permission.
    local_file = open(image_name, 'wb')
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    resp.raw.decode_content = True
    # Copy the response stream raw data to local image file.
    shutil.copyfileobj(resp.raw, local_file)
    # Remove the image url response object.
    del resp


image_url = 'https://www.instagram.com/p/B91h_lSJC9A/'

page = requests.get(image_url)
soup = BeautifulSoup(page.content, "html.parser")


image_desc = soup.find_all('', class_="_6lAjh")
image_desc

text = 'Here you can put your caption for the post' + '\r\n' + 'new line #hashtag'
with client(username, password) as cli:
    cli.upload(image, text)