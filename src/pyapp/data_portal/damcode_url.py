# -*- Encoding:utf-8 -*-
import json
import urllib
from urllib.parse import urlencode, quote_plus, unquote


# DAMCODE URL 형성을 위한  클래스
# 날짜만 args로 입력 나머지는 properties file
class DAMCODE_URL:
    # URL,ServiceKey은 properties
    def __init__(self, url, ServiceKey):
        self.url = url
        self.ServiceKey = ServiceKey

    # 던질 url 조합
    def setUrl(self):
        queryParams = '?' \
                      + urlencode({quote_plus('_type'): 'json'  # 받는 타입
                                    , quote_plus('ServiceKey'): self.ServiceKey  # SERVICE KEY
                                   })
        return self.url + unquote(queryParams)