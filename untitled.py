#coding:utf-8

#!/usr/bin/python
from random import randint
from time import ctime
import os,sys



#将大的文件分成多个小的文件，inputfile 为书输入的文件， splitNumbers为分割的个数	
def splitFile(inputFile, splitNumbers):
	print "begin to split files........"
	file_handler = open(inputFile, 'r+')
	for IP in file_handler:
		IPtest = IP.strip()    #去掉IP地址后面的‘\n’
		
		hashvalue = hash(IPtest) %splitNumbers
		file_path = "./splitfile" + "/" + str(hashvalue) + ".txt"
		if mkFile(file_path):
			
			filePoint = open(file_path, "a+")
			
			filePoint.writelines(IP)
			filePoint.close() #这里存在多次必要的IO操作？？？？待改进
	file_handler.close()  


#IP处理dirPath为分割后的文件所在的“目录”程序会自动搜索目录下的文件		
def ipProcess(dirPath):
	i = 0


	maxvalue = 0
	times = []
	dire = {}
	
	for root, dirs,files in os.walk(dirPath):
		print "get file"
	print "begin to statcstic............."
	while i < len(files):
		####print "file number" + str(len(files)) right 
		
		path = dirPath + "/" + files[i]
		filePoint = open(path, 'r')
		
		for cloums in filePoint:
			if cloums in dire:
				dire[cloums] = dire[cloums] + 1
				
			else:
				dire[cloums] = 1
			
		
		for k,v in dire.iteritems():       #字典遍历也可采用items但是会产生一个大的list浪费内存所以采用了iteritens迭代器具体参见（python学习笔记）
			if maxvalue < v:
				maxvalue = v
					
		times.append(maxvalue)
		i = i + 1
		dire = {}
	###print "total number is" + str(j) right
		
	return times

#删除文件dirPath为文件所在的目录，执行该程序会删除该文件夹下的所有文件	
def deleteFile(direPath):	
	for root, dirs,files in os.walk(direPath):
		print "delete files"
	i = 0;
	while i < len(files):
		path = direPath + "/" + files[i]
		if os.path.exists(path):
			print "delet "+ path
			os.remove(path)
		i = i +1
	
			

if __name__ == "__main__":
	
	generateMassiveIp("urldata", 100000)
	splitFile("urldata",100)
	time = ipProcess("./splitfile")
	
	iptime = 0
	i = 0
	while i < len(time) :
		iptime = iptime + time[i]
		i = i + 1
	deleteFile("./splitfile")
	print iptime
	os.remove("url_list")
	print time
	print len(time)
	
	
	
	
	
	
