import csv
import sys
import datetime
from os.path import dirname
import pandas as pd


if __name__ == "__main__":
    args = sys.argv
    branch_name =  args[1]
    problem_name = args[2]
    problem = f'{branch_name}/{problem_name}.py'
    DIR = dirname(__file__)
    PATH_TO_CSV = f'{DIR}/failed.csv'
    df = pd.read_csv(PATH_TO_CSV)
    df.loc[df['problem'] == problem,'is_resolved'] = True
    df.loc[df['problem'] == problem,'resolved_at'] = datetime.date.today()
    df.to_csv(PATH_TO_CSV, index=False)