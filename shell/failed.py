import csv
import sys
import datetime
import pandas as pd
from os.path import dirname,join
from const import PATH_TO_FAILED_CSV


if __name__ == "__main__":
    args = sys.argv
    branch_name =  args[1]
    problem_name = args[2]
    filename = f'{branch_name}/{problem_name}'

    keyword_idx = -1
    keywords = []
    while keyword_idx != 0:
        print(f'0: No')
        for i,keyword in enumerate(KEYWORDS):
            print(f'{i+1}:{keyword}')
        print("Input keyword idx:")
        keyword_idx = int(input())
        keywords.append(KEYWORDS[keyword_idx-1])

    df = pd.read_csv(PATH_TO_FAILED_CSV)
    df = df.append({'problem': filename, 'date':datetime.date.today(),'keyword':';'.join(keywords),'is_resolved': False,'resolved_at':None}, ignore_index=True)
    df.to_csv(PATH_TO_FAILED_CSV, index=False)
