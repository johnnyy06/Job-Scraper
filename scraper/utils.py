import pandas as pd
from sqlalchemy import create_engine

def save_to_csv(jobs, filename='data/jobs.csv'):
    df = pd.DataFrame(jobs)
    df.to_csv(filename, index=False)


def save_to_db(jobs, db_url='sqlite:///data/jobs.db'):
    engine = create_engine(db_url)
    df = pd.DataFrame(jobs)
    df.to_sql('jobs', engine, if_exists='replace', index=False)