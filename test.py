start=True
global k
k=0
def go_left(): 
    if self.k!=0:
        self.k-=1
        update()

def go_right():
    if len(self.name_list)-1!=self.k:
        self.k+=1
        update()

def end_select_name():
    kb.unhook_all_hotkeys()
    e.clear_cmd()
    self.run_select_name=False

def update():
    e.clear_cmd()
    text = self.text

    print(text.select_load_name+self.name_list[self.k])
    print()
    if self.k==0:print("--->")
    elif self.k==len(self.name_list)-1:print("<---")
    else:print("<---  --->")

e = extention()

db = database()
# for item in db.get_all():
#     name_list.append(item[0])
self.name_list=["name1", "name2", "name3", "name4"]
self.run_select_name = True
kb.add_hotkey("left", go_left)
kb.add_hotkey("right", go_right)
kb.add_hotkey("space", end_select_name)
if start:
    update()

# while self.run_select_name:
#     time.sleep(0.02)
# return self.name_list[self.k]

