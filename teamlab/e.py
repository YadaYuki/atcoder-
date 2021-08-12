MAX_CAPACITY_PER_TRACK = 5000
baggage_arr = [i for i in range(1,801)]

print(baggage_arr)
track_num = 0
current_capacity = 0
for i in range(len(baggage_arr)-1,-1,-1):
  current_capacity += baggage_arr[i]
  print(current_capacity)
  if current_capacity > MAX_CAPACITY_PER_TRACK:
    print(track_num)
    track_num += 1
    current_capacity = baggage_arr[i]
    

print(track_num)
