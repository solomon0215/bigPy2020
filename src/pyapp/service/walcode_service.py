# -*- Encoding:utf-8 -*-

import configparser
import json
import sys

from VO.walcode import VO as vo
from common.commonLog import Logs as logs
from common.commonRequest import apiRequest as Request
from data_portal.walcode_url import WALCODE_URL


# wri_14_json_vo Class
class walcodeService:

    def __init__(self, damcode):
        logs().info('walcodeService 클래스 생성')
        self.damcode = damcode

    # Requset 날리고 결과 json 받아오기
    def querySer(self):
        logs().method('querySer 메소드')
        # property 가져오기
        section = 'WALCODE'
        config = configparser.ConfigParser(interpolation=None)
        config.read('..\conf\openApi.properties')
        url = config.get(section, 'WALCODE_URL')
        serviceKey = config.get(section, 'WALCODE_SERVICEKEY')
        # 인자 순서 : url,ServiceKey,date,damcode,wal
        # 실제 던질 쿼리
        query = WALCODE_URL(url, serviceKey, self.damcode).setUrl()
        re = Request(query)
        logs().info('json 반환 시작')
        return re.doReq()

    # json을 record 형식으로 바꾸는 service
    def listSer(self, j_res):
        logs().method('listSer')
        print(json.dumps(j_res, indent=4))
        res = j_res
        # record를 담을 list형
        rec = []
        # 구분자
        deli = '|^'
        # Header
        resultCode = str(res['response']['header']['resultCode'])
        resultMsg = str(res['response']['header']['resultMsg'])
        print(type(res['response']['body']['items']))
        # 비정상인지 확인
        if resultCode != '99' :
            # items가 dict인지 타입인지 확인 빈값 str
            if type(res['response']['body']['items']) is dict :
                # 값이 하나가 아니어서 list인경우
                if type(res['response']['body']['items']['item']) is list :
                    item = res['response']['body']['items']['item']
                    for i in item :
                        walobsrvtcode = str(i['walobsrvtcode'])
                        obsrvtNm = str(i['obsrvtNm'])
                        rec.append(vo(self.damcode, walobsrvtcode, obsrvtNm).walcodeMeta())
                    return rec
                # 값이 하나여서 DICT인경우
                elif type(res['response']['body']['items']['item']) is dict :
                    walobsrvtcode = str(res['response']['body']['items']['item']['walobsrvtcode'])
                    obsrvtNm = str(res['response']['body']['items']['item']['walobsrvtcode'])
                    rec.append(vo(self.damcode, walobsrvtcode, obsrvtNm).walcodeMeta())
                    return rec
            # str타입인지 확인
            elif  type(res['response']['body']['items']) is str :
                logs().info('빈 값 발생 다음으로 넘기기')
                return False
        else :
            logs().ERROR('서버 비정상 응답 코드')
            logs().ERROR(resultCode)
            logs().ERROR(resultMsg)
            exit(-1)
