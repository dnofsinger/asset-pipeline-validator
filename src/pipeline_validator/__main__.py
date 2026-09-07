from importlib.metadata import version
from pathlib import Path
import sys, getopt


def get_version() -> str:
    """
    Get the version of the package
    """
    return version("asset-pipeline-validator")


def main() -> int:
    """
    Main method for pipeline validator
    """

    args = sys.argv[1:]
    options = "hv"
    long_options = ["help", "version"]

    try:
        arguments, values = getopt.getopt(args, options, long_options)
        for currentArg, currentVal in arguments:
            if currentArg in ("-h", "--help"):
                print(
                    "Usage: python -m pipeline_validator [options] <file_paths>\n"
                    "Options:\n"
                    "  -h, --help    Show this help message and exit\n"
                    "  -v, --version Show the version of the package and exit\n"
                    "Arguments:\n"
                    "  <file_paths>  One or more file paths to validate\n"
                )
                return 0
            elif currentArg in ("-v", "--version"):
                print("Asset Pipeline Validator version:", get_version())
                return 0

        if len(values) != 1:
            print("Error: Please provide exactly one file path to validate.")
            return 2

        path = Path(values[0])

        if not path.exists():
            print(f"Error: The file path '{path}' does not exist.")
            return 2

        if not path.is_dir():
            print(f"Error: The file path '{path}' is not a directory.")
            return 2

        #TODO: Implement the actual validation logic here.
        print(f"TODO! Validating files in directory: {path}")

    except getopt.error as err:
        print(str(err))
        return 2

    return 0

if __name__ == "__main__":
    raise SystemExit(main())