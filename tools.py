# from health_management import name

def gd():
    import datetime
    return datetime.datetime.now
'''to get date and time'''

def log_food(g,name):
    q=input(f"what did you eat {name}")
    with open(g,"a") as f:
        f.write(f"you ate {q} at {gd()}\n")
        print("logged")
'''to log details of food you ate'''

def log_exercise(h,name):
    w=input(f"what did you exercised {name}")
    with open(h,"a") as l:
        l.write(f"you did {w} at {gd()}\n")
        print("logged")
'''to log details of exercise you did'''

def view_food(g):
    with open(g,"r") as f:
        q=f.read()
        print(q)
'''to view details of food you ate'''

def view_exercise(h):
    with open(h,"r") as l:
        w=l.read()
        print(w)
'''to view details of exercise you did'''
