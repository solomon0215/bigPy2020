#-*- Encoding:utf-8 -*-
import collections
import os

from common.commonLog import Logs as logs

#File객체 관련 관리하는 공통 클래스
class DataFile:
    #경로
    def __init__(self,pathFile):
        self.pathFile = pathFile
        self.log = logs.logger

    #Json Record 출력
    def printRecord(self,list):
        #빈값이 아니라면
#         print(list)
        if list !=False :
            self.log.info('printRecord 메소드 실행')
            if os.path.isfile(self.pathFile) :
                f = open(self.pathFile,'a',encoding='utf-8')
            else :
                f = open(self.pathFile,'w',encoding='utf-8')
            i = 1
            for rec in list :
                f.write(rec)
                f.write('\n')
                i += 1
                step = str(i) + str('번 출력진행')
#                 self.log.info(step)
            f.close()
            self.log.info('출력완료')
        else :
            self.log.info('빈값 건너뛰기')

    #META 불러오기
    def getMeta(self,path : str):
        self.log
        meta = []
        f = open(path,'rt',encoding='utf-8')
        if isinstance(f,collections.Iterable) :
            for line in f :
                meta.append(line.replace('\n',''))
            f.close()
            return meta
        else :
            self.log.ERROR('메타 데이터가 비어있습니다.')
            exit(-1)