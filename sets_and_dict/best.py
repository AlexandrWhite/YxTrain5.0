class Device:
    def __init__(self,id):
        self.id = id 
        self.parts_download = [False for i in range(k)]
        self.parts_cnt = 0
        self.from_device = [0 for i in range(n)]
        self.requests = []
        self.timeslot_cnt = 0 

 

    def send_request(self):  
        part_num = 0
        rarity = 101
        for i in range(k):
            if not self.parts_download[i]:
                if update_part_cnt[i] < rarity:
                    rarity = update_part_cnt[i] 
                    part_num = i 

        if rarity == 101: # не нужно грузить обновление
            return    

        donor_device = sorted(devices_parts[part_num], key = lambda x: (x.parts_cnt, x.id))[0]
        donor_device.recieve_request(self, part_num)
    
    def recieve_request(self, recipient,part_num):
        self.requests.append((recipient,part_num))
    
    def process_request(self):
        if self.requests:
            recipient_device, part = sorted(self.requests, key = lambda x: (-self.from_device[x[0].id],x[0].parts_cnt,x[0].id))[0]
            self.requests = []
            return self, recipient_device, part 
       





n,k = map(int, input().split())
update_part_cnt = [1 for i in range(k)]
devices_parts = [[] for i in range(k)]

all_devices = [Device(i) for i in range(n)]
all_parts_cnt = k

first_device = all_devices[0] 
first_device.parts_cnt = k 

for i in range(k):
    first_device.parts_download[i] = True 
for i in range(k):
    devices_parts[i].append(first_device) 


while True:

    is_end = True 
    for i in range(n):
        if all_devices[i].parts_cnt < k:
            all_devices[i].timeslot_cnt += 1
            is_end = False 
    if is_end:
        break

    for i in range(n):
        all_devices[i].send_request()
    
    upd_list = []
    
    for i in range(n):
        d = all_devices[i].process_request()
        if d is not None:
            upd_list.append(d)

    for donor, recipient_device, part in upd_list:
        update_part_cnt[part] += 1
        devices_parts[part].append(recipient_device)

        recipient_device.parts_cnt += 1
        recipient_device.parts_download[part] = True
        recipient_device.from_device[donor.id] += 1



for device in all_devices[1:]:
    print(device.timeslot_cnt,end=' ')