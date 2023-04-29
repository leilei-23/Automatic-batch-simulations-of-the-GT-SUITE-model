# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 22:25:53 2021

@author: Administrator
"""
import os

class GTdriver():
    
    #初始化
    def __init__(self, dat_file, solver_version):
        self.dat_file = dat_file
        self.solver_version = solver_version
    
    #驱动程序
    def drive(self):
        cmd = 'GTpower -v' + self.solver_version + ' -r:on ' + self.dat_file
        os.system(cmd)
    drive