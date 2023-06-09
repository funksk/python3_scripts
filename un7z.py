#!/bin/bash
import os
import subprocess

del7z = True


for root, dirs1, files1 in os.walk("./"):
    for file1 in files1:
        if file1.endswith(".7z"):
            i = 0
            tempName = os.path.join(root,file1[:-3])
            #print(file1[:-3])
            os.system('mkdir "' + file1[:-3] + '"')
            os.system('mv "' + file1 + '" "' + file1[:-3] + '"')
            #tempName1 = '"C:\\Program Files\\7-Zip\\7z.exe" e '
            tempName1 = '7z e '
			rmName = 'rm '
            #tempName1 = 'rm '
            tempName = "'" + file1[:-3] + '/' + file1 + "'"
            #tempName = file1[:-3] + '/' + file1
            #print('len = ', len(tempName))
            #while i < len(tempName):
            #    if tempName[i] == '(' or tempName[i] == ')' or tempName[i] == ' ':
            #        #print(i)
            #        tempName = tempName[:i] + '\\' + tempName[i:]
            #        i=i+1
            #    i=i+1
            #print(tempName)
            #cmd_out = tempName1 + './' + tempName
            cmd_out = 'cd "' + file1[:-3] + '" && ' + tempName1 + '"./' + file1 + '" && cd ..'
            print(cmd_out)
			
            subprocess.run(cmd_out, shell=True)
			
			if del7z:
				cmd_out = 'cd "' + file1[:-3] + '" && ' + rmName + '"./' + file1 + '" && cd ..'
				print(cmd_out)
				subprocess.run(cmd_out, shell=True)
			
            #exit()
            #os.system("bash " + cmd_out)
            #os.system('unecm.exe "' + tempName + '"')