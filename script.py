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

from screeninfo import get_monitors
from PIL import Image
from multiprocessing import Pool


def main():
    if len(sys.argv) == 2 and os.path.isdir(sys.argv[1]):
        apply_image(sys.argv[1])
    else:
        apply_image("")


def apply_image(file_path):
    # Grabbing the current month as an int an converting it to a name
    curr_month = numbers_to_months()

    # If we are dealing with the default wallpapers
    if not file_path:
        transform_images()
        curr_month_file_path = os.path.abspath("editedWallpapers/" + str(curr_month) + ".jpg")
        Desktop.set_wallpaper(curr_month_file_path, Desktop.get_desktop_environment())
    else:
        Desktop.set_wallpaper(file_path, Desktop.get_desktop_environment())


def transform_images():
    # If we have transformed the images then we dont want to do it again
    if os.path.exists("editedWallpapers/"):
        return
    else:
        os.makedirs("editedWallpapers/")

    screen_width = get_monitor_resolution()
    upscale_info = [["January", screen_width], ["February", screen_width], ["March", screen_width],
                    ["April", screen_width], ["May", screen_width], ["June", screen_width], ["July", screen_width],
                    ["August", screen_width], ["September", screen_width], ["October", screen_width],
                    ["November", screen_width], ["December", screen_width]]

    process_pool = Pool()
    for _ in tqdm.tqdm(process_pool.imap_unordered(upscale_image, upscale_info), desc='Images upscaled: ',
                       total=len(upscale_info), unit=' IMG'):
        pass
    process_pool.close()
    process_pool.join()


def upscale_image(inputted_tuple):
    unedited_image = Image.open("wallpapers/" + str(inputted_tuple[0]) + ".jpg")
    width_percent = (inputted_tuple[1] / float(unedited_image.size[0]))
    height_size = int((float(unedited_image.size[1]) * float(width_percent)))
    edited_image = unedited_image.resize((inputted_tuple[1], height_size), Image.LANCZOS)
    edited_image.save("editedWallpapers/" + str(inputted_tuple[0]) + ".jpg")


def get_monitor_resolution():
    width = 0
    # We are looping though all the monitors that the user has, and saving the largest one for transformation
    for m in get_monitors():
        if width < m.width:
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
    unformatted_month = datetime.datetime.now().strftime("%m")
    formatted_month = switcher.get(unformatted_month.strip('0'), "ERROR: Invalid Month")
    return formatted_month


if __name__ == '__main__':
    main()
