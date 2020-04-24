# apt install mediainfo
# brew install mediainfo
# mediainfo --Output=JSON <file_name>

# import os

import json, subprocess, sys, pathlib
from datetime import timedelta

#==============================================================
# DIR = os.path.join(os.path.expanduser("~"), 'Downloads/algo-005')
DIR = pathlib.Path.home()/'Downloads/algo-005'
# VERBOSE = False
#==============================================================

def getMediaInfo(mediafile):
    cmd = "mediainfo --Output=JSON %s"%(mediafile)
    proc = subprocess.Popen(cmd, shell=True,
        stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    data = json.loads(stdout)
    return data         # returns json data

#==============================================================

def getDuration(mediafile, VERBOSE=False):
    data = getMediaInfo(mediafile)
    duration = float(data['media']['track'][0]['Duration'])
    if VERBOSE:
        print(mediafile.name + ' : ' + str(timedelta(seconds=int(duration))))
    return duration
    # return str(timedelta(seconds=int(duration)))

#==============================================================

def getDurationInDirectory(DIR, VERBOSE=False):
    p = pathlib.Path(DIR)
    totalDuration = 0
    durationInFolder = 0
    parentDir = ''
    for mp4 in sorted(p.glob('**/*.mp4')):
        if mp4.parent != parentDir:
            parentDir = mp4.parent
            if VERBOSE:
                if mp4 != sorted(p.glob('**/*.mp4'))[0]:
                    print("TOTAL DURATION IN THIS FOLDER : " + str(timedelta(seconds=int(durationInFolder))))
                print('#==============================================================')
                print(str(parentDir).split('algo-005')[1][1:])
                print('#==============================================================')
            durationInFolder = 0
        duration = getDuration(mp4, VERBOSE)
        totalDuration += duration
        durationInFolder+=duration
        if mp4 == sorted(p.glob('**/*.mp4'))[-1] and VERBOSE:
            print("TOTAL DURATION IN THIS FOLDER : " + str(timedelta(seconds=int(durationInFolder))))
            print('#==============================================================')

    return totalDuration 

#==============================================================

def main():
    VERBOSE = False
    if '-v' in sys.argv:
        VERBOSE = True
    if len(sys.argv) >= 2 and sys.argv[1][0] != '-':
        mediafile = sys.argv[1]

        if pathlib.Path(mediafile).anchor in ['/', '.', '~']:
            if pathlib.Path(mediafile).is_file():
                duration = getDuration(mediafile, VERBOSE)
            else:
                duration = getDurationInDirectory(mediafile, VERBOSE)
        else:
            if pathlib.Path(mediafile).is_file():
                duration = getDuration(pathlib.Path.cwd() / mediafile, VERBOSE)
            else:
                duration = getDurationInDirectory(pathlib.Path.cwd() / mediafile, VERBOSE)

        print('Total Video Time :: ' + str(timedelta(seconds=int(duration))))
    else:
        duration = getDurationInDirectory(pathlib.Path.cwd(), VERBOSE)
        print('Total Video Time :: ' + str(timedelta(seconds=int(duration))))

if __name__ == '__main__':
    main()