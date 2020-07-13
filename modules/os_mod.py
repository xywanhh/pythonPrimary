# -*- encoding=utf-8 -*-
#!/bin/python3
"""
os module
"""
import os

print('hello world.')

# use recursion
def recursionDirsFiles(path):
    if os.path.isdir(path):
        files = os.listdir(path)
        for file in files:
            if file.endswith('.git'):
                continue
            curPath = os.path.join(path, file)
            if os.path.isdir(curPath):
                localDirs.append(curPath)
                recursionDirsFiles(curPath)
            elif os.path.isfile(curPath):
                localFiles.append(curPath)

# use os.walk
def walkDirsFiles(path):
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if root.find('.git') == -1 and (dir != '.git' and dir != '.idea'):
                curDir = os.path.join(root, dir)
                localDirs.append(curDir)
        for file in files:
            if not root.find('.git') != -1:
                curFile = os.path.join(root, file)
                localFiles.append(curFile)

localDirs = []
localFiles = []
if __name__ == '__main__':
    localPath = 'E:\\githubRepositorys\\pythonPrimary'
    
    recursionDirsFiles(localPath)
    print('1', localDirs)
    print('1', localFiles)

    localDirs = []
    localFiles = []
    walkDirsFiles(localPath)
    print('2', localDirs)
    print('2', localFiles)