import sys
import requests
from bs4 import BeautifulSoup
import json
import os
from glob import glob


s =requests.Session()
def getTitle(videocode):
    resp = s.get(f'https://api.avgle.com/v1/jav/{videocode}/0?limit=2')
    soup = BeautifulSoup(resp.text,'html.parser')
    data = json.loads(str(soup))
    return data['response']['videos'][0]['title']
# videopath = 'G:\Video/*/'
videopath = sys.argv[1] + '/*/'

def renamefileinfolder(folderpath):
    filelist = os.listdir(path=folderpath)
    # print(filelist)
    for file in filelist:
        if(file.count('-')):
            try:
                newname = getTitle(file.split('.')[0])
                dest =f'{newname}.mp4'
                os.rename(folderpath + file, folderpath + dest)
                print(f'{file} has been rename to {newname}')
            except:
                pass


res = glob(videopath, recursive = True)

for folder in res:
    res = res + glob(folder+'/*/', recursive = True)
res.append(sys.argv[1])
# print(res)
for folderpath in res:
    renamefileinfolder(folderpath)
