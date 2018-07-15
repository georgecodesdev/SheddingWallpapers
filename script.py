import sys
import datetime
import os
def main():
    #if the user wants to apply the wallpapers form an alternate dir
    if (len(sys.argv) == 2):
        checkAlternateLDir(sys.argv[1])
    else:
        applyWallpaper("")


def checkAlternateLDir(filePath):
    print("Am I actually getting called?" + filePath)

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
        # Applying the correct wallpaper for the month
        currMonthFilePath = os.path.abspath("wallpapers/" + str(currMonth) + ".jpg")
        os.system("gsettings set org.gnome.desktop.background picture-uri file:" + currMonthFilePath)
        os.system("gsettings set org.gnome.desktop.background picture-options \"zoom\"")

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
