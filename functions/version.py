from functions.emulator import EmulatorFunction

class GetVersion(EmulatorFunction):
    def run(self):
        self.send_enter(send_enter_key=False)
        version = self.emulator.string_get(1, 1, 16).strip()
        return version, 200
