from logging import raiseExceptions
import os
import shutil

# const char *CRT_treeStrUtf8[TREE_STR_COUNT] = {
#    '\xe2\x94\x80', // TREE_STR_HORZ ─
#    '\xe2\x94\x82', // TREE_STR_VERT │
#    '\xe2\x94\x9c', // TREE_STR_RTEE ├
#    '\xe2\x94\x94', // TREE_STR_BEND └
#    '\xe2\x94\x8c', // TREE_STR_TEND ┌
#    '+',            // TREE_STR_OPEN +
#    '\xe2\x94\x80', // TREE_STR_SHUT ─

treeStrUtf8 = [
    '─',  #    '\xe2\x94\x80', // TREE_STR_HORZ ─
    '│',  #    '\xe2\x94\x82', // TREE_STR_VERT │
    '├',  #    '\xe2\x94\x9c', // TREE_STR_RTEE ├
    '└',  #    '\xe2\x94\x94', // TREE_STR_BEND └
    '┌',  #    '\xe2\x94\x8c', // TREE_STR_TEND ┌
    '+',  #    '+',            // TREE_STR_OPEN +
    '─'  #    '\xe2\x94\x80', // TREE_STR_SHUT ─
]

def welcome():
    print('Welcome to AtCoder Test Formatter!!')
    print('We provide a nice tool to convert easily AtCoder testcases in order to bring it up into DMOJ test data.')
    print('AtCoder Test Format :')
    print('A')
    print('├─ in')
    print('│  ├─ 00_sample_00.txt')
    print('│  ├─ 01_random_00.txt')
    print('│  ├─ 01_random_01.txt')
    print('│  ├─ ...')
    print('├─ out')
    print('│  ├─ 00_sample_00.txt')
    print('│  ├─ 01_random_00.txt')
    print('│  ├─ 01_random_01.txt')
    print('│  ├─ ...')

    print()
    
    print('DMOJ Test Format :')
    print('A')
    print('├─ 01.in')
    print('├─ 01.out')
    print('├─ 02.in')
    print('├─ 02.out')
    print('├─ 03.in')
    print('├─ 03.out')
    print('├─ ...')

    print()

    print("Note: we will index testcases based on lexicographical order of tests' name.")

def digit_index(x : int, max_digit : int) -> str:
    s = str(x)
    while len(s) < max_digit:
        s = "0" + s
    return s

def main():
    welcome()

    FilePath = input('Path of test file : ')
    ProblemName = input('Name of the problem : ')
    ResultPath = input('Path of the resulting file (if leave blank then it will store in root folder) : ')
    if (ResultPath == ''):
        ResultPath = '.'

    

    try:
        if os.path.exists(f'{FilePath}/'):
            files = ['in', 'out']
            for name in files:
                if not os.path.exists(f'{FilePath}/{name}/'):
                    raise Exception(f'Not found {name} folder')
        else:
            raise Exception('Not found test folder')
    except Exception as e:
        print(e)
        exit(0)
        pass
    
    try:
        FolderPath = f'{ResultPath}/DMOJ_{ProblemName}/'
        if os.path.exists(FolderPath):
            shutil.rmtree(FolderPath)
    except Exception as e:
        print(e)
        print(f'You should run this program in administrator mode or delete folder "{ResultPath}/DMOJ_{ProblemName}/" first!!')
        exit(0)

    InputFiles = os.listdir(f'{FilePath}/in/')

    OutputFiles = os.listdir(f'{FilePath}/out/')

    ValidFiles = list()
    
    for filename in InputFiles:
        if filename in OutputFiles:
            ValidFiles.append(filename)

    # sort all valid FileNames in lexicographical order

    ValidFiles.sort() 

    # ONLY for debug
    print('Valid files: ', ValidFiles)

    # get the maximum number digits of |ValidFiles|

    max_digit = 0
    n = int(len(ValidFiles))
    while n > 0:
        max_digit += 1
        n = int(n / 10)

    # Create result folder
    
    os.makedirs(f'{ResultPath}/DMOJ_{ProblemName}/')

    for i in range(len(ValidFiles)):
        InputSourcePath = f'{FilePath}/in/{ValidFiles[i]}'
        InputDestionationPath = f'{ResultPath}/DMOJ_{ProblemName}/{digit_index(i+1, max_digit)}.in'

        InputResult = shutil.copyfile(InputSourcePath, InputDestionationPath)
        
        OutputSourcePath = f'{FilePath}/out/{ValidFiles[i]}'
        OutputDestionationPath = f'{ResultPath}/DMOJ_{ProblemName}/{digit_index(i+1, max_digit)}.out'

        OutputResult = shutil.copyfile(OutputSourcePath, OutputDestionationPath)

        # ONLY for debug
        print(f'{i} := {InputResult} & {OutputResult}')
    
    print('OK')

if __name__ == '__main__':
    main()