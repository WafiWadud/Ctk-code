from sys import argv
from os import system
from time import sleep
for i in range(2):
	argv.append("")
system("set +v")
system(f"nohup {argv[1]} {argv[2]}")
