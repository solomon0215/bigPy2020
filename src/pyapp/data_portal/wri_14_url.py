#-*- Encoding:utf-8 -*-
import json
import urllib
from urllib.parse import urlencode, quote_plus, unquote


#WRI_14(수위 분강우량조회)를 테스트를 위한  클래스
#날짜만 args로 입력 나머지는 properties file
class WRI_14 :
    #URL,ServiceKey은 properties
    def __init__(self,url,ServiceKey,date,damcode,wal,pageNo):
        self.url = url
        self.date = date
        self.damcode = damcode
        self.wal = wal
        self.ServiceKey = ServiceKey
        self.pageNo = pageNo
    #던질 url 조합
    def setUrl(self):
        queryParams = '?' \
                      + urlencode({quote_plus('_type'): 'json'  # 받는 타입
                                      , quote_plus('tms'): '10'  # 조회 주기
                                      , quote_plus('ServiceKey'): self.ServiceKey
                                      , quote_plus('sdate'): self.date  # 조회시작 날짜
                                      , quote_plus('stime'): '00'  # 시작시간
                                      , quote_plus('edate'): self.date  # 조회종료 날짜
                                      , quote_plus('etime'): '23'  # 종료시간
                                      , quote_plus('damcode'): self.damcode  # 댐코드
                                      , quote_plus('wal'): self.wal  # 관측소코드
                                      , quote_plus('numOfRows'): '999'  # 줄수
                                      , quote_plus('pageNo'): str(self.pageNo)
                                    })
        return self.url + unquote(queryParams)



