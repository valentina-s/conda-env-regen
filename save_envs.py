import os
import sys
import subprocess

def main():
    # extract the base anaconda path
    anaconda_path = sys.base_prefix

    # creating the folder where the .yml files will be stored
    environments_path = os.path.join(os.getcwd(),'envs')
    if not os.path.isdir(environments_path):
        os.makedirs(environments_path)

    #TODO
    # 1) add warning that it will overwrite everything in envs
    # 2) allow to specify new location


    # obtaining a list of all environments
    envs = os.listdir(os.path.join(anaconda_path,'envs'))

    for env in envs:
        yml_filename = os.path.join(environments_path,'environment_%s.yml'%env)
        subprocess.Popen('conda env export --name %s > %s'%(env,yml_filename),shell = True)

if __name__ == "__main__":
    import os
    import sys
    import subprocess

    main()
