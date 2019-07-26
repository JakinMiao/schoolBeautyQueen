# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
from scrapy.http import FormRequest
from scrapy.selector import Selector
from ..config import host_address
from scrapy_splash import SplashRequest
import time
import os
import requests
import re

def formatStr(itemStr):
  return re.sub('\s', '', itemStr)


class BeatyQueenSpider(Spider):
  name = "beatyQueen"
  allowed_domains = ["www.xiaohuar.com"]
  start_urls = [

  ]
  def __init__(self):
    self.base_url = 'http://www.xiaohuar.com{}'

  def parse(self, response):
    pass
  
  def insert_data_to_db(self, params):
    try:
      result = requests.post(host_address + '/api/v1/platform/liuyan', json = params)
      print(result.text)
    except Exception as e:
      print('error!!!!!!!{}'.format(e))

