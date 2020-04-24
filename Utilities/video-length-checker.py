# apt install mediainfo
# brew install mediainfo
# mediainfo --Output=JSON <file_name>

# import os

import json, subprocess, sys, pathlib
from datetime import timedelta

#==============================================================
# DIR = os.path.join(os.path.expanduser("~"), 'Downloads/algo-005')
DIR = pathlib.Path.home()/'Downloads/algo-005'
#==============================================================

def getMediaInfo(mediafile):
    cmd = "mediainfo --Output=JSON %s"%(mediafile)
    proc = subprocess.Popen(cmd, shell=True,
        stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    data = json.loads(stdout)
    return data         # returns json data

#==============================================================

def getDuration(mediafile):
    data = getMediaInfo(mediafile)
    duration = float(data['media']['track'][0]['Duration'])
    return duration
    # return str(timedelta(seconds=int(duration)))

#==============================================================

def getDurationInDirectory(DIR):
    p = pathlib.Path(DIR)
    totalDuration = 0
    for mp4 in p.glob('**/*.mp4'):
        totalDuration += getDuration(mp4)
    return totalDuration 

#==============================================================

def main():
    if len(sys.argv) == 2:
        mediafile = sys.argv[1]

        if pathlib.Path(mediafile).anchor in ['/', '.', '~']:
            if pathlib.Path(mediafile).is_file():
                duration = getDuration(mediafile)
            else:
                duration = getDurationInDirectory(mediafile)
        else:
            if pathlib.Path(mediafile).is_file():
                duration = getDuration(pathlib.Path.cwd() / mediafile)
            else:
                duration = getDurationInDirectory(pathlib.Path.cwd() / mediafile)

        print(str(timedelta(seconds=int(duration))))
    else:
        duration = getDurationInDirectory(pathlib.Path.cwd())
        print(str(timedelta(seconds=int(duration))))

if __name__ == '__main__':
    main()