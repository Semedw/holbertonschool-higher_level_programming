#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct
    except Exception as e:
        print(f"Excemption: {e}", file=sys.stderr)
        return None
