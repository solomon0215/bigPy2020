'''
Created on 2020. 7. 7.

@author: solom
'''
# -*- Encoding:utf-8 -*-
import json
import urllib
from urllib.parse import urlencode, quote_plus, unquote


class WRS_06(object):
    '''
    WRS_06 : 정수장 ,배수지 코드 조회 서비스
    '''


    # URL,ServiceKey은 properties
    def __init__(self, url, ServiceKey,divCode):
        self.url = url  #URL
        self.ServiceKey = ServiceKey # SERVICEKEY
        self.divCode = divCode # 시설구분코드 (1,2,3,4)

    # 던질 url 조합
    def setUrl(self):
        queryParams = '?' \
                      +urlencode({quote_plus('_type'): 'json'  # 받는 타입
                                      , quote_plus('fcltyDivCode'): self.divCode  # 기관코드
                                      , quote_plus('serviceKey'): self.ServiceKey
                                    })
        return self.url + unquote(queryParams)
