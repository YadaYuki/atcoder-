import sys
import pandas as pd
import numpy as np
import datetime

WHITE_SPACE = " "
HOURLY_WAGE = 900
MIDNIGHT_START_TIME, MIDNIGHT_FINISH_TIME = "22:00", "04:00"


class Shift:
    def __init__(self, m: int, d: int, start_time: str, finish_time: str):
        self.m = m
        self.d = d
        self.start_time = start_time
        self.finish_time = finish_time
        # self.start_time_hour =

    def __str__(self):
        return "{}/{} {}-{}".format(self.m, self.d, self.start_time, self.finish_time)

    def __eq__(self, other):
        return self.m == other.m and self.d == other.d and self.start_time == other.start_time and self.finish_time == other.finish_time

    def get_date_format(self):
        return "{}/{}".format(str(self.m).zfill(2), str(self.d).zfill(2))

    def get_work_time(self):
        return (pd.Timestamp(self.finish_time) - pd.Timestamp(self.start_time))/np.timedelta64(1, 'h')

    def get_salary(self):
        return HOURLY_WAGE * self.get_work_time()

    def is_valid_schedule(self):
        if self.get_work_time() < 0:
            return False
        return True

    # def get_midnight_work_time():
    #   return


shift_database = {}  # {["id"]:[Shift,Shift...]}


def get_shift_list(shift_list_str: str):
    shift_list = []
    shift_list_str_arr = shift_list_str.split()
    for i in range(0, len(shift_list_str_arr), 2):
        date_data, time_data = shift_list_str_arr[i], shift_list_str_arr[i+1]
        m, d = [int(item) for item in date_data.split("/")]
        start_time, finish_time = [item for item in time_data.split("-")]
        shift = Shift(m, d, start_time, finish_time)
        shift_list.append(shift)
    return shift_list


def submit(employee_id: str, shift_list, K: int) -> bool:
    # check if is valid shift
    for shift in shift_list:
        if shift.is_valid_schedule() != True:
            return False

    # drop duplicate more than K
    submit_shift_list = []
    for shift in shift_list:
        number_of_worker_in_shift = 0
        for other_employee_id in shift_database:
            others_shift_list = shift_database[other_employee_id]
            for others_shift in others_shift_list:
                if shift == others_shift:
                    number_of_worker_in_shift += 1
        if number_of_worker_in_shift < K:
            submit_shift_list.append(shift)

    shift_database[employee_id] = submit_shift_list

    return True


def submit_query(employee_id: str, shift_list, K: int):
    if submit(employee_id, shift_list, K):
        print("accepted")
    else:
        print("wrong format")


def check_query(employee_id: str):
    shift_dates_str = ""
    shift_list = shift_database[employee_id]
    for item in shift_list:
        shift_dates_str += item.get_date_format() + WHITE_SPACE
    print(len(shift_list))
    print(shift_dates_str)


def calculate_query(employee_id: str):
    total_salary = 0
    shift_list = shift_database[employee_id]
    total_work_time = 0.0
    for item in shift_list:
        total_work_time += item.get_work_time()
        total_salary += item.get_salary()
    # total_saraly += total_work_time * HOURLY_WAGE
    if total_work_time >= 40.0:
        total_salary += 10000
    print(int(total_salary))


def cancel_query(employee_id: str, cancel_shift_list):
    if shift_database.get(employee_id) != None:
        print("no schedule")
        return
    else:
        shift_list = shift_database.get(employee_id)
        shift_list_deleted = []
        for cancel_shift in cancel_shift_list:
            is_exist = False
            for shift in shift_list:
                if shift != cancel_shift:
                    shift_list_deleted.append(shift)
                    is_exist = True
            if is_exist == False:
                print("wrong schedule")
                return
        shift_database[employee_id] = shift_list_deleted
        print("deleted")
    return shift_list_deleted


def main(lines):
    A, B, D, K, T = [int(item) for item in lines[0].split()]
    i = 1
    while i < len(lines):
        if lines[i] == "submit":
            X = lines[i+1]
            # S = lines[i+2]
            p = lines[i+3]
            shift_list = get_shift_list(p)
            submit_query(X, shift_list, K)
            i += 3
        elif lines[i] == "cancel":
            X = lines[i+1]
            p = lines[i+2]
            i += 2
        elif lines[i] == "check":
            X = lines[i+1]
            check_query(X)
            i += 1
        elif lines[i] == "calculate":
            X = lines[i+1]
            calculate_query(X)
            i += 1
        i += 1


if __name__ == "__main__":
    main('''1 31 3 1 2
submit
taro
2
01/31 21:00-23:00 01/31 19:00-23:00
calculate
taro'''.split("\n"))
    shift_database = {}
#     main('''1 31 3 1 2
# submit
# taro
# 3
# 01/31 09:00-12:00 02/01 10:00-12:00 02/02 13:00-18:00
# calculate
# taro'''.split("\n"))
