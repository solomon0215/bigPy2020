# -*- Encoding:utf-8 -*-

import configparser
import json
import sys

from VO.damcode import VO as vo
from common.commonLog import Logs as logs
from common.commonRequest import apiRequest as Request
from data_portal.damcode_url import DAMCODE_URL


# wri_14_json_vo Class
class damcodeService:
    def __init__(self, ):
        print('클래스생성 ')
        self.log = logs.logger
    # Requset 날리고 결과 json 받아오기
    def querySer(self):
        self.log.info('querySer 메소드')
        # property 가져오기
        section = 'DAMCODE'
        config = configparser.ConfigParser(interpolation=None)
        config.read('..\conf\openApi.properties')
        url = config.get(section, 'DAMCODE_URL')
        serviceKey = config.get(section, 'DAMCODE_SERVICEKEY')
        # 인자 순서 : url,ServiceKey,date,damcode,wal
        # 실제 던질 쿼리
        query = DAMCODE_URL(url, serviceKey).setUrl()
        re = Request(query)
        self.log.info('json 반환 시작')
        return re.doReq()

    # json을 record 형식으로 바꾸는 service
    def listSer(self, j_res):
        self.log.info('listSer')
        res = j_res
        # record를 담을 list형
        rec = []
        # 구분자
        deli = '|^'
        # Header
        resultCode = str(res['response']['header']['resultCode'])
        resultMsg = str(res['response']['header']['resultMsg'])
        if resultCode != '99' :
            item =  res['response']['body']['items']['item']
            for i in item :
                damcode = str(i['damcode'])
                damnm = str(i['damnm'])
                rec.append(vo(damcode,damnm).damcodeMeta())
            return rec
        else :
            self.log.error('서버 비정상 응답 코드')
            self.log.error(resultCode)
            self.log.error(resultMsg)
            exit(-1)
