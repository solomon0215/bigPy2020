# -*- Encoding:utf-8 -*-
# DAMCODE VO Class

class VO:
    # field 정의 생성자
    def __init__(self, damcode, damnm):
        self.damcode = damcode
        self.damnm = damnm

    #댐코드 메타
    def damcodeMeta(self):
        return self.damcode