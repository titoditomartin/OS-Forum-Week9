def fcfs(requests, head_start):
    head_movement = 0
    current_position = head_start
    
    for request in requests:
        head_movement += abs(request - current_position)
        current_position = request
    
    return head_movement

def optimized_fcfs(requests, head_start):
    requests.sort(key=lambda x: abs(x - head_start))
    head_movement = 0
    current_position = head_start
    
    for request in requests:
        head_movement += abs(request - current_position)
        current_position = request
    
    return head_movement

def scan(requests, head_start, disk_size=5000):
    requests.sort()
    head_movement = 0
    current_position = head_start
    
    left = [r for r in requests if r <= current_position]
    right = [r for r in requests if r > current_position]
    
    for request in reversed(left):
        head_movement += abs(current_position - request)
        current_position = request
    
    if right:
        head_movement += abs(current_position - right[0])
        current_position = right[0]
    
    for request in right:
        head_movement += abs(current_position - request)
        current_position = request
    
    return head_movement

def optimized_scan(requests, head_start, disk_size=5000):
    requests.sort()
    head_movement = 0
    current_position = head_start
    
    median_request = sorted(requests)[len(requests) // 2]
    
    if median_request < head_start:
        left = [r for r in requests if r <= current_position]
        right = [r for r in requests if r > current_position]
        
        for request in reversed(left):
            head_movement += abs(current_position - request)
            current_position = request
        
        if right:
            head_movement += abs(current_position - right[0])
            current_position = right[0]
        
        for request in right:
            head_movement += abs(current_position - request)
            current_position = request
    else:
        right = [r for r in requests if r >= current_position]
        left = [r for r in requests if r < current_position]
        
        for request in right:
            head_movement += abs(current_position - request)
            current_position = request
        
        if left:
            head_movement += abs(current_position - left[-1])
            current_position = left[-1]
        
        for request in reversed(left):
            head_movement += abs(current_position - request)
            current_position = request

    return head_movement

def c_scan(requests, head_start, disk_size=5000):
    requests.sort()
    head_movement = 0
    current_position = head_start
    
    right = [r for r in requests if r >= current_position]
    left = [r for r in requests if r < current_position]
    
    for request in right:
        head_movement += abs(current_position - request)
        current_position = request
    
    if left:
        head_movement += abs(current_position - (disk_size - 1)) + (disk_size - 1)
        current_position = 0
        
        head_movement += abs(current_position - left[0])
        current_position = left[0]
        
        for request in left:
            head_movement += abs(current_position - request)
            current_position = request
    
    return head_movement

def optimized_c_scan(requests, head_start, disk_size=5000):
    requests.sort()
    head_movement = 0
    current_position = head_start
    
    if (disk_size - 1 - head_start) < head_start:
        right = [r for r in requests if r >= current_position]
        left = [r for r in requests if r < current_position]
        
        for request in right:
            head_movement += abs(current_position - request)
            current_position = request
        
        if left:
            head_movement += abs(current_position - (disk_size - 1)) + (disk_size - 1)
            current_position = 0
            
            head_movement += abs(current_position - left[0])
            current_position = left[0]
            
            for request in left:
                head_movement += abs(current_position - request)
                current_position = request
    else:
        left = [r for r in requests if r <= current_position]
        right = [r for r in requests if r > current_position]
        
        for request in reversed(left):
            head_movement += abs(current_position - request)
            current_position = request
        
        if right:
            head_movement += current_position
            current_position = disk_size - 1
            
            head_movement += abs(current_position - right[-1])
            current_position = right[-1]
            
            for request in reversed(right):
                head_movement += abs(current_position - request)
                current_position = request

    return head_movement
