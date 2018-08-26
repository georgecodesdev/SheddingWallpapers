import sys
import os
import logging

working_directory = os.path.abspath("SheddingWallpaper").rpartition('/')[0]

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_logger_formatter = logging.Formatter('[Level = %(levelname)s | Time = %(asctime)s | File = %(filename)s | Line = '
                                          '%(lineno)d] %(message)s')

file_logger = logging.handlers.RotatingFileHandler(os.path.abspath("{}/Logs/SheddingWallpapers_log".format(working_directory)), maxBytes=100000, backupCount=5)
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
    print(os.path.abspath(file_name))
    file_path = os.path.join("/etc/xdg/autostart", "{}.desktop".format(file_name))
    if not os.path.exists("~/.config/autostart"):
        new_file = open(file_path, "w+")
        new_file.write("[Desktop Entry]\nName={}\nGenericName={}\nComment={}\nExec={"
                       "}\nTerminal=false\nType=Application\nX-GNOME-Autostart-enabled=true".format(file_name,
                                                                                                    generic_name,
                                                                                                    comment,
                                                                                                    "python {}.py".format(os.path.abspath(file_name))
                                                                                                    ))
        new_file.close()
    else:
        logging.warning("AutoStart file already exists, please remove {}{}.desktop and re-run if you wish for a new "
                        "one to get created".format("~/.config/autostart/", file_name))
