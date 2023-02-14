import sys

from pkg.mainentry import MainClass

executable_foldername = sys.argv[0]
print(f"Executable Foldername : {executable_foldername}")
mainClassExecutor = MainClass("From Self Executable Directory")
mainClassExecutor.delegate_implementations()
