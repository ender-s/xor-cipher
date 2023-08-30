"""The main module of the tool."""

import argparse

from argument_handler import ArgumentHandler
from cipher import Cipher


def main(args: argparse.Namespace) -> None:
    """Start the encryption/decryption.

    :param args: Parsed arguments specified by the user
    :type args: argparse.Namespace
    """
    input_path = args.input
    output_path = args.output
    key = args.key.encode("utf-8")

    Cipher.cipher(input_path, output_path, key)

if __name__ == "__main__":
    main(ArgumentHandler().parse())
