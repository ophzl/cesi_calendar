class Calendar:

    def __init__(self):
        self.summary = "CESI"
        self.timeZone = "Europe/Paris"
        self.description = "CESI Calendar by Ophzl"
        self.kind = "calendar#calendar"
        self.defaultReminders = [{'method': 'popup', 'minutes': 10}, {'method': 'popup', 'minutes': 5}]