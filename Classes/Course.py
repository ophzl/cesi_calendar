class Course:

    def __init__(self, data):
        self.summary = data['name']
        self.description = "With " + data['professor']
        self.eventType = "default"
        self.location = data['location']
        self.locked = True
        self.start = {
            "dateTime": data['date'] + "T8:30:00.00+01:00",
            "timeZone": "Europe/Paris"
        }
        self.end = {
            "dateTime": data['date'] + "T16:30:00.00+01:00",
            "timeZone": "Europe/Paris"
        }
