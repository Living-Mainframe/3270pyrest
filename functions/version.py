from functions.emulator import EmulatorFunction

class GetVersion(EmulatorFunction):
    def logon(self):
        self.emulator.connect(self.host)

    def logoff(self):
        self.emulator.terminate()

    def run(self):
        self.send_enter(send_enter_key=False)
        version = self.emulator.string_get(1, 1, 16).strip()
        return version, 200
