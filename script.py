import sys
import datetime
import os
import platform

def main():
    #if the user wants to apply the wallpapers form an alternate dir
    if (len(sys.argv) == 2):
        checkAlternateLDir()
    else:
        applyWallpaper("")


def checkAlternateLDir():
    #todo actually check the dir
    if (os.path.isdir(sys.argv[1])):
        applyImage(sys.argv[1])
    else:
        # The dir was not found, defaulting to the regular wallpapers
        applyWallpaper("")

def applyWallpaper(filePath):
    # If the user wants to use the default wallpapers
    if not filePath:
        applyImage("")
    else:
        applyImage(filePath)

def applyImage(filePath):
    # Grabbing the current month as an int an converting it to a name
    currMonth = datetime.datetime.now().strftime("%m")
    currMonth = numbers_to_months(currMonth)

    # If we are dealing with the default wallpapers
    if not filePath:
        currMonthFilePath = os.path.abspath("wallpapers/" + str(currMonth) + ".jpg")

        # Checking if the user is running linux / gnome
        if (platform.system() == "Linux" and os.environ["DESKTOP_SESSION"] == "gnome"):
            os.system("gsettings set org.gnome.desktop.background picture-uri file:" + currMonthFilePath)
            os.system("gsettings set org.gnome.desktop.background picture-options \"zoom\"")
        elif (platform.system() == "Windows"):
            print("windows support not yet implemented")
        elif (platform.system() == "Darwin"):
            print("mac support not yet implemented")
    else:
        #todo implement alternate dir support
        print("")


# --- Simple number to month conversions ---
def numbers_to_months(argument):
    # Stripping the leading 0s that datetime gives
    switcher = {
        '1': "January",
        '2': "February",
        '3': "March",
        '4': "April",
        '5': "May",
        '6': "June",
        '7': "July",
        '8': "August",
        '9': "September",
        '10': "October",
        '11': "November",
        '12': "December"
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument.strip('0'), "ERROR: Invalid Month Passed in")
    return func

if __name__ == '__main__':
    main()
