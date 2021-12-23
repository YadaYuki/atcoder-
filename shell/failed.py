import csv
import sys
import datetime
from os.path import dirname
import pandas as pd
from os.path import dirname,join

DIR = dirname(__file__)
AC_ROOT = join(DIR,'..')

if __name__ == "__main__":
    args = sys.argv
    branch_name =  args[1]
    problem_name = args[2]
    filename = f'{branch_name}/{problem_name}.py'
    PATH_TO_CSV = f'{AC_ROOT}/failed.csv'
    df = pd.read_csv(PATH_TO_CSV)
    df = df.append({'problem': filename, 'date':datetime.date.today(),'is_resolved': False,'resolved_at':None}, ignore_index=True)
    df.to_csv(PATH_TO_CSV, index=False)