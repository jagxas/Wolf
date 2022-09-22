playernames = []
playernumber = 0
playerroles = []
count1 = 1
cyclevar = 0 # player numberi gectiginde yeniden 1 olmalı
allroles = ["werewolf","seer","witch","villager","doctor", "priest","detective","red lady","medium"]
wolfnum = 1

mayor_enabled = True

previous_choice_of_doc = ["","","","","","","","",""]
lady_go = [-1,-1,-1,-1,-1,-1,-1,-1,-1]

anlik = 0
active_rn = len(allroles) - 1

willdie = [0, 0, 0, 0, 0, 0, 0, 0, 0]
willlive = [0, 0, 0, 0, 0, 0, 0, 0, 0]
dead = [0, 0, 0, 0, 0, 0, 0, 0, 0]
votes = [0, 0, 0, 0, 0, 0, 0, 0, 0]

willrevive = [0, 0, 0, 0, 0, 0, 0, 0, 0]
used_medium = [0, 0, 0, 0 , 0, 0, 0 , 0 , 0]
