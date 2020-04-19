'''
download bing image of the day

maybe set it as desktop wallpaper
'''

import requests, json, os, sys
from bs4 import BeautifulSoup

# Configurations
# Location to save downloaded wallpapers
# Leave the IMAGE_DIR empty to use default directory /Users/USERNAME/Pictures/BingWallpapers
# Or you can set your own custom directory
IMAGE_DIR = ''
# ISO country code
# eg. 'en-US', 'en-NZ', 'zh-CN' or just leave it
COUNTRY_CODE = 'zh-CN'

# Apple Script to set wallpaper
SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

dir_path = os.path.dirname(os.path.realpath(__file__)) 

URL = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'

headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36" 
}

def downloadImage(url, filePath, download_only=False):
    if os.path.isfile(filePath):
        print('Skipped - ' + filePath.split('/')[-1] + ' exists already.')
    else:
        file = open(filePath, "wb")
        file.write(requests.get(url, headers=headers).content)
        file.close()
        print('Image downloaded --> ' + filePath)

    if not download_only:
        setWallpaper(filePath)

def getFilePath(fileName):
    if '' != IMAGE_DIR.strip():
        dir = IMAGE_DIR
    else:
        dir = os.path.join(os.path.expanduser("~"), 'Pictures/BingWallpapers')

    if not os.path.exists(dir):
        os.makedirs(dir)

    file_path = os.path.join(dir, fileName)
    return file_path

def setWallpaper(filePath):
    if os.path.isfile(filePath):
        import subprocess
        subprocess.Popen(SCRIPT%filePath, shell=True)
        print('Wallpaper set to ' + filePath)

def imageDownloader():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser').get_text()
    jsonData = json.loads(soup)
    # print(json.dumps(parsed, indent=2, sort_keys=True))
    # for images in parsed['images']:
    #     print('_'.join(images['copyright'].split()[:2]))
    fileName = '_'.join(jsonData['images'][0]['copyright'].split()[:2])
    imageUrl = 'http://www.bing.com' + jsonData['images'][0]['url']

    filePath = getFilePath(fileName)
    
    downloadImage(imageUrl, filePath)

# Display help message
def printHelpMessage():
    msg = '''
Bing Wallpaper for Mac 
By Chetan Chauahn  chetanchauhanofficial@gmail.com
Bing Wallpaper for Mac can batch download and set Bing image of the day as wallpaper on OS X.
Usage: 
python BingImageDownloader.py [option]
no argument         download today's picture of the day and set it as wallpaper
-d or --download n  download and save the last n pictures withouth changing the current wallpaper
-h or --help        display this help message
    '''
    # print(msg)
    sys.exit(msg)

# imageDownloader()
# print(getFilePath('image1.jpg'))

# setWallpaper('/Users/chetan_mac/Pictures/BingWallpapers/Vernal_Fall.jpg')

def main():
    n=1
    if len(sys.argv) == 1:
        flag_download_only= False
    elif len(sys.argv) >= 2:
        if '-d' == sys.argv[1] or '--download' == sys.argv[1]:
            flag_download_only = True
            n=sys.argv[2] if sys.argv[2] else 8
        elif '-h' == sys.argv[1] or '--help' == sys.argv[1]:
            printHelpMessage()
        else:
            print('Invalid argument!')
            printHelpMessage()
    else:
        print('Invalid arguments!')
        printHelpMessage()
    if flag_download_only:
        url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=' + str(n)  
    else:
        url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    
    if '' != COUNTRY_CODE.strip():
        url += '&mkt=' + COUNTRY_CODE

    try:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser').get_text()
        jsonData = json.loads(soup)
        if 'images' in jsonData:
            images = jsonData['images']
        else:
            sys.exit('JSON error. Please try again later...')
        
        for i in range(len(images)):
            imageUrl = 'http://www.bing.com' + jsonData['images'][i]['url']
            fileName = '_'.join(jsonData['images'][i]['copyright'].split()[:2]) + '.jpg'
            filePath = getFilePath(fileName)
            if flag_download_only:
                downloadImage(imageUrl, filePath, True)
            else:
                downloadImage(url, filePath)
    except requests.HTTPError as e:
        print('Error ' + str(e.code) + '. Please try again later...')

    except requests.URLError as e:
        print('Error. Please check your internet connection...')


if __name__ == '__main__':
    main()