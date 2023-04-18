from py3270 import Emulator
import time, logging

class EmulatorFunction:
    def __init__(self, host, user, passwd):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.emulator = Emulator()
    
    def logon(self):
        self.emulator.connect(self.host)
        self.send_enter(send_enter_key=False)
        self.emulator.send_string(f"LOGON {self.user}")
        self.send_enter()
        self.emulator.send_string(f"{self.passwd}")
        self.send_enter()
        self.send_enter()

    def logoff(self):
        self.emulator.send_pf3()
        self.emulator.send_string(f"LOGOFF")
        self.send_enter()
        self.emulator.terminate()

    def print_screen(self, file_path):
        # TODO use tempfile
        self.emulator.exec_command("PrintText(file,{0})".format(file_path).encode("ascii"))
        with open(file_path, 'r') as fin:
            print(fin.read())
        #delete_file(file_path)

    def send_enter(self, send_enter_key=True, sleep_time=0.5):
        if send_enter_key:
            self.emulator.send_enter()

        logging.log(logging.INFO, f"Sleep time: {sleep_time} seconds")
        time.sleep(sleep_time)
        logging.log(logging.INFO, f"Woke up after: {sleep_time} seconds")

        self.emulator.wait_for_field()
        self.print_screen("test.txt")

    def run(self):
        return "Program executed successfully", 200
