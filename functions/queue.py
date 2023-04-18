from functions.emulator import EmulatorFunction

class GetQueue(EmulatorFunction):
    def run(self):
        # go to SDSF -> input queue
        self.emulator.send_string("=m.5;i")
        self.send_enter()

        self.emulator.send_string("pre *;owner *")
        self.send_enter()

        queue = self.emulator.string_get(3, 1, 80).strip().split(" ")[-1]
        queue = queue.replace("(", "").replace(")", "")

        self.emulator.send_string("=x")
        self.send_enter()

        return queue, 200
