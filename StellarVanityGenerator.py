import argparse
from stellar_sdk import Keypair
import concurrent.futures
import os
import time

# Function to check if a character is valid for a Stellar address
def is_valid_char(c):
    return 'G' == c or '2' <= c <= '7' or 'A' <= c <= 'Z'

# Function to generate a vanity address
def generate_vanity_address(pattern, is_prefix, stats):
    while True:
        # Generate a random keypair
        keypair = Keypair.random()
        # Increment the total count of generated keys
        stats['total'] += 1
        # Check if the public key starts with or ends with the pattern
        if (is_prefix and keypair.public_key.startswith(pattern)) or \
           (not is_prefix and keypair.public_key.endswith(pattern)):
            # If it does, increment the valid count and return the keypair
            stats['valid'] += 1
            return keypair
        else:
            # If it doesn't, increment the invalid count
            stats['invalid'] += 1

# Function to write the results to a file
def write_to_file(public_key, secret_seed, stats, elapsed_time):
    with open('results.txt', 'a') as f:
        f.write("Public Key: " + public_key + "\n")
        f.write("Secret Seed: " + secret_seed + "\n")
        f.write(f"Total keys generated: {stats['total']}\n")
        f.write(f"Valid keys found: {stats['valid']}\n")
        f.write(f"Invalid keys found: {stats['invalid']}\n")
        f.write(f"Time taken: {elapsed_time} seconds\n")
        f.write(f"Keys generated per second: {stats['total'] / elapsed_time}\n\n")

# Create a parser for the command line arguments
parser = argparse.ArgumentParser(description='Generate a Stellar vanity address.')
parser.add_argument('string', nargs='?', default='', help='The string to look for in the address. By default, the string is treated as a suffix.')
parser.add_argument('-p', '--prefix', action='store_true', help='If present, the string will be treated as a prefix instead of a suffix.')
parser.add_argument('-t', '--threads', type=int, default=os.cpu_count(), help='The number of threads to use.')
parser.add_argument('-s', '--save', action='store_true', help='If present, save the results to a file.')

# Parse the command line arguments
args = parser.parse_args()

# If no string was provided, enter interactive mode
if args.string == '':
    # Ask the user to enter a string
    user_string = input("Enter the string: ")

    # Ask the user if the string should be a prefix or a suffix
    is_prefix = input("Should the string be a prefix (y/n)? ").lower() == 'y'

    # Ask the user for the number of threads to use
    num_threads = int(input(f"Number of threads to use? [1-{os.cpu_count()}]: "))

    # Ask the user if they want to save the results to a file
    args.save = input("Do you want to save the results to a file (y/n)? ").lower() == 'y'
else:
    user_string = args.string
    is_prefix = args.prefix
    num_threads = args.threads

# Convert the string to uppercase
user_string = user_string.upper()

# Check that all characters are valid
if not all(is_valid_char(c) for c in user_string):
    print("The string contains invalid characters.")
else:
    # If it's a prefix, automatically add the 'G'
    if is_prefix:
        user_string = 'G' + user_string

    # Initialize the stats
    stats = {'total': 0, 'valid': 0, 'invalid': 0}

    while True:
        # Print a message indicating that the search has started
        print("Starting the search for the vanity address...")
        
        # Record the start time
        start_time = time.time()

        # Create a thread pool
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            future = executor.submit(generate_vanity_address, user_string, is_prefix, stats)
            keypair = future.result()

        # Calculate the elapsed time
        elapsed_time = time.time() - start_time

        print("Public Key: " + keypair.public_key)
        print("Secret Seed: " + keypair.secret)

        # Calculate the keys generated per second
        keys_per_second = stats['total'] / elapsed_time

        # Print the stats
        print(f"Total keys generated: {stats['total']}")
        print(f"Valid keys found: {stats['valid']}")
        print(f"Invalid keys found: {stats['invalid']}")
        print(f"Time taken: {elapsed_time} seconds")
        print(f"Keys generated per second: {keys_per_second}")

        # Write the keys and stats to the file if the --save option was specified
        if args.save:
            write_to_file(keypair.public_key, keypair.secret, stats, elapsed_time)

        # Ask the user if they want to continue the search
        continue_search = input("Do you want to continue the search (y/n)? ").lower() == 'y'
        if not continue_search:
            break
