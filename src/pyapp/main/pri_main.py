'''
Created on 2020. 7. 3.

@author: 서민재
'''
# -*- Encoding:utf-8 -*-
import json
import sys, time, os
from urllib.request import urlopen
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.CommonFile import DataFile as File
from common.commonLog import Logs
from service.pri_02_service import pri02Service
from service.pri_05_service import pri05Service



if __name__ == '__main__':
    strtime = time.time()
    toda = time.strftime('%Y%m%d', time.localtime(time.time()))
    log = Logs.logger
    link_id = sys.argv[1]
    if link_id == 'BP-IF_PRI_05' :
        emty = 0
        err = 0
        f = File(sys.argv[2])
        # META DATA 받아오기
        path = '..\..\meta\PRI06OFFLINE.dat'
        meta = f.getMeta(path)
        
        #쿼리 던지기
        for val in meta :
            cheak = []
            mets = time.time() 
            p5Ser = pri05Service(val, '2017', '11', log)
            res =p5Ser.querySer()
            #비정상 응답
            if res is False :
                err += 1
            #정상응답    
            else :     
                rec = p5Ser.listSer(res)
                #빈값
                if rec is False :
                    emty += 1
                #정상값    
                else :      
                    f.printRecord(rec)
                    del rec
            mete = time.time()
            str1 = val + '\t' + str(mete-mets)
            cheak.append(str1)
            fNm = '..\..\cheak\PRI_05_TEST_'+toda+'.dat'
            da = File(fNm)
            da.printRecord(cheak)                 
        print('비정상 응답     : ', err)
        print('빈값     : ', emty)
    elif link_id == 'BP-IF_PRI_02' :
        emty = 0
        err = 0
        f = File(sys.argv[2])
        
        #쿼리 던지기
        mets = time.time() 
        p2Ser = pri02Service('2018',log)
        res =p2Ser.querySer()
#         print(res)
        #비정상 응답
        if res is False :
            err += 1
        #정상응답    
        else :     
            rec = p2Ser.listSer(res)
            #빈값
            if rec is False :
                emty += 1
            #정상값    
            else :      
                f.printRecord(rec)
                del rec
        if p2Ser.getPageNo() > 1 :
            while True :
                if p2Ser.getPageNo() == 0 :
                    break
                res =p2Ser.querySer()
                #비정상 응답
                if res is False :
                    err += 1
                #정상응답    
                else :     
                    rec = p2Ser.listSer(res)
                    #빈값
                    if rec is False :
                        emty += 1
                    #정상값    
                    else :      
                        f.printRecord(rec)
                        del rec        
        mete = time.time()
        str1 = str(mete-mets)
        fNm = '..\..\cheak\PRI_02_TEST_'+toda+'.dat'
        da = File(fNm)
        da.printRecord(str1)                 
        print('비정상 응답     : ', err)
        print('빈값     : ', emty)        
    endtime = time.time()    
    print('소요시간     :    ',(endtime-strtime),'초')    
    
    