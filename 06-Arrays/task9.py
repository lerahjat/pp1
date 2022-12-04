arr = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy', 'aaaaaaaaaaaaaaaaaaaaaa']
cur_max = 0
for i in range(len(arr)):
    if len(arr[i]) > cur_max:
        cur_max = len(arr[i])
        cur_name = arr[i]
print(cur_name)