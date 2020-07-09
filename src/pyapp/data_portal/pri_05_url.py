# -*- Encoding:utf-8 -*-
import json
import urllib
from urllib.parse import urlencode, quote_plus, unquote


# WRI_14(수위 분강우량조회)를 테스트를 위한  클래스
# 날짜만 args로 입력 나머지는 properties file
class PRI_05 :

    # URL,ServiceKey은 properties
    def __init__(self, url, ServiceKey,ptNoList,wmyrList,wmodList, pageNo):
        self.url = url  #URL
        self.ServiceKey = ServiceKey # SERVICEKEY
        self.ptNoList = ptNoList    #측정소 코드
        self.wmyrList = wmyrList    #측정년도
        self.wmodList = wmodList    #측정월
        self.pageNo = pageNo

    # 던질 url 조합
    def setUrl(self):
        queryParams = '?' \
                      +urlencode({quote_plus('resultType'): 'JSON'  # 받는 타입
                                      , quote_plus('serviceKey'): self.ServiceKey
                                      , quote_plus('pageNo'): str(self.pageNo)
                                      , quote_plus('ptNoList'): self.ptNoList  # 측정소코드
                                      , quote_plus('wmyrList'): self.wmyrList  # 측정년도
                                      , quote_plus('wmodList'): self.wmodList  # 측정월
                                      , quote_plus('numOfRows'): '999'  # 줄수
                                    })
        return self.url + unquote(queryParams)

