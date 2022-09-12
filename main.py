import sys
import Resources.Services.Timer as tm

def main():
    tm.get_answer_Time()


if __name__ == '__main__':
    if(len(sys.argv)==1):
        print("Incorrect execution:\tNo Arguments\n")
        print("For help, enter the following argument:")
        print("\tpython3 Obtain_Data.py -h")

    elif(len(sys.argv)==2 and sys.argv[1]=="-h"):
        print("\t\t\t~~~~~~~~")
        print("\t\t\t| Help |")
        print("\t\t\t~~~~~~~~\n")
        print("For correct execution of the program, you must enter the following arguments:\n")
        print("\tpython3 Obtain_Data.py -i [filename] -th [number]\n")
        print("Example: python3 Obtain_Data.py -i sequences.txt -th 0.5")
        print("Because of problems nature, threshold must be a number between 0 and 1")

    elif(len(sys.argv)==2 and sys.argv[1]=="-t"):
        main()
    else:
        print("Incorrect execution")
        print("For help, enter the following argument:")
        print("python3 Obtain_Data.py -h")