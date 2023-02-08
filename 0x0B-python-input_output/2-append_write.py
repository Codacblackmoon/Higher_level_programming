#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, mode="a", encoding="utf-8") as f:
        return(f.write(text))
