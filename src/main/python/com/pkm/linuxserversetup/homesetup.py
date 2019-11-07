# Pythono3 code to add creature comforts like bash, alias, and vimrc files
  
# importing os module 
import os 
import os.path
from os import path
  
# Function to rename multiple files 
def main(): 
    os.chdir("/home/pmartin") 
    homedirFilesList = ['bashrc.txt', 'alias.txt', 'vimrc.txt']
    for filename in homedirFilesList: 
        if path.exists(filename):
            # Add a leading '.' and remove the .txt from the file
            dst ='.' + filename[:-4]
            print("Renaming '" + filename + "' to '" + dst + "'")
            # Rename the file if it exists
            os.rename(filename, dst) 
        else:
            print ("'" + filename + "' does not exist!")

# Driver Code 
if __name__ == '__main__': 
 
    # Calling main() function 
    main() 
    print("Done!")

