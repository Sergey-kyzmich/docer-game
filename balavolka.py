data["assessed_sum"]=random.randint(int(data["real_sum"]-min(data["real_sum"]*(1-level/100), data["real_sum"]*0.8)), int(data["real_sum"]+data["real_sum"]*(3-2*(level/100))))
    