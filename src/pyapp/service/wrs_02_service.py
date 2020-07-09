'''
Created on 2020. 7. 6.

@author: solom
'''
# -*- Encoding:utf-8 -*-
import json
import types

from common.commonConfig import config 
from common.commonLog import Logs as logs
from common.commonRequest import apiRequest as Request
from common.commonVO import VO
from data_portal.wrs_02_url import WRS_02   


class wrs02Ser :
    def __init__(self, divCode,log):
        self.divCode = divCode
        self.log = logs.logger
    
    def querySer(self):
        j_list = []
        # property 가져오는 공통 클래스
        cfig = config('WRS_02','waterFlux_fcltyList_url', 'waterFlux_service_key')
        #query 조합하는 클래스
        query = WRS_02(cfig.reUrl(), cfig.reSerKey(), self.divCode).setUrl()
        print('쿼리날리기')
        try :
            re = Request(query)
            res = re.doReq()
        except Exception as ex :
            self.log.error('쿼리 전송중 에러발생')
            return False
        else :
            print(json.dumps(res,indent=4))
            j_list.append(res)
            return j_list
            
    #받은 Json 프린트
    def listSer(self,j_list):    
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
                if str(res['response']['header']['resultCode'])== '00':
#                     print('정상응답')
                    # 값이 있다면 items 는 dict
                    if type(res['response']['body']['items']['item']) is list :
#                         print('item 리스트 타입')
                        if len(res['response']['body']['items']['item']) != 0 :
                            for i in res['response']['body']['items']['item'] :
                                print('list 출력 :     ',i)
                                values = ""
                                values += str(i['fcltyMngNm']) + deli
                                values += str(i['sujCode'])
                                print(values)
                                rec.append(VO(resultCode,resultMsg,values).getRec())
                            return rec
                        else :
                            return False
                    elif  type( res['response']['body']['items']['item']) is str :
                        print(res)
                        self.log.info('빈값건너 뛰기')
                        return False
                else :
                    self.log.error('비정상 서버 응답')
                    exit(-1)
        else :
            self.log.error('서버 비정상 응답으로 다음 작업넘어가기')
            self.log.info(str(j_list))
            return False
 