import keyboard
import time

def ListLookUp(List, Thing):
    for i in range(len(List)):
        if List[i] == Thing:
            return i
    raise SyntaxError("The variable " + str(Thing) + " is not in the list " + str(List))

# Clear the console
def cls():
    print("\033[H\033[J", end="")

def CreateMeny(MenyOptions,MenyName="",ReturnINT=False,ClearOnExit=True):

    # Validates the input variables
    if type(MenyOptions) != list:
        raise TypeError("MenyOptions must be a list")
    if type(MenyName) != str:
        raise TypeError("MenyName must be a string")

    CurrentlySelected = 0
    Update = True

    while True:

        # Meny manuvering key triggers
        if keyboard.is_pressed('down') and not Update:
            Update = True
            if CurrentlySelected < len(MenyOptions) - 1:
                CurrentlySelected += 1

        if keyboard.is_pressed('up') and not Update:
            Update = True
            if CurrentlySelected > 0:
                CurrentlySelected -= 1

        if keyboard.is_pressed('enter') and not Update:
            if ClearOnExit:
                cls()
            if ReturnINT:
                return CurrentlySelected
            else:
                return MenyOptions[CurrentlySelected]

        # Draw the meny if Update is True
        if Update:
            Update = False
            cls()
            if MenyName != "":
                print(MenyName)
            for i in range(len(MenyOptions)):
                if i == CurrentlySelected:
                    print("->", MenyOptions[i])
                else:
                    print("  ", MenyOptions[i])
            time.sleep(0.1)


LoadingBarNameList,LoadingBarPercentageList = [], []
def CreateLoadingBar(LoadingBarName=""):

    # Validates the input variables
    if type(LoadingBarName) != str:
        raise TypeError("LoadingBarName must be a string")

    LoadingBarNameList.append(LoadingBarName)
    LoadingBarPercentageList.append(0)

def UpdateLoadingBar(LoadingBarName="", CompletionPercentage=0): 
    # TODO: Add functionality Update multiple loading bars at once

    # Validates the input variables
    if type(CompletionPercentage) != int:
        raise TypeError("CompletionPercentage must be an integer")
    if CompletionPercentage < 0 or CompletionPercentage > 100:
        raise ValueError("CompletionPercentage must be between 0 and 100")
    
    if LoadingBarName == "":
        if len(LoadingBarNameList) == 1:
            LoadingBarName = LoadingBarNameList[0]
        else:
            raise SyntaxError("LoadingBarName must be specified")

    LoadingBarIndex = ListLookUp(LoadingBarNameList, LoadingBarName)
    LoadingBarPercentageList[LoadingBarIndex] = CompletionPercentage

    cls()
    print(LoadingBarNameList[LoadingBarIndex])
    print("[" + "#" * LoadingBarPercentageList[LoadingBarIndex] + " " * (100 - LoadingBarPercentageList[LoadingBarIndex]) + "]")

def RemoveLoadingBar(LoadingBarName=""):

    if type(LoadingBarName) != str:
        raise TypeError("LoadingBarName must be a string")
    if LoadingBarName == "":
        raise SyntaxError("LoadingBarName must be specified")
    
    LoadingBarIndex = ListLookUp(LoadingBarNameList, LoadingBarName)
    LoadingBarNameList.pop(LoadingBarIndex)
    LoadingBarPercentageList.pop(LoadingBarIndex)

def RemoveAllLoadingBars():
    LoadingBarNameList.clear()
    LoadingBarPercentageList.clear()

global LoopUpdateCount
LoopUpdateCount = 0
def LoopUpdate():
    global LoopUpdateCount
    LoopUpdateCount += 1
    cls()
    print("Loop ran " + str(LoopUpdateCount) + " times")

def ResetLoopUpdate():
    global LoopUpdateCount
    LoopUpdateCount = 0

