class TimeRecorder:
    def __init__(self):
        self._nanoseconds = None
    
    @property
    def nanoseconds(self):
        return self._nanoseconds
    
    @nanoseconds.setter
    def nanoseconds(self, value):
        self._nanoseconds = value

    @property
    def milliseconds(self):
        return self._nanoseconds / 1_000_000

    @property
    def seconds(self):
        return self._nanoseconds / 1_000_000_000

    @property
    def minutes(self):
        return self.seconds / 60
    
# tr = TimeRecorder(1_000_000)
# print(tr.nanoseconds)
# print(tr.milliseconds)
# print(tr.seconds)