this_file=__name__+".py"

file = open(this_file,"r")
data = file.read()
file = open(this_file,"w")
file.write(data+"\n\n#Test Kommentar")
file.close()

#Test Kommentar

#Test Kommentar