import getopt
import sys
from importlib.metadata import version
from pathlib import Path

from pipeline_validator.engine import run_rules


def get_version() -> str:
    """
    Get the version of the package
    """
    return version("asset-pipeline-validator")


def main() -> int:
    """
    Main method for pipeline validator
    """

    GREEN = "\033[32m"
    RED = "\033[31m"
    YELLOW = "\033[33m"
    RESET = "\033[0m"


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

        # Validating files by running through rules.
        print(f"Validating files in directory: {path}")
        violations = run_rules(path)
        for violation in violations:
            print(f"Violation found: {violation.rule_id} - "
                  f"{violation.message} - "
                  f"{violation.file_path}")

        # TODO: Print out list of items with [PASS] or [FAIL]
        print("Validating character folder: johnny_tigerfox")
        print(f"{GREEN}[PASS]{RESET} scenes/ folder exists")
        print(f"{RED}[FAIL]{RESET} textures/ folder missing")
        print(f"{RED}[FAIL]{RESET} exports/ folder missing")
        print(f"{GREEN}[PASS]{RESET} correct version names")
        print(f"{GREEN}[PASS]{RESET} no spaces in names")

    except getopt.error as err:
        print(str(err))
        return 2

    return 0

if __name__ == "__main__":
    raise SystemExit(main())