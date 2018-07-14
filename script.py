import sys
import datetime
from screeninfo import get_monitors

def main():
    #if the user wants to apply the wallpapers form an alternate dir
    if (len(sys.argv) == 2):
        checkAlternateLDir(sys.argv[1])
    else:
        applyWallpaper("")


def checkAlternateLDir(filePath):
    print("Am I actually getting called?" + filePath)

def applyWallpaper(filePath):
    # Grabbing the current month as an int an converting it to a name
    currMonth = datetime.datetime.now().strftime("%m")
    currMonth = numbers_to_months(currMonth)
    # If the user wants to use the default wallpapers
    if not filePath:
        ## transform the image
        ## apply the image
        transformImage("")
    else:
        ## apply the image
        print()

def transformImage(currMonth):
    for m in get_monitors():
        print(str(m))

# --- Simple number to month conversions ---
def numbers_to_months(argument):
    # Stripping the leading 0s that datetime gives
    switcher = {
        '1': "january",
        '2': "february",
        '3': "march",
        '4': "april",
        '5': "may",
        '6': "june",
        '7': "july",
        '8': "august",
        '9': "september",
        '10': "october",
        '11': "november",
        '12': "december"
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument.strip('0'), "ERROR: Invalid Month Passed in")
    return func

if __name__ == '__main__':
    main()
