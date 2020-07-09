'''
Created on 2020. 7. 6.

@author: solom
'''

class VO:
    '''
    Common VO Class 
    '''


    def __init__(self, *args : str):
        '''
        args로 받은 인자 값들을각각 의  필드로 저장
        '''
        self.list = []
        for i in args :
            self.list.append(i)
        
    
    def getRec(self):
        rec = '' 
        for i in self.list :
            rec += i
        return rec    
    
    