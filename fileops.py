from os import getcwd, listdir, path
import json

#==================================================================#
#  Generic Method for prompting for file path
#==================================================================#
def getsavepath(dir, title, types):
    return input("Enter save file path for " + title + ", types: " + str(types) + ": ")

#==================================================================#
#  Generic Method for prompting for file path
#==================================================================#
def getloadpath(dir, title, types):
    return input("Enter load file path for " + title + ", types: " + str(types) + ": ")

#==================================================================#
#  Generic Method for prompting for directory path
#==================================================================#
def getdirpath(dir, title):
    return input("Enter directory path for " + title + ": ")

#==================================================================#
#  Returns an array of dicts containing story files in /stories
#==================================================================#
def getstoryfiles():
    list = []
    for file in listdir(getcwd()+"/stories"):
        if file.endswith(".json"):
            ob = {}
            ob["name"] = file.replace(".json", "")
            f = open(getcwd()+"/stories/"+file, "r")
            js = json.load(f)
            f.close()
            ob["actions"] = len(js["actions"])
            list.append(ob)
    return list

#==================================================================#
#  Returns True if json file exists with requested save name
#==================================================================#
def saveexists(name):
    return path.exists(getcwd()+"/stories/"+name+".json")