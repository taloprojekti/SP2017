def downloader():
	#import downloader
  #downloader.main()
  return 0

def lampotila():
	Tnow = 15
	#import lampotila
	#lampotila.main()
	return Tnow
	

def main():
	
	import time                            
	from datetime import datetime        
	n = 0
	ret1 = 0
	t0 = time.time()
	try:
		while ret1 == 0:
			time.sleep(10)
			#tähän tulee PID funktio
			now = datetime.now()
			print("{:d}:{:d}:{:d}".format(now.hour, now.minute, now.second))
			if now.minute == 0 and now.hour == 0:
				downloader()
				while now.minute == 0:
					time.sleep(1)
					now = datetime.now()

			if now.minute % 30 == 0: 
				lampotila() 
				while now.minute % 30:
					time.sleep(1)
					datetime.now()
					
	except KeyboardInterrupt:
		return
	
main()	
