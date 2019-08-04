import datetime
import json
import os
import time

__version__ = 0.1


class Logger:
    def __init__(self):
        self.error = ""
        self.info = ""

        # Loading Necessary Information from Config File
        with open("/home/milad/College/Medify/config/config.json") as config_file:
            config_data = json.load(config_file)
            self.log_dir = config_data['log_directory']
            if not os.path.exists(self.log_dir):
                os.makedirs(self.log_dir)

    def save_error(self, error):  # Save errors in error.log

        self.error = str(error.encode('utf-8'))  # Saving Last error in variable (no use for now)
        error_log_path = self.log_dir + '[' + str(datetime.date.today().year) + '-' + str(
            datetime.date.today().month) + ']' + 'error.log'
        if os.path.exists(error_log_path):  # Check if error.log exists
            append_write = 'a'
        else:
            append_write = 'w'

        with open(error_log_path, mode=append_write) as error_log:
            error_log.write(
                str('\n' + time.strftime("%Y-%m-%d  %H:%M:%S"))
                + "\ninfo:\n" + str(self.info)
                + "\nerror:\n" + str(error) + "\n")

    def save_info(self, info):  # Save information in info.log

        info = str(info.encode('utf-8'))

        self.info = info  # Saving last info in variable for using in error log

        info_log_path = self.log_dir + '[' + str(datetime.date.today().year) + '-' + str(
            datetime.date.today().month) + ']' + 'info.log'

        if os.path.exists(info_log_path):  # Checking if info.log exists
            append_write = 'a'
        else:
            append_write = 'w'

        with open(info_log_path, mode=append_write) as info_log:
            info_log.write('\n' + time.strftime("%Y-%m-%d  %H:%M:%S")
                           + '\n' + info + "\n")

    def log(self, log_type, message):  # main function to call in other classes
        if log_type == 'error':
            self.save_error(message)
            self.save_info('Error:\n' + message)  # TODO: FIX self.last_info and ...
        elif log_type == 'info':
            self.save_info(message)
