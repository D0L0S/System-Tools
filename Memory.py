#!/usr/bin/env python

## #######################################
## 
## Originally Created To
## Allow Checking of Mac Memory from CLI
##
## #######################################

import subprocess, re

class Memory:

    def __init__(self):
        self.ps = subprocess.Popen(['ps', '-caxm', '-orss,comm'], stdout=subprocess.PIPE).communicate()[0]
        self.vm = subprocess.Popen(['vm_stat'], stdout=subprocess.PIPE).communicate()[0]

    def main(self):
        processLines = self.ps.split('\n')
        sep = re.compile('[\s]+')
        rssTotal = 0 # kB
        for row in range(1,len(processLines)):
            rowText = processLines[row].strip()
            rowElements = sep.split(rowText)
            try:
                rss = float(rowElements[0]) * 1024
            except:
                rss = 0
            rssTotal += rss
        vmLines = self.vm.split('\n')
        sep = re.compile(':[\s]+')
        vmStats = {}
        for row in range(1,len(vmLines)-2):
            rowText = vmLines[row].strip()
            rowElements = sep.split(rowText)
            vmStats[(rowElements[0])] = int(rowElements[1].strip('\.')) * 4096
        print ' [+] Wired Memory: {wired} MB'.format(wired=vmStats["Pages wired down"]/1024/1024)
        print ' [+] Active Memory: {active} MB'.format(active=vmStats["Pages active"]/1024/1024)
        print ' [+] Inactive Memory: {inactive} MB'.format(inactive=vmStats["Pages inactive"]/1024/1024)
        print ' [+] Free Memory: {free} MB'.format(free=vmStats["Pages free"]/1024/1024)
        print ' [+] Real Mem Total (ps): {real} MB'.format(real=rssTotal/1024/1024)

if __name__=="__main__":
    Memory().main()
