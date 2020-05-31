from textblob_de import TextBlobDE as TextBlob
import json
from pathlib import Path

LINE_BOUND_TOKEN = '\n ------------------------------------------------------------ \n'
MAIL_FILE_PATH = Path('../mails.json')

def analyseMail(mail: str):
    blob = TextBlob(mail)
    sentiment = blob.sentiment
    output = '\n'.join((mail, str(sentiment), LINE_BOUND_TOKEN))
    print(output)

with open(MAIL_FILE_PATH) as mails_file:
    data = json.load(mails_file)
    for mail in data['mails']:
        blob = TextBlob(mail)
        analyseMail(mail)

