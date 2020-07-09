# -*- Encoding:utf-8 -*-

import configparser
import json
import types

from VO.WRI_14 import VO as vo
from common.commonLog import Logs as logs
from common.commonRequest import apiRequest as Request
from data_portal.wri_14_url import WRI_14

# wri_14_json_vo Class
class wri14Service:
    def __init__(self, damcode, walcode, date,log):
        self.damcode = damcode
        self.walcode = walcode
        self.date = date
        self.pageNo = 1
        self.log = logs.logger
    # Requset 날리고 결과 json 받아오기
    # page가 여러경우가 발생
    def querySer(self):
        self.log.info(types.BuiltinMethodType.__name__)
        # property 가져오기
        j_list = []
        section = 'WRI_14'
        config = configparser.ConfigParser(interpolation=None)
        config.read('..\conf\openApi.properties')
        url = config.get(section, 'WRI_14_URL')
        serviceKey = config.get(section, 'WRI_14_SERVICEKEY')
        # 인자 순서 : url,ServiceKey,date,damcode,wal
        # 실제 던질 쿼리
        query = WRI_14(url, serviceKey, self.date, self.damcode, self.walcode, self.pageNo).setUrl()
        try :
            re = Request(query)
            res = re.doReq()
        except Exception as ex :
            self.log.error('쿼리 전송중 에러발생')
            return False
        else :
            self.log.info(res)
            j_list.append(res)
        # page숫자를 파악하기 위한 단계
        if str(res['response']['header']['resultCode']) == '00':
            self.log.info(str(res['response']['body']['totalCount']))
            if type(res['response']['body']['items']) is dict :
                if type(res['response']['body']['items']['item']) is list :
                    # 현재 페이지 * 설정한 row수가 전체 카운트 보다 낮다면
                    pageNo = int(res['response']['body']['pageNo'])
                    totalCount = int(res['response']['body']['totalCount'])
                    numOfRows = int(res['response']['body']['numOfRows'])
                    pageCount = int((totalCount/numOfRows) + 1)
                    if  pageCount > 1 :
                        for i in range(2,pageCount) :
                            self.log.info('페이지 다수 작업 실시')
                            pageNo += 1
                            query = WRI_14(url, serviceKey, self.date, self.damcode, self.walcode, pageNo).setUrl()
                            try :
                                re = Request(query)
                                res = re.doReq()
                            except Exception as ex :
                                self.log.error('쿼리 전송중 에러발생')
                                continue 
                            else : 
                                self.log.info(res)       
                                j_list.append(res)
            else : 
                self.log.info('빈값 재시도')
                self.log.info(str(j_list))
                return False                    
        self.log.info('json 반환 시작') 
        return j_list

    # json을 record 형식으로 바꾸는 service
    def listSer(self, j_list):
        self.log.info(str(types.BuiltinMethodType.__name__))
        #서버가 비정상 응답이 아닌지 확인
        if j_list != False :
            for j_res in j_list :
                res = j_res
                # record를 담을 list형
                rec = []
                # 구분자
                deli = '|^'
                # Header
                resultCode = str(res['response']['header']['resultCode']) + deli
                resultMsg = str(res['response']['header']['resultMsg']) + deli
                # 정산반환 확인
                if str(res['response']['header']['resultCode']) == '00':
                    # 값이 있다면 items 는 dict
                    if type(res['response']['body']['items']) is dict :
                        # 값이 여러개면 item은 list
                        if type(res['response']['body']['items']['item']) is list :
                            # body
                            item = res['response']['body']['items']['item']
                            numOfRows = str(res['response']['body']['numOfRows']) + deli
                            pageNo = str(res['response']['body']['pageNo']) + deli
                            totalCount = str(res['response']['body']['totalCount'])
                            self.log.info('msg')
                            self.log.info(str(totalCount))
                            for i in item:
                                # 해당값이 없는경우
                                if 'flux' in i : flux = str(i['flux']) + deli
                                else : flux = ' ' + deli
                                if 'no' in i : no = str(i['no']) + deli
                                else : no = ' ' + deli
                                if 'obsrdtmnt' in i : obsrdtmnt = str(i['obsrdtmnt']) + deli
                                else : obsrdtmnt = ' ' + deli
                                if 'wal' in i : wal = str(i['wal']) + deli
                                else : wal = ' ' + deli
                                rec.append(vo(resultCode, resultMsg, flux, no, obsrdtmnt, wal, numOfRows, pageNo, totalCount).getRecord())
                            return rec
                        # 값이 하나여서 DICT인경우
                        elif type(res['response']['body']['items']['item']) is dict:
                            numOfRows = str(res['response']['body']['numOfRows']) + deli
                            pageNo = str(res['response']['body']['pageNo']) + deli
                            flux = str(res['response']['body']['items']['item']['flux']) + deli
                            no = str(res['response']['body']['items']['item']['no'])
                            obsrdtmnt = str(res['response']['body']['items']['item']['obsrdtmnt']) + deli
                            wal = str(res['response']['body']['items']['item']['wal']) + deli
                            totalCount = str(res['response']['body']['totalCount'])
                            rec.append(vo(resultCode, resultMsg, flux, no, obsrdtmnt, wal, numOfRows, pageNo, totalCount).getRecord())
                            return rec
                    # 빈값이면 str
                    elif  type(res['response']['body']['items']) is str :
                        print(json.dumps(res, indent=3))
                        self.log.info('빈 값 발생 다음으로 넘기기')
                        return False
                else :
                    self.log.error('비정상 서버 응답')
                    exit(-1)
        else :
            self.log.error('서버 비정상 응답으로 다음 작업넘어가기')
            self.log.info(str(j_list))
            return False
                