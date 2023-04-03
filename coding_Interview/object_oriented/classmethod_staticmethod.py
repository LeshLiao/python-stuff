
class Calendar:

    # Can not access value of instance
    @staticmethod
    def is_weekend(date):
        return date.weekday() > 4

    # pass the class as a parameter
    @classmethod
    def from_jason(cls, filename):
        c = cls()
        return c


class WorkCalendar(Calendar):
    pass

if __name__ == "__main__":
    pass
