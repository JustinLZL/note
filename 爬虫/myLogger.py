# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:51:08 2018

@author: Administrator
"""
import logging
import sys

class LoggerHelper:
    def __init__(self,name='LogHelper',setLevel=logging.DEBUG):
        self.logger = logging.getLogger(name)
        self.formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        self.file_handler = logging.FileHandler(name+".log")
        self.file_handler.setFormatter(self.formatter)
        
        self.console_handler = logging.StreamHandler(sys.stdout)
        self.console_handler.setFormatter(self.formatter)
        
        self.logger.setLevel(setLevel)
        
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.console_handler)        
        
    def writeLog(self,info,level='debug'):
        if level == "critial":
            self.logger.critical(info)
        elif level == "error":
            self.logger.error(info)
        else:
            self.logger.debug(info)
    
    def removeLog(self):
        self.logger.removeHandler(self.file_handler)
        self.logger.removeHandler(self.console_handler)
        
if __name__ == "__main__":
    logger = LoggerHelper()
    logger.writeLog("hello",level = 'error')
    logger.removeLog()