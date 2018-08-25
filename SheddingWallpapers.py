#!/usr/bin/env python3
# coding: utf-8

# SheddingWallpapers is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SheddingWallpapers is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with WeatherDesk (in the LICENSE file).
# If not, see <http://www.gnu.org/licenses/>.

import sys
import datetime
import os
import Desktop
import tqdm
import logging

from screeninfo import get_monitors
from PIL import Image
from multiprocessing import Pool
from logging import handlers

if not os.path.exists("Logs/"):
    os.makedirs("Logs/")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_logger_formatter = logging.Formatter('[%(levelname)s | %(asctime)s | %(filename)s | %(lineno)d] %(message)s')

file_logger = logging.handlers.RotatingFileHandler("Logs/SheddingWallpapers_log", maxBytes=100000, backupCount=5)
file_logger.setFormatter(file_logger_formatter)
logger.addHandler(file_logger)


def main():
    if len(sys.argv) == 2 and os.path.isdir(sys.argv[1]):
        apply_image(sys.argv[1])
    else:
        apply_image("")


def apply_image(file_path):
    # Grabbing the current month
    curr_month = numbers_to_months()

    # If we are dealing with the default wallpapers
    if not file_path:
        logger.info("Alternate image location not detected")
        transform_images()

        logger.info("Applying [" + str(curr_month) + ".png" + "] as new wallpaper")
        print("Applying [" + str(curr_month) + ".png" + "] as new wallpaper")

        curr_month_file_path = os.path.abspath("Edited_Wallpapers/" + str(curr_month) + ".png")
        Desktop.set_wallpaper(curr_month_file_path, Desktop.get_desktop_environment())
    # If we are dealing with a directory that the user has passed in
    else:
        logger.info("Alternate image location detected...attempting to apply wallpaper")
        Desktop.set_wallpaper(file_path, Desktop.get_desktop_environment())


def transform_images():
    # Check to prevent us from re-transforming when we dont need to
    if os.path.exists("Edited_Wallpapers/"):
        return
    else:
        os.makedirs("Edited_Wallpapers/")

    if not os.path.exists("Wallpapers/"):
        logger.critical("Wallpapers folder not found -- please re-download from git repo ["
                        "https://github.com/ridgeontheway/SheddingWallpapers]")
        print("Wallpapers folder not found -- eference the log for more details")
        sys.exit(0)

    logger.info("Wallpapers not transformed -- applying transformation to original images ")
    screen_width = get_monitor_resolution()
    upscale_info = [["January", screen_width], ["February", screen_width], ["March", screen_width],
                    ["April", screen_width], ["May", screen_width], ["June", screen_width], ["July", screen_width],
                    ["August", screen_width], ["September", screen_width], ["October", screen_width],
                    ["November", screen_width], ["December", screen_width]]

    try:
        process_pool = Pool()
        print("Performing upscale transformations on original images: ")
        for _ in tqdm.tqdm(process_pool.imap_unordered(upscale_image, upscale_info), desc='Images upscaled: ',
                           total=len(upscale_info), unit=' IMG'):
            pass

        process_pool.close()
        process_pool.join()
    except ValueError:
        logger.critical(ValueError)
        print("Critical error reached when applying transformations, reference the log for more details")


def upscale_image(inputted_tuple):
    unedited_image = Image.open("Wallpapers/" + str(inputted_tuple[0]) + ".png")
    width_percent = (inputted_tuple[1] / float(unedited_image.size[0]))
    height_size = int((float(unedited_image.size[1]) * float(width_percent)))
    edited_image = unedited_image.resize((inputted_tuple[1], height_size), Image.LANCZOS)
    edited_image.save("Edited_Wallpapers/" + str(inputted_tuple[0]) + ".png")


def get_monitor_resolution():
    try:
        width = 0
        for m in get_monitors():
            if width < m.width:
                width = m.width
        return width
    except ValueError:
        logger.critical(ValueError)
        print("Critical error reached when fetching your monitor resolution, reference the log for more details")


# --- Simple number to month conversions ---
def numbers_to_months():
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
    unformatted_month = datetime.datetime.now().strftime("%m")
    formatted_month = switcher.get(unformatted_month.strip('0'), "ERROR: Invalid Month")
    return formatted_month


if __name__ == '__main__':
    main()
