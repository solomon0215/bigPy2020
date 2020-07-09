# -*- Encoding:utf-8 -*-


import sys, time, os

from common.CommonFile import DataFile as File
from service.damcode_service import damcodeService
from service.walcode_service import walcodeService
from service.wri_14_service import wri14Service
from common.commonLog import Logs


# main 실행
print(__name__)
if __name__ == '__main__':
    log = Logs.logger
    #시작 시간
    start = time.time()
    
    link_id = sys.argv[1]
    #WRI_14 크로울링 실행
    if link_id == 'BP-IF_WRI_14':
        f = File(sys.argv[2])
        # META DATA 받아오기
        path = '..\..\meta\WALCODE.dat'
        meta = f.getMeta(path)
        for val in meta :
            param = val.split('|^')
            print(param)
            # 던지고 json받아오기 인자값 url
            wriSer = wri14Service(param[0],param[1],'2020-06-30',log)
            # 파일 쓰기 클래스 인자값 파일네임(경로 포함), 출력메소드
            res =  wriSer.querySer()
            if res == False :
                i = 1
                while True : 
                    res =  wriSer.querySer()
                    if res != False :
                        break 
                    elif i == 6 :
                        break
                    i += 1
            f.printRecord(wriSer.listSer(res))
    #댐코드 메타 만들기 작업
    elif link_id == 'damcode' :
        if len(sys.argv) == 3 :
            # 던지고 json받아오기 인자값 url
            damSer = damcodeService()
            # 파일 쓰기 클래스 인자값 파일네임(경로 포함), 출력메소드
            File(sys.argv[2]).printRecord(damSer.listSer(damSer.querySer()))
        else:
            log.info('파라미터 갯수 에러')
            exit(-1)
    # 수위 관측소 코드 메타 만들기 작업
    elif link_id == 'walcode':
        if len(sys.argv) == 3 :
            f=File(sys.argv[2])
            #META DATA 받아오기
            path ='..\..\meta\DAMCODE.dat'
            meta = f.getMeta(path)
            for damcode in meta :
                # 던지고 json받아오기 인자값 url
                walSer = walcodeService(damcode)
                # 파일 쓰기 클래스 인자값 파일네임(경로 포함), 출력메소드
                f.printRecord(walSer.listSer(walSer.querySer()))
        else :
            log.error('파라미터 갯수 에러')
            exit(-1)
    end = time.time()
    print(end - start,'초')