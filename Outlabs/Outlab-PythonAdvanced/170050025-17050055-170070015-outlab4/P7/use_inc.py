from inc import ang_to_vec as atv
from inc import vec_to_ang as vta
import sys
import numpy as np

if __name__ == "__main__":
    if(len(sys.argv) < 3):
        print("Enter infile,outfile and choice")
        exit(1)
    infile_n = sys.argv[1]
    outfile_n = sys.argv[2]
    choice = sys.argv[3]
    infile = open(infile_n, "r")
    outfile = open(outfile_n, "w")
    i = np.loadtxt(infile, delimiter=",")
    try:
        p = i.shape[1]
    except:
        i = i.reshape((i.shape[0], 1))
    if(choice == '0'):
        if(i.shape[1] == 1):
            euler = atv(i)
            np.savetxt(outfile, euler, delimiter=",")
        else:
            print("Wrong dimensions")
            exit(1)
    else:
        if(i.shape[1] == 2):
            quaternion = vta(i)
            print(quaternion.shape)
            np.savetxt(outfile, quaternion, delimiter=",")
        else:
            print("Wrong dimensions")
            exit(1)
