from langconv import *
import sys

print(sys.version)
print(sys.version_info)

# 转换繁体到简体
def cht_to_chs(line):
    line = Converter('zh-hans').convert(line)
    line.encode('utf-8')
    return line

# 转换简体到繁体
def chs_to_cht(line):
    line = Converter('zh-hant').convert(line)
    line.encode('utf-8')
    return line

# line_chs='<>123asdasd把中文字符串进行繁体和简体中文的转换'
# line_cht='<>123asdasd把中文字符串進行繁體和簡體中文的轉換'

# ret_chs = "%s\n"%cht_to_chs(line_cht)
# ret_cht = "%s\n"%chs_to_cht(line_chs)



print("start")


#用UTF8打开
file = open('zh_CN.js','r',encoding='utf-8')

ret_cht = ""
while True:
    line = file.readline()  # 整行读取数据
    if not line:
        # print("break")
        break
    print(line)
    ret_cht += chs_to_cht(line)

#打印到调试窗体
print(ret_cht)

file.close()

wf = open('zh_TW.js','w',encoding='utf-8')
wf.write(ret_cht)
wf.close()

print("end")