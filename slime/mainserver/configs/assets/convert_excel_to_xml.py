#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#========================================================================
#     Author: Leon
#      Email: yanglianglee@gmail.com
# LastChange: 2012-11-13 21:03:22
#========================================================================

from openpyxl import load_workbook
import os

def trans(header, line):
    """ 
    @param header 表头格式
    @param line 一行记录，是一个列表
    @return  把每一行对应表头转换为指定的格式
    """
    record = ['<RECORD']
    for key, value in zip(header, line):
        word = '%s="%s"' % (key, value)
        record.append(word)
    record.append('>')
    record.append('</RECORD>\n')
    return ' '.join(record)


def output(filepath, header, content):
    with open(filepath, 'w') as f:
        f.write('<?xml version="1.0" standalone="yes"?>\n')
        f.write("<RECORDS>\n")
        for line in content:
            f.write(trans(header, line))
        f.write("</RECORDS>")


def get_content(filename):
    print 'xlsx file name:', filename

    wb = load_workbook(filename=filename)
    for sheet_name in wb.get_sheet_names():
        sheet = wb.get_sheet_by_name(sheet_name)
        break
    rows = sheet.rows

    # 读取表头
    header = [col.value for col in rows[1]]
    
    # 读取所有行数据
    content = []
    for row in rows[3:]:
        line = [col.value if col.value else '' for col in row]
        content.append(line)
    
    return header, content

def convert(filename):
    # 获取表头和数据
    header, content = get_content(filename)
    # 写出到 xml 文件
    output_file = filename.split(".")[0]+".xml"
    print output_file
    output(output_file, header, content)
    
    
if __name__ == '__main__':
    dir_path = os.getcwd()
    for filename in os.listdir(dir_path):
        print filename
        if filename.endswith('.xlsx'):
            convert(filename)
