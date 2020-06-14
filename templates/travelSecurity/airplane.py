from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import sys
from bs4 import BeautifulSoup as bs
import re
import smtplib
from email.mime.text import MIMEText
from subprocess import Popen, PIPE
import pickle
import argparse
from flask import Flask, request

outcity = request.form['airport_one']
incity = request.form['airport_two']
out_date = request.form['date_one']
in_date = request.form['date_two']

def clean(string):
    ret = ''
    in_string = False

    for c in string:
        if c in ['\n', ' ']:
            if in_string == True:
                ret += c
                in_string = False
            else:
                continue
        else:
            in_string = True
            ret += c

    return ret[:-1]


class Expedia:
    def __init__(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
    

    def search(self, origin_city, destination_city, start_date, return_date):
        data_storage = open('flight-price.txt', 'a')
        data_storage.write('-'*30 + '\n' + datetime.date.today().strftime('%b %d %Y result:') + '\n')

        url = "https://www.expedia.com/Flights-Search?trip=roundtrip&leg1=from:{org_city},to:{dest_city},departure:{origin_date}TANYT&leg2=from:{dest_city},to:{org_city},departure:{return_date}TTANYT&passengers=children:0,adults:1&mode=search" \
                .format(org_city=origin_city, \
                dest_city=destination_city, \
                origin_date=start_date, \
                return_date=return_date)

        search = self.driver.get(url)
        # print search
        time.sleep(10)
        content = None

'''
parser = argparse.ArgumentParser()
parser.add_argument('outcity', help='the outbound city')
parser.add_argument('incity', help='the inbound city')
parser.add_argument('out_date', help='outbound date')
parser.add_argument('in_date', help='inbound date')
args = parser.parse_args()
outcity = args.outcity
incity = args.incity
out_date = args.out_date
in_date = args.in_date   
'''


expedia = Expedia()

expedia.search(outcity,incity,out_date,in_date)