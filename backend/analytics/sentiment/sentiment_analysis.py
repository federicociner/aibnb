# -*- coding: utf-8 -*-

from utils import db_conn, db_config, db_table, write_to_db
from translate import detect_language
from vader import get_sentiment_scores, plot_score_histograms
from vader import sentiment_by_listing
from sqlalchemy.dialects.mysql import INTEGER, FLOAT


def run_sentiment_analysis(with_graphs=False):
    conn = db_conn(db_config())
    sql = 'SELECT * FROM reviews'
    df = db_table(conn, sql)
    df['lang'] = df.apply(lambda x: detect_language(x['comments']), axis=1)
    df_english = df.loc[df['lang'] == 'english']
    df_scores = get_sentiment_scores(df_english)

    if with_graphs:
        plot_score_histograms(df_scores['positive'],
                              score_type='Positive',
                              filename='pos_sentiment.png')
        plot_score_histograms(df_scores['neutral'],
                              score_type='Neutral',
                              filename='neu_sentiment.png')
        plot_score_histograms(df_scores['negative'],
                              score_type='Negative',
                              filename='neg_sentiment.png')
        plot_score_histograms(df_scores['compound'],
                              score_type='Compound',
                              filename='compound_sentiment.png')

    df_avg = sentiment_by_listing(df_scores)
    dtypes = {'listing_id': INTEGER,
              'compound': FLOAT,
              'positive': FLOAT,
              'neutral': FLOAT,
              'negative': FLOAT}

    write_to_db(conn, df_avg, name='listings_sentiment', dtypes=dtypes)


if __name__ == '__main__':
    run_sentiment_analysis(with_graphs=True)
