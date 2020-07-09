'''
Created on 2020. 7. 6.

@author: solom
'''
# -*- Encoding:utf-8 -*-
import json
import urllib
from urllib.parse import urlencode, quote_plus, unquote


# WRS_02 취수장,정수장,가압장 코드 조회서비스의 테스트를 위한  클래스
class WRS_02 :
    '''
    WRS_02 : 취수장,정수장,가압장 코드조회 서비스 
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

       
        