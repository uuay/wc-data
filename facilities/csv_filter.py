#!/usr/bin/env python3
import pandas as pd
import sys

def isResidentCenter(target):
    firstChar = target.str.slice(0, 1)
    return firstChar.str.isdigit()

def isExtractTarget(target):
    isHealth = (target.str.slice(0, 2) == '보건')
    isWelfareCenter = (target.str.slice(0, 3) == '지자체')
    isLibrary = (target.str == '도서관')
    isFireSchool = (target.str == '소방_소방학교')

    return isHealth | isWelfareCenter | isLibrary | isFireSchool | isResidentCenter(target)

input_file = sys.argv[1]
output_file = sys.argv[2]
print('input csv file...')
data_frame = pd.read_csv(input_file, engine='python')

print('start filtering...')
data_frame_value_meets_condition = data_frame.loc[isExtractTarget(data_frame['유형_2']), :]

print('output csv file...')
data_frame_value_meets_condition.to_csv(output_file, index=False, encoding='euc-kr')

print('done')