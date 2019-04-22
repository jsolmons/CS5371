#!/home/angr/.virtualenvs/angr/bin/python3

import angr
import monkeyhex
import argparse
import logging

def getFuncAddress(cfg, funcName, plt=None ):
    found = [
        addr for addr,func in cfg.kb.functions.items()
        if funcName == func.name and (plt is None or func.is_plt == plt)
        ]
    if len( found ) > 0:
        return found[0]
    else:
        raise Exception("No address found for function : "+funcName)


def binary_function_fuzzer(program, function):

    # Load the program
    proj = angr.Project(program, load_options={'auto_load_libs':False})

    # Create the cfg to find the vulnerable function
    cfg = proj.analyses.CFG(fail_fast=True)

    # Get the function address
    funcAddr = getFuncAddress(cfg, function)

    # make the function stand alone - callable
    f = proj.factory.callable(funcAddr)

    # simulate fuzzing it
    f("good")
    known_good = f.result_state.addr

    f("hello")
    good = f.result_state.addr

    f("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    bad = f.result_state.addr

    if known_good == good:
        print("good == good")

    print("good = %s" % (good))
    print("bad = %s" % (bad))

def main():
    # Parse the arguments
    parser = argparse.ArgumentParser(description='Binary Function Fuzzer')
    parser.add_argument('-p', dest='program', required=True, help='Program Name')
    parser.add_argument('-f',dest='function', required=True, help='Function Name')
    args = parser.parse_args()

    # Set the verbosity
    # READ THIS - https://github.com/angr/angr-doc/blob/master/docs/faq.md
    logging.getLogger('angr').setLevel('ERROR')

    # Begin the BFF
    binary_function_fuzzer(args.program, args.function)

if __name__ == "__main__":
    main()
