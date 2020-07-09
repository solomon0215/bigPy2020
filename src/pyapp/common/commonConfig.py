'''
Created on 2020. 7. 6.

@author: solom
'''
import configparser

class config :
    '''
    configparser 공통 클래스
    '''

    
    def __init__(self,section,url,serKey):
        '''
        class 생성자  section 명  url 명  servicekey 명을 받는다.
        '''
        self.config = configparser.ConfigParser(interpolation=None)
        self.section = section
        self.url = url
        self.serKey = serKey
    
    # url return 메소드    
    def reUrl(self):    
        self.config.read('..\conf\openApi.properties',encoding='utf-8')
        url = self.config.get(self.section, self.url)
        return url 
    # service key return 메소드    
    def reSerKey(self):
        self.config.read('..\conf\openApi.properties',encoding='utf-8')   
        serviceKey = self.config.get(self.section, self.serKey)
        return serviceKey