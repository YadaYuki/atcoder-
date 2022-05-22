from collections import defaultdict
import sys
from copy import deepcopy
# USER_INPUT_TYPE
ORDER_INPUT = 0
COMPLETE_INPUT = 1

# MACHINE_STATE
AVAILABLE = "available"
BUSY = "busy"


size_to_amount = {
    "S":300,
    "M":500,
    "L":700,
}

class MachineRequest:
    def __init__(self,amount,drink,orders_related):
        self.amount = amount
        self.drink = drink
        self.orders_related = orders_related

class Machine:
    
    def __init__(self,machine_id,S,T):
        self.machine_id = machine_id
        self.S = S
        self.T = T
        self.__status = 'available' # available, busy
        self.__cur_request = None
    
    def make_drink(self,machine_request:MachineRequest):
        self.__status = 'busy'
        self.__cur_request = deepcopy(machine_request)

    def complete_making(self):
        self.__status = 'available'
        cur_request = deepcopy(self.__cur_request)
        self.__cur_request = None
        return cur_request

    @property
    def status(self):
        return self.__status


class Order:
    def __init__(self,order_id,order_drink,size,time):
        self.order_id = order_id
        self.order_drink = order_drink
        self.size = size
        self.time = time


class DrinkShopApp:    
    def __init__(self,X,N,M,S,T,K,drinks,inputs):
        # define variables
        self.X = X
        self.N = N
        self.S = S
        self.machines = [Machine(i+1,S,T) for i in range(M)]
        self.pending_orders = []
        self.K = K 
        self.drinks = drinks
        self.inputs = inputs
    
    def main(self):
        # main process
        order_ids = defaultdict(bool)
        drinks_dict = {drink:True for drink in self.drinks}

        for user_input in self.inputs:
            if self.__get_user_input_type(user_input) == ORDER_INPUT:
                order_id,order_drink,size,time = user_input.split()
                
                # check Error
                if order_drink not in drinks_dict:
                    print(f'ERROR: item named {order_drink} does not exist.')
                    continue
                if order_id in order_ids:
                    print('ERROR: reference number duplicates.')
                    continue 

                # add order
                order_ids[order_id] = True

                # process order
                order = Order(order_id,order_drink,size,time)
                available_machine_id = self.__get_available_machine_idx() # 利用可能なマシンのインデックスを取得
                if available_machine_id is not None: 
                    # 利用可能なマシンがある場合
                    amount = size_to_amount[size]
                    self.machines[available_machine_id].make_drink(MachineRequest(amount, order_drink, orders_related=[order_id]))
                    print(f"make: {self.machines[available_machine_id].machine_id} {order_drink} {size_to_amount[size]}")
                else:
                    self.pending_orders.append(order)

            else: # complete input
                _,machine_id = user_input.split()
                machine_id = int(machine_id)
                completed_request = self.machines[machine_id-1].complete_making()
                print(f"serve to: {' '.join(completed_request.orders_related)}")

                # pending_ordersを処理する
                if len(self.pending_orders) > 0:
                    order = self.pending_orders.pop(0) 
                    amount = size_to_amount[order.size]
                    orders_related = [order.order_id]
                    # Sを超えない かつ orderと同じdrinkであるpending_ordersを先頭から追加していく
                    for pending_order in self.pending_orders:
                        if pending_order.order_drink == order.order_drink:
                            pending_order_amount = size_to_amount[pending_order.size]
                            if pending_order_amount + amount <= self.S:
                                amount += pending_order_amount
                                orders_related.append(pending_order.order_id)
                                self.pending_orders.remove(pending_order)
                            else:
                                break
                    print(f"make: {machine_id} {order.order_drink} {amount}")
                    self.machines[machine_id-1].make_drink(MachineRequest(amount, order.order_drink, orders_related=orders_related))

    def __get_available_machine_idx(self):
        for machine_id,machine in enumerate(self.machines):
            if machine.status == AVAILABLE:
                return machine_id
        return None

    def __get_user_input_type(self,input_str):
        if input_str.startswith('complete'):
            return COMPLETE_INPUT
        return ORDER_INPUT
    




def main():
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.

    X = int(input())
    N,M,S,T,K = None,None,None,None,None
    if X == 1:
        N,M,S,T,K = map(int,input().split())
    else:
        N,M,S,T = map(int,input().split())
    drinks = list(input().split())
    inputs = []
    try:
        for _ in range(13):
            inputs.append(input())
    except EOFError:
        pass
    drink_shop_app = DrinkShopApp(X,N,M,S,T,K,drinks,inputs)
    drink_shop_app.main()


main()