import os, sys

isDEBUG = False
# Root Direcotry
pathToDownload = "D:\Music" 

def download(arg):
    cmd = f'spotdl --lyrics=genius {arg}'
    if (isDEBUG):
        print(cmd)
    else:
        os.system(cmd)

if (__name__ == "__main__"):
    if len(sys.argv) == 1:
        print("Usage: spotdla <folder> url")
        print("Usage: spotdla url")
    elif len(sys.argv) == 2:
        newPathToDownload = pathToDownload + '\like'; 

        os.chdir(newPathToDownload)
        print(f"[1] download to {os.getcwd()}")
        download(sys.argv[1])

    elif len(sys.argv) == 3:
        newPathToDownload = pathToDownload + '\\' + sys.argv[1]

        if os.path.isdir(newPathToDownload) != True:
            os.mkdir(newPathToDownload)
        os.chdir(newPathToDownload)

        print(f"[2] download to {newPathToDownload}")
        download(sys.argv[2])
    
    if os.path.exists('.spotdl-cache'):
        os.remove('.spotdl-cache')