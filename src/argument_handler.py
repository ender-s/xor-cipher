"""Define and parse the arguments expected from users."""

import argparse
import os


class ArgumentHandler:
    """A class for handling user-specified arguments."""

    def __init__(self) -> None:
        "Initialize ArgumentHandler with argument definitions."
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-i", "--input", type=str,
                                 help="Path of the file to be encrypted/decrypted",
                                 required=True)
        self.parser.add_argument("-o", "--output", type=str,
                                 help="Path of the output file to"
                                      " be created (must be non-existent)",
                                 required=True)
        self.parser.add_argument("-k", "--key", type=str,
                                 help="The key to be used for encryption/decryption",
                                 required=True)

    def validate(self, args: argparse.Namespace) -> None:
        """Validate the arguments specified by the user.

        :param args: Arguments parsed by ArgumentParser 
        :type args: argparse.Namespace
        """
        if not os.path.isfile(args.input):
            raise RuntimeError(f"No such file: {args.input}")

        if os.path.exists(args.output):
            raise RuntimeError(f"Output path must be non-existent: {args.output}")

    def parse(self) -> argparse.Namespace:
        """Return the parsed arguments.

        :return: Parsed arguments
        :rtype: argparse.Namespace
        """
        args = self.parser.parse_args()
        self.validate(args)
        return args
