import sys
import subprocess

def clean(cmake = "/Applications/CLion.app/Contents/bin/cmake/mac/aarch64/bin/cmake", folder="cmake-build-debug"):
    """Command that cleans the build env to allow for a new build \n
        Command run: cmake --build cmake-build-debug --target clean
    """
    result = subprocess.run([cmake, "--build", folder, "--target", "clean"], capture_output=True, text=True)

    print(result.stdout)
    print(result.stderr)
    pass

def build(cmake = "/Applications/CLion.app/Contents/bin/cmake/mac/aarch64/bin/cmake", folder="cmake-build-debug"):
    """Command that builds the python lib \n
        Command run: cmake --build cmake-build-debug --target clean
    """
    result = subprocess.run([cmake, "--build", folder, "--target", "finProj", "-j", "10"], capture_output=True, text=True)

    print(result.stdout)
    print(result.stderr)
    pass


def main():
    """Main entry point of the program."""
    if len(sys.argv) < 2:
        print("ERROR: Not enough arugments")
        print("add help to view arguements")
        exit(1)
    
    match sys.argv[1]:
        case "help":
            print("""Usage:
            help: show this message
            clean: clean c++ code
            build: build python library
            combo: both commands""")
        case "clean":
            clean()
        case "build":
            build()
        case "combo":
            clean()
            build()
        case _:
            print("ERROR: unknown commands")
            print("use help to view aruguments")
            exit(1)


if __name__ == "__main__":
    main()