import os
class Useclamav:
     def __init__(self, scanFile, virusFile):
          self.scanFile = scanFile
          self.virusFile = virusFile
     def scan(self):
          a=os.popen("cd VIRUS && clamscan -i -r --move="+self.virusFile+" "+self.scanFile)
          print(a.read())



scanFile="/home/user/forBrian/biohazard" #The address you want to scan
virusFile = "/home/user/VIRUS"           #The address you want to put the virus
UC = Useclamav(scanFile, virusFile)
UC.scan()
