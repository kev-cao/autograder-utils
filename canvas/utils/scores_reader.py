import csv

class ScoresReader:
    def __init__(self, filename):
        with open(filename) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')

            self.scores = [{
                'Username': row['Username'],
                'Score': row['Total Points'],
                'Total': row['Total Points Possible']
                } for row in csv_reader]
