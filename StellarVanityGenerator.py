# Import necessary modules
import argparse
from stellar_sdk import Keypair
import concurrent.futures
import os
import time

# Function to check if a character is valid in a Stellar address
def is_valid_char(c):
    return 'G' == c or '2' <= c <= '7' or 'A' <= c <= 'Z'

# Function to generate addresses until one matches the desired pattern
def generate_vanity_address(pattern, is_prefix, stats):
    while True:
        keypair = Keypair.random()  # Generate a new address
        stats['total'] += 1  # Update the total count of generated addresses
        # Check if the address matches the desired pattern
        if (is_prefix and keypair.public_key.startswith(pattern)) or \
           (not is_prefix and keypair.public_key.endswith(pattern)):
            stats['valid'] += 1  # Update the count of valid addresses
            return keypair  # Return the valid address
        else:
            stats['invalid'] += 1  # Update the count of invalid addresses

# Function to write the results to a file
def write_to_file(public_key, secret_seed, stats, elapsed_time, filename):
    with open(f'{filename}.txt', 'a') as f:
        f.write("Public Key: " + public_key + "\n")
        f.write("Secret Seed: " + secret_seed + "\n")
        f.write(f"Total keys generated: {stats['total']}\n")
        f.write(f"Valid keys found: {stats['valid']}\n")
        f.write(f"Invalid keys found: {stats['invalid']}\n")
        f.write(f"Time taken: {elapsed_time} seconds\n")
        f.write(f"Keys generated per second: {stats['total'] / elapsed_time}\n\n")

# Configure command line argument parsing
parser = argparse.ArgumentParser(description='Generate a Stellar vanity address.')
parser.add_argument('string', nargs='?', default='', help='The string to look for in the address. By default, the string is treated as a suffix.')
parser.add_argument('-p', '--prefix', action='store_true', help='If present, the string will be treated as a prefix instead of a suffix.')
parser.add_argument('-t', '--threads', type=int, default=os.cpu_count(), help='The number of threads to use.')
parser.add_argument('-s', '--save', action='store_true', help='If present, save the results to a file.')
args = parser.parse_args()

# Handle user input
if args.string == '':
    user_string = input("Enter the string: ")
    print("The string is:")
    print("[1] prefix")
    print("[2] suffix")
    prefix_or_suffix = input()
    is_prefix = prefix_or_suffix == '1'
    num_threads = int(input(f"Number of threads to use? [1-{os.cpu_count()}]: "))
    args.save = input("Do you want to save the results to a file (y/n)? ").lower() == 'y'
else:
    user_string = args.string
    is_prefix = args.prefix
    num_threads = args.threads

# Convert user string to uppercase
user_string = user_string.upper()

# Check if user string contains only valid characters
if not all(is_valid_char(c) for c in user_string):
    print("The string contains invalid characters.")
else:
    # If the string should be a prefix, add 'G' at the beginning
    if is_prefix:
        user_string = 'G' + user_string
    # Initialize statistics
    stats = {'total': 0, 'valid': 0, 'invalid': 0}
    while True:
        print("Starting the search for the vanity address...")
        start_time = time.time()  # Record the start time
        # Use multithreading to speed up address generation
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            future = executor.submit(generate_vanity_address, user_string, is_prefix, stats)
            keypair = future.result()  # Get the valid address
        elapsed_time = time.time() - start_time  # Calculate elapsed time
        # Print key information and statistics
        print("Public Key: " + keypair.public_key)
        print("Secret Seed: " + keypair.secret)
        keys_per_second = stats['total'] / elapsed_time
        print(f"Total keys generated: {stats['total']}")
        print(f"Valid keys found: {stats['valid']}")
        print(f"Invalid keys found: {stats['invalid']}")
        print(f"Time taken: {elapsed_time} seconds")
        print(f"Keys generated per second: {keys_per_second}")
        # If the user chose to save the results, write the information to a file
        if args.save:
            write_to_file(keypair.public_key, keypair.secret, stats, elapsed_time, user_string)
        # Ask the user if they want to continue the search
        continue_search = input("Do you want to continue the search (y/n)? ").lower() == 'y'
        if not continue_search:
            break  # If the user doesn't want to continue, break the loop
