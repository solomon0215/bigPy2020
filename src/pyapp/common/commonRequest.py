#-*- Encoding:utf-8 -*-
import json, urllib
from urllib.request import urlopen

from common.commonLog import Logs as logs

#Request 공통 클래스 결과를 json객체를 dict로
class apiRequest :
    def __init__(self,url):
        self.log=logs.logger
        print('apiRequest 클래스 생성')
        self.url = url
        print('실행 URL : ' , self.url)
    def doReq(self):
        self.log.info('doReq 메소드 실행')
        request = urllib.request.Request(self.url)
        # url 실행 후 결과 읽기
        res = urlopen(request).read()
        j_res = json.loads(res.decode('utf-8'))
        return j_res