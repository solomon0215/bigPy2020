# -*- Encoding:utf-8 -*-
import json
import urllib
from urllib.parse import urlencode, quote_plus, unquote


# WALCODE URL 형성을 위한  클래스
# DAMCDOE ARGS로
class WALCODE_URL:
    # URL,ServiceKey은 properties damcode는 메타데이터
    def __init__(self, url, ServiceKey,damcode):
        self.url = url
        self.ServiceKey = ServiceKey
        self.damcode=damcode

    # 던질 url 조합
    def setUrl(self):
        queryParams = '?' \
                      + urlencode({quote_plus('_type'): 'json'  # 받는 타입
                                    , quote_plus('ServiceKey'): self.ServiceKey  # SERVICE KEY
                                    , quote_plus('damcode'): self.damcode  # damcode
                                    })
        return self.url + unquote(queryParams)