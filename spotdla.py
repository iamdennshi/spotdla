import os, sys

isDEBUG = False
linkToDefaultPlayList = "https://open.spotify.com/playlist/04pSdL0ACQaLDp090DayxH"
pathToDownload = "D:\\Music"

os.chdir(pathToDownload)

def action(arg):
    if (isDEBUG):
        print(arg)
    else:
        os.system(arg)


if (__name__ == "__main__"):
    if (len(sys.argv) == 2):
        action('spotdl ' + sys.argv[1])
    elif (len(sys.argv) == 1):
        action('spotdl ' + linkToDefaultPlayList)
    
    if (os.path.exists('.spotdl-cache')):
        os.remove('.spotdl-cache')