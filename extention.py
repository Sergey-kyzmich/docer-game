import os
import sys
import keyboard as kb
from database import database
from text import text as class_text

class extention:
    def __init__(self):
        self.kb = kb
        self.text=class_text()

    def clear_cmd(self):
        a = lambda:os.system("cls")
        a()
    
    def show_control():
        print("show_control")

    def select_name(self, k):
        r=""
        e = extention()

        db = database()
        name_list=[]
        # for item in db.get_all():
        #     name_list.append(item[0])
        name_list=["name1", "name2", "name3", "name4"]
        start=True
        while True:
            print(123)
            if r=='' or start==True:
                start=False
                print("go")
                e.clear_cmd()
                r=''
                text = self.text
                if k==-1:
                    k=len(name_list)-1

                print(text.select_load_name+name_list[k])
                print()
                if k==0:print("--->")
                elif k==len(name_list)-1:print("<---")
                else:print("<---  --->")
            else:
                if r == "left":
                    if k!=0:
                        k-=1
                elif r == "right":
                    if k!=len(name_list)-1:
                        k+=1
                elif r=="space":
                    return name_list[k]
        
            # r = kb.read_key()