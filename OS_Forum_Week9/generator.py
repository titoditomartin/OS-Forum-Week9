import random

# Number of cylinder requests
num_requests = 1000
# Disk size
disk_size = 5000

# Open a file to write
with open('input_requests.txt', 'w') as file:
    for _ in range(num_requests):
        # Generate a random cylinder number between 0 and 4999
        request = random.randint(0, disk_size - 1)
        # Write the request to the file
        file.write(f"{request}\n")