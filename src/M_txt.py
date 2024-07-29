import os

folder = "./ArmFolder"
archieve = folder+"/ArmFile"

def Ex_td():
    if os.path.exists(folder):
        r = "pasta identificada, "
    else:
        os.mkdir(folder)
        r = "pasta criada com sucesso"

    
    if os.path.isfile(archieve):
        r = r + "arquivo identificado."
    else:
        with open(archieve, "w") as file:
            r = r + "arquivo criado com sucesso" 

def read():
    with open(archieve, "r") as file:
        line = str(file.readlines())
        if line[2:-2] == "":
            line = str(['0'])
        return line

def redef(Nv):
    with open(archieve, "w") as a:
        a.write(str(Nv))

def add(Nv):
    r = float(read()[2:-2])
    Vt = Nv+r
    with open(archieve, "w") as a:
        a.write(str(Vt))
    return Vt

def gast(Nv):
    r = float(read()[2:-2])
    Vt = r-Nv
    if Vt < 0:
        Vt = 0
    with open(archieve, "w") as a:
        a.write(str(Vt))
    return Vt