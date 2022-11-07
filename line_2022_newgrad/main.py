import sys
from functools import cmp_to_key,total_ordering

@total_ordering
class MyDatetime:
    def __init__(self,d:str,time_str:str):
        self.d = int(d)
        h,m = list(map(int,time_str.split(":")))
        self.h = h
        self.m = m
    
    def after_x_minites(self,x:int):
        h,m = self.h + (self.m+x) // 60, (self.m + x) % 60
        return MyDatetime(self.d, f"{str(h).zfill(2)}:{str(m).zfill(2)}")
    
    def time_str(self):
        return f"{str(self.h).zfill(2)}:{str(self.m).zfill(2)}"
    
    def __str__(self):
        return f"{self.d} {self.time_str()}"

    def datetime_to_minute(self):
        return self.d * 24 * 60 + self.h * 60 + self.m

    def __eq__(self, o):
        return o.datetime_to_minute() == self.datetime_to_minute()
    
    def __lt__(self, o):
        return o.datetime_to_minute() > self.datetime_to_minute()

class Sales:
    def __init__(self,price:int,d:MyDatetime):
        self.d = d
        self.price = price


class Guest:
    def __init__(self, guest_id: str,d:str,check_in_time:str,number_of_guests:int,days_to_accomodate:int):
        self.guest_id = guest_id
        self.check_in_time = MyDatetime(d, check_in_time)
        self.number_of_guests = number_of_guests
        self.days_to_accomodate = days_to_accomodate

class Room:

    def __init__(self, room_id: str, room_type: str, capacity: int, price_in_weekday: int):

        self.room_id = room_id
        self.room_type = room_type
        self.capacity = capacity
        self.price_in_weekday = price_in_weekday
        # room status
        self.occupied = False
        # self.cleaning = False # TODO: 最終チェックアウト時刻から30m後かどうかで判定する


        self.last_check_out:MyDatetime = None
        self.cleaning_finish_time:MyDatetime = None

        # current guest
        self.current_guest:Guest = None


    def checkin_guest(self,g:Guest):
        self.current_guest = g
        self.occupied = True
    
    def checkout_guest(self,d:str,time_str:str):
        self.current_guest = None
        self.occupied = False
        self.last_check_out = MyDatetime(d, time_str)
    
    def set_cleaning_finish_time(self,d:MyDatetime):
        self.cleaning_finish_time = d
    
    def is_cleaning(self,cur:MyDatetime):
        if self.last_check_out is None:
            return False
        return self.last_check_out <= cur < self.cleaning_finish_time
    
    def is_occupied(self,cur:MyDatetime):
        if self.is_cleaning(cur):
            return False
        if self.current_guest == None:
            return False
        return True

    def is_vacant(self,cur:MyDatetime):
        return (not self.is_cleaning(cur)) and (not self.is_occupied(cur))

class Hotel:
    def __init__(self, rooms: list[Room],cleaners:int):
        # self.rooms = rooms
        self.room_id_2_rooms = {
            room.room_id: room for room in rooms
        }
        self.guest_id_2_guests = {}
        self.sales:list[Sales] = []

        self.cleaning_tasks:list[Room] = [
            [] for _ in range(cleaners)
        ]

    def check_in(self,d:str, time:str, guest_id:str, room_id:str, n:int, days:int):
        guest = Guest(guest_id, d, time, n, days)
        self.guest_id_2_guests[guest_id] = guest
        self.room_id_2_rooms[room_id].checkin_guest(guest)
    
    def assign_cleaning_task(self,room_id:str,checkout_time:MyDatetime) -> tuple[MyDatetime,MyDatetime]: # room_idの清掃が終わる時間を返す
        
        clener_id = -1 
        fastest_cleeaning_start_time = None
        for i in range(len(self.cleaning_tasks)):
            tasks = self.cleaning_tasks[i]
            
            if len(tasks) == 0:
                fastest_cleeaning_start_time = checkout_time
                clener_id = i
                break
            elif tasks[-1].cleaning_finish_time <= checkout_time: #  手が空いている清掃員が存在する
                fastest_cleeaning_start_time = checkout_time
                clener_id = i
                break
            else:
                if fastest_cleeaning_start_time == None:
                    fastest_cleeaning_start_time = tasks[-1].cleaning_finish_time
                    clener_id = i
                else:
                    if fastest_cleeaning_start_time > tasks[-1].cleaning_finish_time:
                        fastest_cleeaning_start_time = tasks[-1].cleaning_finish_time
                        clener_id = i
        
        # cleaner_idさんに清掃をさせる
        
        cleaning_finish_time = fastest_cleeaning_start_time.after_x_minites(30)
        self.room_id_2_rooms[room_id].set_cleaning_finish_time(cleaning_finish_time)
        
        self.cleaning_tasks[clener_id].append(self.room_id_2_rooms[room_id])
        

        return fastest_cleeaning_start_time, cleaning_finish_time


    def check_out(self,d:str, time:str,  guest_id:str, room_id:str) -> tuple[MyDatetime,MyDatetime]: # room_idの清掃を始める時間と終わる時間を返す
        checkout_time = MyDatetime(d, time)
        sale = Sales(self.calculate_price(guest_id, room_id), MyDatetime(d, time))
        self.sales.append(sale)
        self.room_id_2_rooms[room_id].checkout_guest(d,time)
        return self.assign_cleaning_task(room_id, checkout_time)
    
    def exist_room(self,room_id):
        return room_id in self.room_id_2_rooms

    def exist_guest(self,guest_id):
        return guest_id in self.guest_id_2_guests
    
    def is_guest_using_the_room(self,guest_id,room_id):
        r = self.room_id_2_rooms[room_id]

        if r.current_guest == None:
            return False
        return r.current_guest.guest_id == guest_id
    
    def can_accomodate(self,room_id,n):
        r = self.room_id_2_rooms[room_id]
        return r.capacity >= n
    
    def is_occupied(self,room_id):
        r = self.room_id_2_rooms[room_id]
        return r.occupied
    
    def is_cleaning(self,room_id,d,time_str):
        r = self.room_id_2_rooms[room_id]
        cur = MyDatetime(d, time_str)
        return r.is_cleaning(cur)
    
    def calculate_price(self,guest_id,room_id):
        r = self.room_id_2_rooms[room_id]
        g = r.current_guest
        price = 0
        for d in range(g.check_in_time.d,g.check_in_time.d + g.days_to_accomodate):
            if (d + 1) % 7 == 0 or (d + 1) % 7 == 6:
                price += r.price_in_weekday * 1.5
            else:
                price += r.price_in_weekday

        return price
    
    def calculate_total_sales(self,from_time:MyDatetime,to_time:MyDatetime):
        total_sales = 0
        for sale in self.sales:
            if from_time.datetime_to_minute() <=sale.d.datetime_to_minute() < to_time.datetime_to_minute():
                total_sales += sale.price
        return total_sales

    def occupied_room_count(self,cur:MyDatetime):
        cnt = 0
        for k,v in self.room_id_2_rooms.items():
            if v.is_occupied(cur):
                cnt += 1
        return cnt
    
    def vacant_room_count(self,cur:MyDatetime):
        cnt = 0
        for k,v in self.room_id_2_rooms.items():
            if v.is_vacant(cur):
                cnt += 1
        return cnt

    def cleaning_room_count(self,cur:MyDatetime):
        cnt = 0
        for k,v in self.room_id_2_rooms.items():
            if v.is_cleaning(cur):
                cnt += 1
        return cnt

    

class HotelApp:
    @staticmethod
    def main(lines):
        N, M = list(map(int, lines[0].split()))
        # 部屋情報を読み込む
        rooms = []
        for i in range(1, N+1):
            room_id, room_type, cap, price_in_weekday = list(lines[i].split())
            rooms.append(Room(
                room_id, room_type, int(cap), int(price_in_weekday)
            )
            )

        hotel = Hotel(rooms=rooms,cleaners=M)

        msg = [] # [(time,msg),(time,msg) ...]
        # クエリを読み込む
        for i in range(N+1, len(lines)):
            query = list(lines[i].split())
            q_type = query[2]

            if q_type == "check-in":
                d, time, _, guest_id, room_id, n, days = list(lines[i].split())
                mstime = MyDatetime(d, time)
                n = int(n)
                days = int(days)
                if not hotel.exist_room(room_id):
                    msg.append((mstime,f"{d} {time} ERROR: {room_id} does not exist."))
                elif not hotel.can_accomodate(room_id, n):
                    msg.append((mstime,f"{d} {time} ERROR: {room_id} cannot accommodate {guest_id}."))
                elif hotel.is_cleaning(room_id,d,time):
                    msg.append((mstime,f"{d} {time} ERROR: {room_id} is being cleaned."))
                elif hotel.is_occupied(room_id):
                    msg.append((mstime,f"{d} {time} ERROR: {room_id} is being occupied."))
                else:
                    hotel.check_in(d, time, guest_id, room_id, n, days)
                    msg.append((mstime,f"{d} {time} {guest_id} successfully checked in to {room_id}."))
                    
            elif q_type == "check-out":
                d, time, _, guest_id, room_id = list(lines[i].split())
                mstime = MyDatetime(d, time)
                if not hotel.exist_room(room_id):
                    msg.append((mstime,f"{d} {time} ERROR: {room_id} does not exist."))
                elif not hotel.exist_guest(guest_id):
                    msg.append((mstime,f"{d} {time} ERROR: {guest_id} does not exist."))
                elif not hotel.is_guest_using_the_room(guest_id, room_id):
                    msg.append((mstime,f"{d} {time} ERROR: {guest_id} is not in {room_id}."))
                else:
                    price = hotel.calculate_price(guest_id, room_id)
                    
                    msg.append((mstime,f"{d} {time} {guest_id} has to pay {price} to leave {room_id}."))
                    
                    cleaning_start_time, cleaning_finish_time =  hotel.check_out(d, time,  guest_id, room_id)
                    
                    if cleaning_start_time > mstime:
                        msg.append((mstime,f"{d} {time} No cleaner is available."))

                    msg.append((cleaning_start_time,f"{d} {cleaning_start_time.time_str()} A cleaner is assigned to {room_id}."))

                    msg.append((cleaning_finish_time,f"{d} {cleaning_finish_time.time_str()} {room_id} has been cleaned."))
            elif q_type == "status":

                d, time, _ = list(lines[i].split())
                mstime = MyDatetime(d, time)
                msg.append((mstime,f"{d} {time} Vacant: {hotel.vacant_room_count(mstime)}, Cleaning in progress: {hotel.cleaning_room_count(mstime)}, Occupied: {hotel.occupied_room_count(mstime)}"))
            
            elif q_type == "sales":
                d, time, _, fd,ftime,td,ttime = list(lines[i].split())
                from_time = MyDatetime(fd, ftime)
                to_time = MyDatetime(td,ttime)
                total_sales = hotel.calculate_total_sales(from_time, to_time)
                mstime = MyDatetime(d, time)
                msg.append((mstime,f"{d} {time} Sales: {total_sales}"))
        
        def msg_cmp(a, b):
            if b[0] != a[0]: 
                return -1 if b[0] > a[0] else 1
            else:
                if a[1].endswith("cleaned."):
                    return -1
                elif b[1].endswith("cleaned."):
                    return 1
                else:
                    return 0

        msg = sorted(msg,key=cmp_to_key(msg_cmp))

        for _,m in msg:
            print(m)

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    HotelApp.main(lines)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
