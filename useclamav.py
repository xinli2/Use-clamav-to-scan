import os
class Useclamav:
     def __init__(self, scanFile, virusFile):
          self.scanFile = scanFile
          self.virusFile = virusFile
     def scan(self):
          a=os.popen("cd VIRUS && clamscan -i -r --move="+self.virusFile+" "+self.scanFile)
          print(a.read())



scanFile="/home/user/forBrian/biohazard"
virusFile = "/home/user/VIRUS"
UC = Useclamav(scanFile, virusFile)
UC.scan()