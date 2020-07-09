'''
Created on 2020. 7. 6.

@author: 서민재
'''
# -*- Encoding:utf-8 -*-
import sys, time, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from common.CommonFile import DataFile as File
from service.wrs_02_service import  wrs02Ser
from common.commonLog import Logs


if __name__ == '__main__' :
    start = time.time()
    link_id = sys.argv[1]
    log = Logs.logger
    if link_id == 'BP-IF_WRS_02' :
        print(link_id)
        f = File(sys.argv[2])
        for i in range(1,5) :
            w02Ser = wrs02Ser(str(i), log)
            res = w02Ser.querySer()
            if res != False :
#                 print('정상응답')
                rec = w02Ser.listSer(res)
                if rec != False :
                    f.printRecord(rec)
                else :
                    print('빈값')
            else : 
                print('비정상 응답')    
    elif link_id == 'BP-IF_WRS_06' :    
        f = File(sys.argv[2])
        for i in range(1,5) :
            w02Ser = wrs02Ser(str(i), log)
            res = w02Ser.querySer()
            if res != False :
                print('정상응답')
                rec = w02Ser.listSer(res)
                if rec != False :
                    f.printRecord(rec)
                else :
                    print('빈값')
            else : 
                print('비정상 응답')    

    end = time.time()
    print(end-start)    