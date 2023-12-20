import pandas
import os,csv,zipfile,subprocess


#test

try:
	cwd=os.getcwd()

	cmd='copy '+ os.path.join(cwd,'Ami_ImportEOD_realtime.exe')+ ' D:'
	os.system(cmd)

	subprocess.check_call([os.path.join(cwd,'colectData_RealTime.bat')])
	with zipfile.ZipFile(os.path.join('D:','cophieu68_EOD_realtime.zip'),'r') as zip_ref:
		zip_ref.extractall(cwd)

	alphabet='Q W E R T Y U I O P A S D F G H J K L Z X C V B N M _'
	alphabet=alphabet.split()

	df_Ticker=pandas.read_csv(os.path.join(cwd,'data','TickerList.txt'),sep=" ") 
	df_EOD=pandas.read_csv(os.path.join(cwd,'amibroker_realtime_data.txt'),sep=",")

	for i in df_Ticker['Ticker']: 
		df_CurrentStock=df_EOD.loc[df_EOD["<Ticker>"]==i].reset_index(drop=True)

		if i[0] in alphabet and len(i)<=3:	
			tickerFile=i+'.txt'
			path=os.path.join(cwd,'data',str(i[0]),tickerFile)
			with open(path,'a') as outFile:
				df_CurrentStock.to_csv(outFile,header=None, index=None, sep=' ', mode='a')
		else:
			tickerFile=i+'.txt'
			path=os.path.join(cwd,'data','_',tickerFile)
			with open(path,'a') as outFile:
				df_CurrentStock.to_csv(outFile,header=None, index=None, sep=' ', mode='a')

	os.remove(os.path.join('D:','Ami_ImportEOD_realtime.exe'))
	os.remove(os.path.join('D:','cophieu68_EOD_realtime.zip'))
except NameError:
	print('Error name:',NameError)
except:
	print("Unknown error")
    
   #next comment
   #second comment