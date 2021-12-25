import csv
import sys
import datetime
import pandas as pd
from const import PATH_TO_FAILED_CSV


if __name__ == "__main__":
    args = sys.argv
    branch_name =  args[1]
    problem_name = args[2]
    problem = f'{branch_name}/{problem_name}'
    df = pd.read_csv(PATH_TO_FAILED_CSV)
    df.loc[df['problem'] == problem,'is_resolved'] = True
    df.loc[df['problem'] == problem,'resolved_at'] = datetime.date.today()
    df.to_csv(PATH_TO_FAILED_CSV, index=False)