from textblob_de import TextBlobDE as TextBlob
import json
from pathlib import Path
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

LINE_BOUND_TOKEN = '\n ------------------------------------------------------------ \n'
MAIL_FILE_PATH = Path('../mails.json')

def output_sentiment_on_console(mail: str):
    blob = TextBlob(mail)
    sentiment = blob.sentiment
    output = '\n'.join((mail, str(sentiment), LINE_BOUND_TOKEN))
    print(output)

def console_sentiment_analysis(mails: list):
    for mail in mails:
        output_sentiment_on_console(mail) 

def create_sentiment_distribution_plot(mails: list):
    polarities = list()
    for mail in mails:
        blob = TextBlob(mail)
        polarity = blob.sentiment.polarity
        polarities.append(polarity)
    polarities = [-0.2, -0.2, 0.5, 0.51, 0.52, 0.511, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    polarities = np.array(polarities)
    print(polarities)
    
    minbin = -1
    maxbin = 1
    cmap = plt.get_cmap('RdYlGn')
    norm = mpl.colors.Normalize(vmin=-1, vmax=1)
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0, 0.8, 0.2])
    axDist = fig.add_axes([0.1, 0.25, 0.8, 0.7])
    cb1 = mpl.colorbar.ColorbarBase(ax, cmap=plt.get_cmap('RdYlGn'),
                                norm=norm,
                                orientation='horizontal')
    sns.set_style("darkgrid")
    axDist = sns.distplot(polarities, hist=False, ax=axDist, kde=True, label='Polarity score', kde_kws={'shade': True, 'linewidth': 3})
    axDist.set_xlim(-1, 1)
    plt.show()

with open(MAIL_FILE_PATH) as mails_file:
    data = json.load(mails_file)
    mails = data['mails']
    console_sentiment_analysis(mails)
    create_sentiment_distribution_plot(mails)

