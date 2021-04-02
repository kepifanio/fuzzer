# Written by: Katherine Epifanio

import requests
import sys
import textwrap
from tabulate import tabulate
tabulate.PRESERVE_WHITESPACE = True

xss_list = []

# Store each line of .txt file in xss_list. Each line represents
# an attack string. Exit program if file doesn't exist.
def read_list(fuzz_doc):
    try:
        with open(fuzz_doc) as file:
            text = file.readlines()
        for line in text:
            line = line.strip('\n')
            xss_list.append(line)
    except:
        sys.exit("\n** Can't open file '" + fuzz_doc +
        "': No such file in current directory. **\n")

# Issue the HTTP requests and check the response. If the URL
# and payload concatenation fail to produce a valid HTTP request,
# exit from program.
def fuzz(xss_list, target):
    table = []
    table.append(["ATTACK STRING", "STATUS CODE ", "RESPONSE"])
    try:
        for payload in xss_list:
            req = requests.post(target + payload)
            status = str(req.status_code)
            if payload in req.text:
                message = "payload FOUND in http request"
            else:
                message = "payload NOT FOUND in http request"
            pl_str = payload
            if len(pl_str) > 60:
                pl_str = pl_str[:61] + "..."
            final_str = "\"" + pl_str + "\""
            table.append([final_str, status, message])
        print("\n")
        print(tabulate(table, headers="firstrow", tablefmt="psql"))
        print("\n")

    except:
        sys.exit("** HTTP request failed. **\n")

# Read in user input. Call helper functions to store attack strings
# and initiate fuzzing.
def main():
    print("\n")
    print("                 ######### THE FUZZER #########\n")
    print("Checking for reflected Cross-Site Scripting (XSS) bugs...")

    target = input("\nEnter a target URL: ")
    fuzz_doc = input("\nEnter a wordlist to use for fuzzing (Include path if outside current directory): ")

    read_list(fuzz_doc)
    fuzz(xss_list, target)

main()
