# -*- Encoding:utf-8 -*-


# WRI_14_VO
class VO :

    # 생성자
    def __init__(self, resultCode, resultMsg, flux, no, obsrdtmnt, wal, numOfRows, pageNo, totalCount):
        self.resultCode = resultCode
        self.resultMsg = resultMsg
        self.flux = flux
        self.no = no
        self.obsrdtmnt = obsrdtmnt
        self.wal = wal
        self.numOfRows = numOfRows
        self.pageNo = pageNo
        self.totalCount = totalCount

    def getRecord(self):
        rec = self.resultCode \
              +self.resultMsg \
              +self.numOfRows \
              +self.pageNo \
              +self.totalCount \
              +self.no \
              +self.obsrdtmnt \
              +self.flux \
              +self.wal
        return rec

