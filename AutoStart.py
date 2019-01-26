#/usr/bin/env python3
# coding: utf-8

# This file is part of SheddingWallpapers.
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
import os
import logging

# Setting up the logger and log folder
working_directory = ""

if os.path.exists(sys.argv[0]) and str(sys.argv[0]).__contains__("/"):
    working_directory = sys.argv[0].rpartition('/')[0] + "/"

if not os.path.exists(os.path.abspath("{}Logs/".format(working_directory))):
    os.makedirs("{}Logs/".format(working_directory))

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_logger_formatter = logging.Formatter('[Level = %(levelname)s | Time = %(asctime)s | File = %(filename)s | Line = '
                                          '%(lineno)d] %(message)s')

file_logger = logging.handlers.RotatingFileHandler(os.path.abspath("{}Logs/SheddingWallpapers_AutoStart_Log".format(working_directory)), maxBytes=100000, backupCount=5)
file_logger.setFormatter(file_logger_formatter)
logger.addHandler(file_logger)


def auto_start(script_name, generic_name, comment):
    if sys.platform in ['win32', 'cygwin']:
        return 'windows not implemented'
    elif sys.platform == 'darwin':
        return 'mac not implemented'
    else:
        auto_start_linux(script_name, generic_name, comment)


def auto_start_linux(file_name, generic_name, comment):
    file_path = os.path.join("{}/.config/autostart".format(os.environ['HOME']), "{}.desktop".format(file_name))
    if not os.path.exists("{}/.config/autostart".format(os.environ['HOME'])):
        os.mkdir("{}/.config/autostart".format(os.environ['HOME'])) 
    if not os.path.exists(file_path):
        new_file = open(file_path, "w+")
        new_file.write("[Desktop Entry]\nName={}\nGenericName={}\nComment={}\nExec={"
                       "}\nTerminal=false\nType=Application\nX-GNOME-Autostart-enabled=true".format(file_name,
                                                                                                    generic_name,
                                                                                                    comment,
                                                                                                    "python {}.py".format(os.path.abspath(file_name))
                                                                                                    ))
        new_file.close()
    else:
        logging.warning("AutoStart file already exists, please remove {}{}.desktop file and re-run if you wish for a "
                        "new "
                        "one to get created".format("/etc/xdg/autostart", file_name))
