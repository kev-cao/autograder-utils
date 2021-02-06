import csv

class ScoresReader:
    def __init__(self, filename):
        with open(filename) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')

            self.scores = [{
                'username': row['Username'],
                'score': float(row['Total Points']),
                'total': float(row['Total Points Possible'])
                } for row in csv_reader]

            # Keep only usernames from emails.
            for score in self.scores:
                email = score['username']
                try:
                    score['username'] = email[:email.index('@')]
                except ValueError:
                    continue



    def scale_scores(self, new_total):
        """
        Scales down the scores to the new total.

        Params:
            new_total (float) : the new total points possible for the assignments.
        """
        for score in self.scores:
            new_score = new_total / score['total'] * score['score']

            score['score'] = round(new_score, 2)
            score['total'] = round(new_total, 2)
