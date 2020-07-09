# -*- Encoding:utf-8 -*-
import json
import urllib
from urllib.parse import urlencode, quote_plus, unquote


# WRI_14(수위 분강우량조회)를 테스트를 위한  클래스
# 날짜만 args로 입력 나머지는 properties file
class PRI_02 :

    # URL,ServiceKey은 properties
    def __init__(self, url, ServiceKey,yyyy, pageNo):
        self.url = url  #URL
        self.ServiceKey = ServiceKey # SERVICEKEY
        self.yyyy = yyyy
        self.pageNo = pageNo

    # 던질 url 조합
    def setUrl(self):
        queryParams = '?' \
                      +urlencode({quote_plus('resultType'): 'JSON'  # 받는 타입
                                      , quote_plus('serviceKey'): self.ServiceKey
                                      , quote_plus('pageNo'): str(self.pageNo)
                                      , quote_plus('yyyy'): self.yyyy  # 측정소코드
                                      , quote_plus('numOfRows'): '999'  # 줄수
                                    })
        return self.url + unquote(queryParams)
