from audioop import add
import difflib
import os
from colorama import Style, Fore

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

os.system('color')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"\n{bcolors.UNDERLINE}COMPARES FIRST LINE TO ALL FOLLOWING LINES, DIFFERRENCES HIGHLIGHTED{bcolors.ENDC}\n")
print(f"{Fore.RED}{bcolors.UNDERLINE}RED{bcolors.ENDC}{Style.RESET_ALL} means removed compared to first line")
print(f"{Fore.GREEN}{bcolors.UNDERLINE}GREEN{bcolors.ENDC}{Style.RESET_ALL} means addition compared to first line")
print(f"{Fore.YELLOW}{bcolors.UNDERLINE}YELLOW{bcolors.ENDC}{Style.RESET_ALL} means direct replacement compared to first line")

print("\nPulling data from test.txt...\n")

with open (script_dir+"\\test.txt", "r") as myfile:
        rawData = myfile.read().splitlines()
        data = list(filter(None, rawData))

for index,item in enumerate(data):
    if not index: continue

    addIssues = []
    addIssuesIndex = []
    subIssues = []
    subIssuesIndex = []

    prevPosition = -1
    print("\n\n")
    for y in range(100): print("-", end='')
    print(f"\n\n{bcolors.UNDERLINE}Compare Line {1} => {index+1}{bcolors.ENDC} :\n")  
    for i,s in enumerate(difflib.ndiff(data[index],data[0])):
        if s[0]==' ': continue
        elif s[0]=='+':
            print(u'Found missing {} at position {}\n'.format(s[-1],i))
            for k, j  in enumerate(data[index]):
                if k == i:
                    addIssues.append(s[-1])
                    addIssuesIndex.append(i)
        elif s[0]=='-':
            print(u'Found {} at position {}\n'.format(s[-1],i))
            for k, j  in enumerate(data[index]):
                if k == i:
                    subIssues.append(s[-1])
                    subIssuesIndex.append(i)

    addIssuesDict = dict(zip(addIssuesIndex, addIssues))
    subIssuesDict = dict(zip(subIssuesIndex, subIssues))
    # print(addIssuesDict)
    # print(subIssuesDict)

    addIssuesLen = len(addIssues)
    subIssuesLen = len(subIssues)

    offset = 0

    newLine = f""
    print(f"{bcolors.UNDERLINE}LINE {1}{bcolors.ENDC}:\n")
    print(data[0])
    print(f"\n{bcolors.UNDERLINE}LINE {index+1}{bcolors.ENDC}:\n")
    k = 0

    while True:
        if k in subIssuesDict.keys() and k+1 in addIssuesDict.keys():
            newLine+= f"{Fore.YELLOW}{bcolors.UNDERLINE}{subIssuesDict[k]}{bcolors.ENDC}{Style.RESET_ALL}"
            del addIssuesDict[k+1]
            del subIssuesDict[k]
            k += 2
            offset += 1

        elif k in addIssuesDict.keys() and not k in subIssuesDict.keys():
            newLine += f"{Fore.RED}{bcolors.UNDERLINE}{addIssuesDict[k]}{bcolors.ENDC}{Style.RESET_ALL}"
            del addIssuesDict[k]
            k += 1
        
        elif k in subIssuesDict.keys() and not k in addIssuesDict.keys():
            newLine+= f"{Fore.GREEN}{bcolors.UNDERLINE}{subIssuesDict[k]}{bcolors.ENDC}{Style.RESET_ALL}"
            del subIssuesDict[k]
            k += 1
            offset += 1

        else:
            try:
                # print(k)
                newLine += f"{data[0][k-offset]}"
                k += 1
            except: break

        # try: data[0][k]
        # except: break
    print(newLine)

print("\n")
for y in range(100): print("-", end='')
print("\n")
print(f"Differential highlighting complete.\n")
