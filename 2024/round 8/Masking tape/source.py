import sys

# Define helper functions
def sub_1020():
    var_8 = 0
    # jump -> nullptr (No action in Python, as we don't deal with null pointers in the same way)

def sub_1030():
    var_8 = 0
    return sub_1020()

def sub_1040():
    var_8 = 1
    return sub_1020()

def sub_1050():
    var_8 = 2
    return sub_1020()

def sub_1060():
    var_8 = 3
    return sub_1020()

def sub_1070():
    var_8 = 4
    return sub_1020()

def __cxa_finalize(d):
    return __cxa_finalize(d)

def puts(str):
    # In Python, we use print() instead of puts
    print(str)
    return len(str)

def strlen(arg1):
    # Python's len() is equivalent to strlen
    return len(arg1)

def printf(format, *args):
    # Python's print() is more flexible, similar to printf
    print(format % args)
    return 0

def strcmp(arg1, arg2):
    # Python's string comparison can be done with '=='
    if arg1 == arg2:
        return 0
    elif arg1 < arg2:
        return -1
    else:
        return 1

def malloc(bytes):
    # Python's memory allocation works automatically via lists/arrays, but we can simulate it
    return bytearray(bytes)

def register_tm_clones():
    return

def deregister_tm_clones():
    return

def __do_global_dtors_aux():
    global __TMC_END__
    if __TMC_END__:
        return
    if __cxa_finalize:
        __cxa_finalize(__dso_handle)
    deregister_tm_clones()
    __TMC_END__ = 1

def frame_dummy():
    return register_tm_clones()

def main(argc, argv, envp):
    if argc == 2:
        rax_5 = argv[1]
        bytes = strlen(rax_5) + 1
        rax_9 = malloc(bytes)
        rax_11 = malloc(bytes)

        for i in range(bytes):
            char_val = rax_5[i]
            char_val = (char_val <= 3) or (char_val >= 5)

            if not (char_val & 1):
                rax_9[i] = char_val & 0xcc
                rax_11[i] = char_val & 0x33
            else:
                rax_9[i] = char_val & 0x33
                rax_11[i] = char_val & 0xcc

        rax_45 = strcmp(enc1, rax_9)
        if not rax_45:
            rax_47 = strcmp(enc2, rax_11)

        if rax_45 or rax_47:
            puts("wrong")
        else:
            puts("congratz")
    else:
        printf("usage: %s <input>", argv[0])

    return 0

def _start(arg1, arg2, arg3):
    # Simulating __libc_start_main logic is difficult, as it's tied to a C runtime environment
    # Skipping this for simplicity

    def _fini():
        return _fini()

# Global variable for _do_global_dtors_aux logic
__TMC_END__ = False
__dso_handle = None  # In a Python context, this doesn't have the same meaning as in C
enc1 = b"some_encrypted_data_1"
enc2 = b"some_encrypted_data_2"

# Simulate the script's entry point
if __name__ == "__main__":
    main(len(sys.argv), sys.argv, None)
