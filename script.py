import sys

def main():
    #if the user wants to apply the wallpapers form an alternate dir
    if (len(sys.argv) == 2):
        checkAlternateLDir(sys.argv[1])
    else:
        applyWallpaper("")


def checkAlternateLDir(filePath):
    print("Am I actually getting called?" + filePath)

def applyWallpaper(filePath):
    #If the user wants to use the default wallpapers included
    if not filePath:
        print("temp")

if __name__ == '__main__':
    main()
