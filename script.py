import sys
import datetime
import os
import platform
import threading
from screeninfo import get_monitors
from PIL import Image


def main():
    if (len(sys.argv) == 2):
        checkAlternateLDir()
    else:
        transformImages()
        applyImage("")


def checkAlternateLDir():
    # todo actually check the dir
    if (os.path.isdir(sys.argv[1])):
        applyImage(sys.argv[1])
    else:
        # The dir was not found, defaulting to the regular wallpapers
        transformImages()
        applyImage("")


def applyImage(filePath):
    # Grabbing the current month as an int an converting it to a name
    currMonth = numbers_to_months()

    # If we are dealing with the default wallpapers
    if not filePath:
        currMonthFilePath = os.path.abspath("editedWallpapers/" + str(currMonth) + ".jpg")

        # Checking if the user is running linux / gnome
        if (platform.system() == "Linux" and os.environ["DESKTOP_SESSION"] == "gnome"):
            os.system("gsettings set org.gnome.desktop.background picture-uri file:" + currMonthFilePath)
        elif (platform.system() == "Windows"):
            print("windows support not yet implemented")
        elif (platform.system() == "Darwin"):
            print("mac support not yet implemented")
    else:
        # todo implement alternate dir support
        print("")


def transformImages():
    # If we have transformed the images then we dont want to do it again
    if os.path.exists("editedWallpapers/"):
        return
    else:
        os.makedirs("editedWallpapers/")

    monthArray = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]
    currWidth = getMonitorResolution()

    #Keeping Track of all the threads we are currently using
    threadArray = []

    # Calling threads to apply the transformations to all images
    for currMonth in monthArray:
        thread = threading.Thread(target=upscaleImage, args=(currMonth,currWidth,))
        thread.start()
        threadArray.append(thread)

    for currThread in threadArray:
        print("active Threads: ", threading.active_count())
        currThread.join()


def upscaleImage(month, currWidth):
    uneditedImage = Image.open("wallpapers/" + str(month) + ".jpg")
    # Changing the size of the image, and saving the output
    wpercent = (currWidth / float(uneditedImage.size[0]))
    hsize = int((float(uneditedImage.size[1]) * float(wpercent)))
    editedImage = uneditedImage.resize((currWidth, hsize), Image.LANCZOS)
    editedImage.save("editedWallpapers/" + str(month) + ".jpg")


def getMonitorResolution():
    width = 0

    # We are looping though all the monitors that the user has, and saving the largest one for transformation
    for m in get_monitors():
        print(str(m))
        if (width < m.width):
            width = m.width

    return width


# --- Simple number to month conversions ---
def numbers_to_months():
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
    currMonth = datetime.datetime.now().strftime("%m")
    func = switcher.get(currMonth.strip('0'), "ERROR: Invalid Month Passed in")
    return func


if __name__ == '__main__':
    main()
