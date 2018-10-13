
from Apps.Daily.daily import DailyQ
# Response should be written in this function
def response(Question):
    Answer = DailyQ(Question,"test")
    #Answer="123"
    print(Answer)
    return Answer