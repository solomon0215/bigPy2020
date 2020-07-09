# -*- Encoding:utf-8 -*-
# WALCODE VO Class
from common.commonLog import Logs as logs


class VO:

    # field 정의 생성자
    def __init__(self, damcode, walobsrvtcode, obsrvtNm):
        logs().info('walcodeVO 클래스 생성')
        self.damcode = damcode
        self.obsrvtNm = obsrvtNm
        self.walobsrvtcode = walobsrvtcode

    # 수위관측소코드 메타
    def walcodeMeta(self):
        logs().method('walcodeMeta 메소드')
        meta = self.damcode + '|^' + self.walobsrvtcode
        print(meta)
        return meta
