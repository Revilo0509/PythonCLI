import PythonCli
import time

# Test the CreateMeny function
print(PythonCli.CreateMeny(["Option 1","Option 2","Option 3"],MenyName="Meny Name"))

# Test all loading bar functions
PythonCli.CreateLoadingBar("Loading Bar Name")

for i in range(100):
    PythonCli.UpdateLoadingBar("Loading Bar Name",i)
    time.sleep(0.1)

PythonCli.RemoveLoadingBar("Loading Bar Name")