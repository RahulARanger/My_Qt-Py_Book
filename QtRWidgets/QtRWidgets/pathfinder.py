
# ! NOT  A RIP OFF of the APEX LEGEND's agent pathfinder
import platform,os

def pathfinder(path:str)->str:
    store=platform.system()
    if store=='Windows':return path
    elif store=='Linux':return os.path.join('',*path.strip().split('\\'))
    else:raise OSError("Sorry, pathfinder() can't convert path: {} suitable for your os (comptable are : Linux and Windows). Please Raise an issue in the repo for adding your os. ".format(path))
if __name__=='__main__':print(pathfinder('QtRWidgets\\.vscode\\settings.json'))