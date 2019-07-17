import time
import os,shutil
import re
import sys

#***获取当前目录***
current_file_path = os.path.abspath(os.path.dirname(__file__))
print(current_file_path)

#***获取上级目录***
parent_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
print(parent_dir)

#***output目录***
output_path = parent_dir + '/Output/'

tool_name = 'iOS_system_framework_sqllitte.py'
tool_py_path = current_file_path + '/'  + tool_name

def mg_copyfile(srcfile,dstfile):
    isExists=os.path.exists(srcfile)
    if not isExists:
        os.makedirs(srcfile)
    
    if not os.path.isfile(srcfile):
        print("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile,dstfile)      #复制文件
        print("copy %s -> %s"%( srcfile,dstfile))

"""
利用递归实现目录的遍历
@para sourcePath:原文件目录
@para targetPath:目标文件目录
"""
def getDirAndCopyFile(sourcePath,targetPath):
 
  if not os.path.exists(sourcePath):
    return
  if not os.path.exists(targetPath):
    os.makedirs(targetPath)
     
  #遍历文件夹
  for fileName in os.listdir(sourcePath):
    #拼接原文件或者文件夹的绝对路径
    absourcePath = os.path.join(sourcePath, fileName)
    #拼接目标文件或者文件加的绝对路径
    abstargetPath = os.path.join(targetPath, fileName)
    #判断原文件的绝对路径是目录还是文件
    if os.path.isdir(absourcePath):
      #是目录就创建相应的目标目录
      os.makedirs(abstargetPath)
      #递归调用getDirAndCopyFile()函数
      getDirAndCopyFile(absourcePath,abstargetPath)
    #是文件就进行复制
    if os.path.isfile(absourcePath):
      rbf = open(absourcePath,"rb")
      wbf = open(abstargetPath,"wb")
      while True:
        content = rbf.readline(1024*1024)
        if len(content)==0:
          break
        wbf.write(content)
        wbf.flush()
      rbf.close()
      wbf.close()


if __name__ == "__main__":
 
  walk_path=parent_dir+'/Frameworks/'
  print(walk_path)

  for root,dirs,files in os.walk(walk_path):
    for name in dirs:
      name_path = os.path.join(root,name)

      name_no_ext = name.replace('.framework','')
      name_out_path_dir = output_path + '/' + name_no_ext

      name_out_path = name_out_path_dir + '/' + name 

      isExists=os.path.exists(name_out_path_dir)
      if not isExists:
        os.makedirs(name_out_path_dir)
      
      tool_to_path = name_out_path_dir + '/' + tool_name
      getDirAndCopyFile(name_path,name_out_path)
      mg_copyfile(tool_py_path,tool_to_path)







