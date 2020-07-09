# -*- Encoding:utf-8 -*-
from fileinput import filename
import logging
import logging.handlers
import time
from types import *
import types


#===============================================================================
# Logs : 로그를 작성하기 위한 클래스
#===============================================================================
class Logs :
    # logging 인스턴스
    toda = time.strftime('%Y%m%d%H', time.localtime(time.time()))
    fileN = '..\..\logs\logs_'+str(toda)+'.dat'
    logging.basicConfig(filename = fileN \
                            ,level=logging.INFO \
                            ,format='[%(asctime)s][%(levelname)s][%(filename)s:%(lineno)s] >> %(message)s)'
                            )
    logger = logging.getLogger()
if __name__ == '__main__' :
    log=Logs.logger
    log.info('test')
