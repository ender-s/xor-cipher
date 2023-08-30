# xor-cipher
A command line tool written in Python that performs encryption/decryption of files using XOR function.

# Usage
To see usage of the tool, run the following command:
```bash
$ python3 main.py --help
```
Output:
```bash
usage: main.py [-h] -i INPUT -o OUTPUT -k KEY

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Path of the file to be encrypted/decrypted
  -o OUTPUT, --output OUTPUT
                        Path of the output file to be created (must be non-existent)
  -k KEY, --key KEY     The key to be used for encryption/decryption
```

# Record of a Sample Run
[![asciicast](https://asciinema.org/a/3694liGEtM878aJyUIhD9cDHU.svg)](https://asciinema.org/a/3694liGEtM878aJyUIhD9cDHU)