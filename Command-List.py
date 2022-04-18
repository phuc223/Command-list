import os 
import time

list_commands = []
command_numbers = int(input("Please input your command number list: "))
x = int
for x in range(0, command_numbers):
    commands = input("Please input your command: ")
    list_commands.append(commands)

print("The command list: ", list_commands)
n = int
n = 0
for x in range(n, command_numbers):
    os.system(list_commands[n])
    n = n + 1
