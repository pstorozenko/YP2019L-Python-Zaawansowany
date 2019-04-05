
def make_summary():
    zajecia = [
        {
            'temat': 'Przypomnienie Pythona',
            'tresc': 'Na pierwszych zajęciach poznawaliśmy zaawansowane sztuczki w pythonie.'
        },
        {
            'temat': 'Numpy',
            'tresc': 'Na drugich zajęciach były liczone numeryczne całki'
        }
    ]
    return zajecia

import datetime 

class LastVisit:
    def __init__(self):
        self.last = None

    def __call__(self):
        resp = self.last
        self.last = datetime.datetime.now()
        return resp
        