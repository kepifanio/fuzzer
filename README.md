Written by: Katherine Epifanio


Purpose:
        
        This program determines whether a given URL is vulnerable to
        reflected Cross-Site Scripting (XSS) by initiating an HTTP
        request and analyzing the response.

Files Included:
        
        fuzzer.py - Contains all source code.
        Fuzzing   - Directory of input text files from Daniel Miessler's
                    SecLists GitHub repository.
                    (https://github.com/danielmiessler/SecLists/tree/master/Fuzzing)

Compiling:
        
        python fuzzer.py


Usage:
        
        The command line does not accept additional arguments. Once
        the program is executed, it prompts the user to input...

        1.) a target URL, and
        2.) the name/path of the text file containing the attack
        strings to test.

        * An invalid URL/failure to make an HTTP request with the
          provided target URL results in the program quitting
        * An invalid file name/path entry results in the program
          quitting.


Acknowledgments:

        https://docs.python.org/3/library/http.client.html

        https://pypi.org/project/tabulate/
