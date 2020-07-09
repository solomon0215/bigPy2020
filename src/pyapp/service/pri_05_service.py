'''
Created on 2020. 7. 3.

@author: 서민재
'''
# -*- Encoding:utf-8 -*-

from common.commonVO import VO
from common.commonConfig import config 
import json
import types

from common.commonLog import Logs as logs
from common.commonRequest import apiRequest as Request
from data_portal.pri_05_url import PRI_05 

class pri05Service :
    def __init__(self, ptNoList,wmyrList,wmodList,log):
        self.ptNoList = ptNoList
        self.wmyrList = wmyrList
        self.wmodList = wmodList
        self.pageNo = 1
        self.log = logs.logger
    
    def querySer(self):
        j_list = []
        # property 가져오는 공통 클래스
        cfig = config('PRI','PRI_05_URL', 'PRI_SERVICEKEY')
        #query 조합하는 클래스
        query = PRI_05(cfig.reUrl(), cfig.reSerKey(), self.ptNoList, self.wmyrList, self.wmodList, self.pageNo).setUrl()
        try :
            re = Request(query)
            res = re.doReq()
        except Exception as ex :
            self.log.error('쿼리 전송중 에러발생')
            return False
        else :
            j_list.append(res)
        if str(res['getWaterMeasuringListMavg']['header']['code']) == '00' :
            # 현재 페이지 * 설정한 row수가 전체 카운트 보다 낮다면
            pageNo = int(res['getWaterMeasuringListMavg']['pageNo'])
            totalCount = int(res['getWaterMeasuringListMavg']['totalCount'])
            numOfRows = int(res['getWaterMeasuringListMavg']['numOfRows'])
            pageCount = int((totalCount/numOfRows) + 1)
            if pageCount > 1 :
                for i in range(2,pageCount) :
                    self.log.info('페이지 다수 작업 실시')
                    pageNo += 1
                    query = PRI_05(cfig.reUrl(), cfig.reSerKey(), self.ptNoList, self.wmyrList, self.wmodList, pageNo).setUrl()
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
                print('단일 페이지 ')
                return j_list            
        else :
            self.log.info('서버 비정상 응답 재시도 ')
            return False                    
    
    #받은 Json 프린트
    def listSer(self,j_list):    
        self.log.info(str(types.BuiltinMethodType.__name__))
        print('list ser')
        #서버가 비정상 응답이 아닌지 확인
        if j_list != False :
            print('not False')
            for j_res in j_list :
                print('service work')
                res = j_res
                # record를 담을 list형
                rec = []
                # 구분자
                deli = '|^'
                # Header
                resultCode = str(res['getWaterMeasuringListMavg']['header']['code']) + deli
                resultMsg = str(res['getWaterMeasuringListMavg']['header']['message']) + deli
                # 정산반환 확인
                if str(res['getWaterMeasuringListMavg']['header']['code'])== '00':
                    print('정상응답')
                    rows = str(res['getWaterMeasuringListMavg']['rows']) + deli
                    numOfRows = str(res['getWaterMeasuringListMavg']['numOfRows']) + deli
                    pageNo = str(res['getWaterMeasuringListMavg']['pageNo'])    + deli
                    totalCount = str(res['getWaterMeasuringListMavg']['totalCount'])
                    # 값이 있다면 items 는 dict
                    if type( res['getWaterMeasuringListMavg']['item']) is list :
                        print('item 리스트 타입')
                        values = ""
                        if len(res['getWaterMeasuringListMavg']['item']) != 0 :
                            for i in res['getWaterMeasuringListMavg']['item'] :
                                for key,val in i.items() :
                                    if str(val) =='null' : 
                                        values += (' ' + deli)
                                    else : 
                                        values += (str(val) + deli)    
                                rec.append(VO(resultCode,resultMsg,values,rows,numOfRows,pageNo,totalCount).getRec())
                                return rec
                        else :
                            return False
                    elif  type( res['getWaterMeasuringListMavg']['item']) is str :
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
                
        