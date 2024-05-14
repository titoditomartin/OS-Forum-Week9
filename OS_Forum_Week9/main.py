import sys
from algorithms import fcfs, scan, c_scan, optimized_fcfs, optimized_scan, optimized_c_scan

def read_requests(file_path):
    with open(file_path, 'r') as file:
        requests = [int(line.strip()) for line in file.readlines()]
    return requests

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <initial_head_position> <input_file>")
        sys.exit(1)

    head_start = int(sys.argv[1])
    file_path = sys.argv[2]
    requests = read_requests(file_path)

    # Original algorithms
    print("Original FCFS Head Movements:", fcfs(requests, head_start))
    print("Original SCAN Head Movements:", scan(requests, head_start))
    print("Original C-SCAN Head Movements:", c_scan(requests, head_start))

    # Optimized algorithms
    print("Optimized FCFS Head Movements:", optimized_fcfs(requests, head_start))
    print("Optimized SCAN Head Movements:", optimized_scan(requests, head_start))
    print("Optimized C-SCAN Head Movements:", optimized_c_scan(requests, head_start))

if __name__ == '__main__':
    main()
