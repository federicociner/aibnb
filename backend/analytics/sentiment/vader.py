# -*- coding: utf-8 -*-

from utils import get_abspath, ensure_dir_exists
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import seaborn as sns
import matplotlib.pyplot as plt


def get_sentiment_scores(df, target='comments'):
    sia = SentimentIntensityAnalyzer()
    df['positive'] = df.apply(
        lambda x: sia.polarity_scores(x[target])['pos'], axis=1
    )

    df['neutral'] = df.apply(
        lambda x: sia.polarity_scores(x[target])['neu'], axis=1
    )

    df['negative'] = df.apply(
        lambda x: sia.polarity_scores(x[target])['neg'], axis=1
    )

    # Standardized sentiment score between -1.0 and 1.0
    df['compound'] = df.apply(
        lambda x: sia.polarity_scores(x[target])['compound'], axis=1
    )

    return df


def sentiment_by_listing(df):
    avg = df[['listing_id', 'compound', 'positive', 'neutral', 'negative']]
    return avg.groupby(['listing_id'], as_index=False).mean()


def plot_score_histograms(df, score_type, filename, filepath='graphs'):
    # Set figure parameters
    sns.set(font_scale=1.3, rc={'figure.figsize': (12, 8)})

    # Create plot and set parameters
    fig, ax = plt.subplots()
    ax.hist(df, bins=20)
    fig.suptitle('{} Polarity Score Frequency'.format(score_type))
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')

    # Save plot
    plotpath = get_abspath(filename, filepath)
    ensure_dir_exists(plotpath)
    plt.savefig(plotpath)
    plt.close()
