# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 22:02:04 2021

@author: Administrator
"""
#%% 导入模块
import re
import numpy as np
import pandas as pd

#%% 类
class GTsolver():
    
    #初始化
    def __init__(self, RLT_File, File_index, Num_Case):
        self.RLT_File = RLT_File
        self.File_index = File_index
        self.Num_Case = Num_Case
        
    #读取GT结果文件，返回文件中的所有数据    
    def RLT_Data_Read(self):
        f = open(self.RLT_File)
        Char_Data = f.read()
        newStr = Char_Data.split('\n')
        a = []
        for i in range(len(newStr)):
            temp = re.split('"|,', newStr[i])
            for j in temp:
                if len(j) != 0:
                    a.append(j)
        RLT_Data = list(np.array(a).reshape(-1,4))
        RLT_Data.append([[],[],[],[]])
        return pd.DataFrame(RLT_Data)
    
    #读取准备提取的参数
    def Param_Result_Extraction(self):
        Param_Cell = []
        with open(self.File_index) as f:
            while True:
                line = f.readline()
                if not line: break
                templine = re.split(',|\n',line)
                if templine[-1] == '':
                    templine.pop()
                Param_Cell.append(templine)
        return pd.DataFrame(Param_Cell)
    
    #按提取参数从GT结果文件中提取数据
    def RLT_Result_Extraction(self):
    
        RLT_Data = self.RLT_Data_Read()
        Param_Cell = self.Param_Result_Extraction()
        
        part_name_cor = Param_Cell.iloc[:, 0]
        param_name_cor = Param_Cell.iloc[:, 1]
        
        part_name = RLT_Data.iloc[:,0]
        param_name = RLT_Data.iloc[:,1]
        case_name = RLT_Data.iloc[:,2]
        data_name = RLT_Data.iloc[:,3]
        
        Result_Data_Cell = np.zeros((len(Param_Cell), self.Num_Case))
        for i in range(self.Num_Case):
            for j in range(len(part_name_cor)):
                Result_Data_Cell[j ,i] = float(data_name[(part_name_cor[j] == part_name) & (param_name_cor[j] == param_name) & (str(i+1) == case_name)])
        return Result_Data_Cell
    
    Result_Data_Cell = RLT_Result_Extraction