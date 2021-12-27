class Subject:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, beo):
        self.subscribers.append(beo)

    def unsubscribe(self, beo):
        self.subscribers.remove(beo)

    def notify(self):
        for sub in self.subscribers:
            sub.update()
