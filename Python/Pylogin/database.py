class Database:
    def __init__(self):
        self.records = [
            ['Thabo', '3210'],
            ['Sizwe', '8520'],
            ['Anda', '0123'],
            ['Jesus', '1111'],
            ['Amen', '0258']
            ]

    def add_record(self, name, id_number):
        self.records.append([name, id_number])

    def get_records(self):
        return self.records

    def find_record(self, name):
        for record in self.records:
            if record[0] == name:
                return record
        return None

class Profile:
    def __init__(self):
        self.profile = []