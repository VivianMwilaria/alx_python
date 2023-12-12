import sys

def print_arguments(argv):
    num_args = len(argv)

    if num_args == 0:
        print("0 arguments.")
        
    else:
        print(f"{num_args} argument{'s' if num_args > 1 else ''}:")
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    print_arguments(sys.argv[1:])
