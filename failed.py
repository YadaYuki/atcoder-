import csv
import sys
import datetime


if __name__ == "__main__":
    args = sys.argv
    branch_name =  args[1]
    problem_name = args[2]
    with open('failed.csv',"a") as f:
        writer = csv.writer(f)
        writer.writerow([f'{branch_name}/{problem_name}.py',datetime.date.today()])

