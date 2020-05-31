import numpy as np
import matplotlib.pyplot as plt
import json

from wordcloud import WordCloud
from stop_words import get_stop_words
from pathlib import Path

MAIL_FILE_PATH = Path('../mails.json')
BLACKLIST = get_stop_words('german')

text = ''
with open(MAIL_FILE_PATH) as mails_file:
    data = json.load(mails_file)
    for mail in data['mails']:
        text = text + mail

wc = WordCloud(background_color='white', stopwords=BLACKLIST)
wc.generate(text)
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()

