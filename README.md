# Stellar Vanity Address Generator

This Python script generates Stellar addresses that match a user-specified pattern. The pattern can be a prefix or a suffix of the Stellar address. The results are appended to a text file named 'results.txt', which is saved in the same directory as the script.

## Description

The script uses the `stellar_sdk` library to generate Stellar key pairs. It continuously generates new key pairs until it finds a public key that matches the specified pattern. The script supports parallel execution using a thread pool, the number of which can be specified by the user. The results, including the generated keys and statistics, are appended to a text file.

## Instructions

1. Make sure you have Python installed.
2. Install the necessary Python packages. You can do this either directly or from the `requirements.txt` file:
    - To install directly, run `pip install stellar_sdk`.
    - To install from the `requirements.txt` file, run `pip install -r requirements.txt`.
3. Run the script with `python3 script.py`.
4. When prompted, enter the string you want to search for in the Stellar address.
5. Specify whether the string should be a prefix or a suffix of the address.
6. Enter the number of threads you want to use.
7. The script will continue to generate addresses until it finds one that matches the pattern. You can stop the search at any time by answering 'n' when asked if you want to continue the search.
8. The search results, including the generated keys and statistics, are appended to the 'results.txt' file in the same directory as the script.

**IMPORTANT: It is strongly recommended to destroy the 'results.txt' file after use to prevent unauthorized access to the generated keys.**

## Donations

If you found this script helpful and would like to show your appreciation, consider making a donation to the following Stellar address: `YOUR_STELLAR_ADDRESS_HERE`. Your support helps maintain and improve this project. Thank you! 😊

## Security Warnings

- Vanity addresses can potentially be less secure than randomly generated addresses. An attacker who knows the pattern you used could try to generate the same address and gain access to your funds.
- Vanity address generators can be a target for malware. Only run this script in a secure, offline environment.
- Always verify the integrity of your vanity addresses and consider the potential security risks before using them.

## Disclaimer

This script is provided "as is", without warranties of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.
