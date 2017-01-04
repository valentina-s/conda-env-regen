import os
import sys
import glob
import subprocess

def main():
    environments_path = os.path.join(os.getcwd(),'envs')
    # assuming all the files are conda .yml (I could check better)
    env_files = glob.glob(environments_path+'/*')

    for filename in env_files:
        #filename.strip('environment_')
        env_name = os.path.basename(filename)[12:-4]
        env_filename = os.path.basename(filename)[12:]
        subprocess.Popen('conda env create -f %s'%env_filename, shell=True)

if __name__ == "__main__":
    import os
    import sys
    import glob
    import subprocess
    main()
