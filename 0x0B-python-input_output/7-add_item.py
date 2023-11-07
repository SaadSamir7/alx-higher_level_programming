#!/usr/bin/python3
import sys
from os.path import isfile
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

if isfile("add_item.json"):
    my_list = load_from_json_file("add_item.json")
else:
    my_list = []

for arg in sys.argv[1:]:
    my_list.append(arg)

save_to_json_file(my_list, "add_item.json")
