# Stellar Vanity Address Generator

This Python script generates "vanity" addresses for the Stellar network. A vanity address is a public address that contains a specific string.

## Features

- Generate a Stellar vanity address with a specific string.
- The string can be a prefix or a suffix of the address.
- Multithreaded address generation.
- Option to save the results to a file.

## Requirements

- Python 3
- `stellar_sdk` Python library
- `argparse` Python library

You can install the required Python libraries using pip:

```bash
pip install stellar_sdk argparse
```

## Usage

You can run the script with command line arguments or in interactive mode.

### Command Line Arguments

- `string`: The string to look for in the address. By default, the string is treated as a suffix.

- `-p` or `--prefix`: If present, the string will be treated as a prefix instead of a suffix.

- `-t` or `--threads`: The number of threads to use. By default, the script uses the maximum number of threads available on your computer.

- `-s` or `--save`: If present, save the results to a file.

  

Here are some examples of how to run the script with command line arguments:


```bash
python StellarVanityGenerator.py xlm -p -t 4 -s
```
This command will search for ‘xlm’ **PREFIX** in the address, use 4 threads, and save the results to a file.




```bash
python StellarVanityGenerator.py xlm -t 4
```
This command will search for ‘xlm’ **SUFFIX** in the address, use 4 threads, and print the results to the console.



### Interactive Mode

If no string is provided when running the script, the script enters interactive mode. In interactive mode, the script will ask you to enter a string, decide if the string should be a prefix or a suffix, specify the number of threads to use, and decide if you want to save the results to a file.

Here’s how to run the script in interactive mode:

```bash
python StellarVanityGenerator.py
```



## Donations

If you found this script helpful and would like to show your appreciation, consider making a donation to the following Stellar address: `YOUR_STELLAR_ADDRESS_HERE`. Your support helps maintain and improve this project. Thank you! 😊



## Security Warnings

- Vanity addresses can potentially be less secure than randomly generated addresses. An attacker who knows the pattern you used could try to generate the same address and gain access to your funds.
- Vanity address generators can be a target for malware. Only run this script in a secure, offline environment.
- Always verify the integrity of your vanity addresses and consider the potential security risks before using them.



## Disclaimer

This script is provided "as is", without warranties of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.



## License

This project is licensed under the terms of the MIT license.
