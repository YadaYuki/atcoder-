import sys
import datetime
import pandas as pd
from const  import PATH_TO_SOLVED_CSV


if __name__ == "__main__":
    args = sys.argv
    branch_name =  args[1]
    problem_name = args[2]
    problem = f'{branch_name}/{problem_name}'



    df = pd.read_csv(PATH_TO_SOLVED_CSV)
    df = df.append({'problem': problem, 'solved_at':datetime.date.today()}, ignore_index=True)
    df.to_csv(PATH_TO_SOLVED_CSV, index=False)