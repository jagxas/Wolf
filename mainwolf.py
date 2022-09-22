#from kivy.config import Config
#Config.set('graphics', 'width', '375')
#Config.set('graphics', 'height', '667')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.properties import StringProperty, ListProperty, NumericProperty, BooleanProperty
from kivy.metrics import dp,sp
from kivy.properties import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.core.audio import SoundLoader
import constants
import random


class StartingScreen(Screen):

    temp_val = 0
    temp_list  = constants.used_medium.copy()
    rolenum = 0
    def enoughqm(self):
        for a in constants.allroles:
            if a != "werewolf" and a != "mayor":
                self.rolenum += 1

        if self.rolenum < 1:
            self.rolenum = 0
            return False
        else:
            self.rolenum = 0
            return True


    def hmm(self):
        print(constants.playerroles)
        print(constants.playernames)
        print(constants.playernumber)
    def cleansing(self):
        print(constants.allroles)
        constants.willdie = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        constants.willlive = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        constants.dead = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        constants.votes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        constants.playernames = []
        constants.playernumber = 0
        constants.playerroles = []
        constants.count1 = 1
        constants.cyclevar = 0
        constants.previous_choice_of_doc = ["","","","","","","","",""]
        constants.lady_go = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
        constants.anlik = 0
        self.temp_val = constants.anlik
        constants.willrevive = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        constants.used_medium = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.temp_list = constants.used_medium.copy()


class Enable(Screen):

    atleast2 = 0


    def least(self):
        if self.ids.witch.active == True: self.atleast2 += 1
        if self.ids.villager.active == True: self.atleast2 += 1
        if self.ids.seer.active == True: self.atleast2 += 1
        if self.ids.doc.active == True: self.atleast2 += 1
        if self.ids.detective.active == True: self.atleast2 += 1
        if self.ids.priest.active == True: self.atleast2 += 1
        if self.ids.redlady.active == True: self.atleast2 += 1
        if self.ids.medium.active == True: self.atleast2 += 1

        while True:
            if self.atleast2 == 0:
                rn = random.randint(1,8)
                if rn == 1:
                    self.ids.witch.active = True
                    self.atleast2 += 1
                elif rn == 2:
                    self.ids.seer.active = True
                    self.atleast2 += 1
                elif rn == 3:
                    self.ids.villager.active = True
                    self.atleast2 += 1
                elif rn == 4:
                    self.ids.doc.active = True
                    self.atleast2 += 1
                elif rn == 5:
                    self.ids.detective.active = True
                    self.atleast2 += 1
                elif rn == 6:
                    self.ids.priest.active = True
                    self.atleast2 += 1
                elif rn == 7:
                    self.ids.redlady.active = True
                    self.atleast2 += 1
                elif rn == 8:
                    self.ids.medium.active = True
                    self.atleast2 += 1

            else:
                break

        self.atleast2 = 0

    def s_up(self, *args):
        print(args[1])
        self.ids.slab.text = str(args[1])
        constants.wolfnum = args[1]

    def update(self):
        if self.ids.seer.active == True:
            if constants.allroles.__contains__("seer") == False:
                constants.allroles.append("seer")
        else:
            if constants.allroles.__contains__("seer") == True:
                constants.allroles.remove("seer")
        if self.ids.villager.active == True:
            if constants.allroles.__contains__("villager") == False:
                constants.allroles.append("villager")
        else:
            if constants.allroles.__contains__("villager") == True:
                constants.allroles.remove("villager")
        if self.ids.witch.active == True:
            if constants.allroles.__contains__("witch") == False:
                constants.allroles.append("witch")
        else:
            if constants.allroles.__contains__("witch") == True:
                constants.allroles.remove("witch")
        if self.ids.doc.active == True:
            if constants.allroles.__contains__("doctor") == False:
                constants.allroles.append("doctor")
        else:
            if constants.allroles.__contains__("doctor") == True:
                constants.allroles.remove("doctor")
        if self.ids.detective.active == True:
            if constants.allroles.__contains__("detective") == False:
                constants.allroles.append("detective")
        else:
            if constants.allroles.__contains__("detective") == True:
                constants.allroles.remove("detective")
        if self.ids.priest.active == True:
            if constants.allroles.__contains__("priest") == False:
                constants.allroles.append("priest")
        else:
            if constants.allroles.__contains__("priest") == True:
                constants.allroles.remove("priest")
        if self.ids.redlady.active == True:
            if constants.allroles.__contains__("red lady") == False:
                constants.allroles.append("red lady")
        else:
            if constants.allroles.__contains__("red lady") == True:
                constants.allroles.remove("red lady")
        if self.ids.medium.active == True:
            if constants.allroles.__contains__("medium") == False:
                constants.allroles.append("medium")
        else:
            if constants.allroles.__contains__("medium") == True:
                constants.allroles.remove("medium")

        if self.ids.prsdnt.active == True:
            constants.mayor_enabled = True
        else:
            constants.mayor_enabled = False





class PlayerNum(Screen):
    playernum = constants.playernumber
    def doit(self):
        constants.playernumber = self.playernum


class PlayerNames(Screen):
    count = constants.count1
    playernumbera = constants.playernumber
    ses = SoundLoader.load("audiofiles/howl.wav")
    def ekstra(self):
        self.count = 1
        self.ids.input.hint_text = 'Player {}'.format(str(self.count))

    def limit(self):
        if len(self.ids.input.text) > 8:
            print("8den fazla",end=" ")
            mylist = list(self.ids.input.text)
            mylist[8] = ''
            mytxt = ""
            mytxt.join(mylist)
            self.ids.input.text = mytxt

    def takeit(self):
        self.playernumbera = constants.playernumber
        text = self.ids.input.text
        if text == "":
            constants.playernames.append(self.ids.input.hint_text)
        else:
            constants.playernames.append(text)
        self.ids.input.text = ""
        self.ids.input.hint_text = 'Player {}'.format(str(self.count + 1))

    def assignroles(self):
        WN = constants.wolfnum
        for i in range(0, len(constants.playernames)):
            r = random.randint(1,len(constants.allroles)-1)
            constants.playerroles.append(constants.allroles[r])

        #Mayor
        if constants.mayor_enabled == True:
            binary = random.randint(0,1)
            if binary == 1:
                r = random.randint(0,len(constants.playernames)-1)
                constants.playerroles[r] = "mayor"
        #Werewolf

        for j in range(0, WN):
            print("Werewolf Number: ",WN)
            while True:
                r = random.randint(0, len(constants.playerroles) - 1)
                if constants.playerroles[r] != "werewolf":
                    constants.playerroles[r] = "werewolf"
                    break
                else:
                    continue

    def auuu(self):
        self.ses.play()

class End(Screen):
    val = BooleanProperty(False)
    wws = ""
    second = StringProperty("")
    top = StringProperty("")

    def dsply(self):
        for i in range(0, constants.playernumber):
            if constants.playerroles[i] == "werewolf":
                self.wws = self.wws + "\n" +str(constants.playernames[i])

        print(self.wws)
        self.ids.mylabel.text = self.wws
        self.second = "was the werewolf"
        self.ids.mylabel2.text = self.second

    def bton(self):
        self.ids.mylabel.text = "The Game Has Ended"
        self.second = ""
        self.ids.mylabel2.text = self.second

    def who(self):
        for i in range(0,constants.playernumber):
            if constants.dead[i] == 0 and constants.playerroles[i] == "werewolf":
                self.top = "werewolves WON!"
            elif constants.dead[i] == 0 and constants.playerroles[i] != "werewolf":
                self.top = "VILLAGERS WON!"



class GivePhone(Screen):
    ses = SoundLoader.load("audiofiles/rooster.wav")
    btxt = StringProperty("Continue")

    s_or_pass = BooleanProperty(False)
    text = StringProperty("Proceed")
    viptext = StringProperty()
    aktiv = constants.playernumber
    anotherval = BooleanProperty(True)
    label2 = StringProperty("")
    variable = 0


    #on touch kullan bari ne diyim, tıkla ve ekranda yazan kisiye telefonu ver
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.variable = constants.cyclevar
    def auuu(self):
        self.ses.play()

    def testingfunc(self):
        self.variable = 0
        constants.cyclevar = 0
        self.anotherval = True
        self.s_or_pass = False

    def clickedFalse(self):
        constants.i_hate_this_shit = False
        self.i_fucking_hate_this = constants.i_hate_this_shit
        self.variable = constants.cyclevar
        self.dername = constants.playernames.copy()
        self.dierolle = constants.playerroles.copy()
        self.maxval = constants.playernumber
        self.aktiv = constants.playernumber - constants.dead.count(1)

        while True:
            if self.variable >= constants.playernumber:
                print("Variable Value {}".format(self.variable))
                self.text = "Proceed"
                print("Huh?")
                self.s_or_pass = True
                self.variable+=1
                break
            elif constants.dead[self.variable] == 0:
                print("Index: {}".format(self.variable))
                self.text = "{}".format(self.dername[self.variable])
                self.label2 = "Give the device to"
                self.btxt = "Show Role"
                self.s_or_pass = True
                self.variable += 1
                print("Ofya {} {}".format(self.variable, constants.cyclevar))

                constants.anlik = self.variable # Hmmmmmmmmm
                break
            elif constants.dead[self.variable] == 1:
                self.variable += 1
                continue
        #print("Aktif Sayı {}".format(self.aktiv))
        constants.cyclevar = self.variable

    def clickedTrue(self):
        constants.i_hate_this_shit = False
        self.i_fucking_hate_this = constants.i_hate_this_shit
        self.variable = constants.cyclevar
        self.btxt = "Continue";
        self.label2 = ""
        self.maxval = constants.playernumber
        self.dername = constants.playernames.copy()
        self.dierolle = constants.playerroles.copy()
        self.viptext = self.dierolle[self.variable-1]
        if self.variable < self.maxval:
            self.s_or_pass = False
            lgiag = True
            for i in range(self.variable, self.maxval):
                if constants.dead[i] == 0:
                    lgiag = False
            if lgiag:
                self.anotherval = False
                self.variable = self.maxval

        else:
            self.variable+=1
            print("Hiç buraya geldik mi peki")
            self.anotherval = False

        self.text = "Proceed"
        print("Current CYCLEVAR: ",constants.cyclevar)

class Voting(Screen):
    namelist = ListProperty()
    dis = BooleanProperty(False)
    election = constants.votes.copy()
    schondead = constants.dead.copy()
    val = NumericProperty(0)
    txt = StringProperty("Discuss & Vote for someone's")
    txt2 = StringProperty("Execution")
    stop = False
    ses = SoundLoader.load("audiofiles/howl.wav")
    rolelist = ListProperty()

    def got_it(self):
        self.rolelist = constants.playerroles.copy()

        self.namelist = constants.playernames.copy()
        self.election = constants.votes.copy()
        self.schondead = constants.dead.copy()
        self.clear()
        for i in range(0,constants.playernumber):
            constants.votes[i] = 0
        for i in range(0, constants.playernumber):
            if constants.dead[i] == 0:
                self.txt = "Give the Device to"
                self.txt2 = self.namelist[i]
                self.val = i+1
                break

    def clear(self):
        if constants.playernumber>0: self.ids.sifir.text = "{} ({})".format(self.namelist[0], self.election[0]) # ID OF A BUTTON AMINAKOYIM
        if constants.playernumber>1: self.ids.bir.text = "{} ({})".format(self.namelist[1], self.election[1])
        if constants.playernumber>2: self.ids.iki.text = "{} ({})".format(self.namelist[2], self.election[2])
        if constants.playernumber>3: self.ids.uc.text = "{} ({})".format(self.namelist[3], self.election[3])
        if constants.playernumber>4: self.ids.dort.text = "{} ({})".format(self.namelist[4], self.election[4])
        if constants.playernumber>5: self.ids.bes.text = "{} ({})".format(self.namelist[5], self.election[5]) # ID OF A BUTTON AMINAKOYIM
        if constants.playernumber>6: self.ids.alti.text = "{} ({})".format(self.namelist[6], self.election[6])
        if constants.playernumber>7: self.ids.yedi.text = "{} ({})".format(self.namelist[7], self.election[7])
        if constants.playernumber>8: self.ids.sekiz.text = "{} ({})".format(self.namelist[8], self.election[8])
        self.ids.mb.text = "Start"
        #self.ids.mb.disabled = False

    def clean_afterwards(self):
        self.ids.sifir.text = ""
        self.ids.bir.text = ""
        self.ids.iki.text = ""
        self.ids.uc.text = ""
        self.ids.dort.text = ""
        self.ids.bes.text = ""
        self.ids.alti.text = ""
        self.ids.yedi.text = ""
        self.ids.sekiz.text = ""
        self.ids.dv.text = "Discuss & Vote for someone's"
        self.ids.ex.text = "execution"

    def goahead(self):
        self.namelist = constants.playernames.copy()
        while True:
            self.clear()
            if self.val >= constants.playernumber:
                print("Variable Value {}".format(self.val))
                self.txt = "Voting has come to an end"
                self.txt2 = ""
                self.ids.mb.text = "Proceed"
                self.s_or_pass = True
                self.val+=1
                self.stop = True
                self.dis = False
                Clock.schedule_once(self.newfunc, 0.7)
                break
            elif constants.dead[self.val] == 0:
                print("Index: {}".format(self.val))
                self.txt = "Give the Device to"
                self.txt2 = self.namelist[self.val]
                self.s_or_pass = True
                self.val += 1
                break
            elif constants.dead[self.val] == 1:
                self.val += 1
                continue
        print(self.election)

    def newfunc(self, dt):
        high = max(self.election)
        if self.election.count(high) == 1:
            i = self.election.index(high, 0, constants.playernumber)
            self.txt = "The executed player is"
            self.txt2 = self.namelist[i]
            constants.dead[i] = 1
            self.dis = False
        else:
            self.txt = "No one died"
            self.txt2 = ""
            self.dis = False

    def WolfDie(self):
        alive = False
        for i in range(0, constants.playernumber):
            if constants.dead[i] == 0 and constants.playerroles[i] == "werewolf":
                alive = True

        if alive == True:
            return False
        else:
            return True

    def WolfWin(self):
        OnlyWolves = True
        for i in range(0, constants.playernumber):
            if constants.dead[i] == 0 and constants.playerroles[i] != "werewolf":
                OnlyWolves = False


        if OnlyWolves == True:
            return True
        else:
            return False

    def auuu(self):
        self.ses.play()

class Kurt(Screen):
    pass

class Gozcu(Screen):
    pass

class Cadi(Screen):
    pass

class Koylu(Screen):
    pass

class Doctor(Screen):
    def skipped(self):
        constants.previous_choice_of_doc[constants.cyclevar - 1] = ""

class Papaz(Screen):
    pass

class RedLady(Screen):
    pass

class Medium(Screen):
    pass

class Detective(Screen):
    pass

class Prezident(Screen):
    pass

class Sabah(Screen):
    text = StringProperty("IT'S MORNING")
    temp = BooleanProperty(True)
    deathstonight = False
    anothertext = StringProperty("")

    comebackers = False

    stop = False

    def display(self):
        self.text = ""

        if constants.willrevive.__contains__(1): self.comebackers = True

        #Lady process
        for j in range(0,constants.playernumber):
            if constants.playerroles[j] == "red lady":
                pindex = int(constants.lady_go[j])
                if pindex != -1:
                    print("Debuggin reasons")
                    if (constants.willdie[pindex] == 0 or constants.willlive[pindex] == 1) and constants.playerroles[pindex] != "werewolf":
                        constants.willlive[j] = 1
                    elif constants.willdie[pindex] == 1 and constants.willlive[pindex] == 0:
                        constants.willdie[j] = 1
                    elif constants.playerroles[pindex] == "werewolf":
                        constants.willdie[j] = 1


        for i in range(0, constants.playernumber):
            if constants.willdie[i] == 1 and constants.willlive[i] == 0:
                self.text += constants.playernames[i]
                self.text += '\n'
                constants.dead[i] = 1
                self.deathstonight = True


            constants.willdie[i] = 0
            constants.willlive[i] = 0

        self.temp = False

        if self.deathstonight == True:
            self.anothertext = "has/have died tonight"
            self.deathstonight = False
        else:
            self.text = "No one died tonight"

    def any_comeback(self):
        # Dirilt - Medium Process
        self.text = ""
        for k in range(0, constants.playernumber):
            if constants.willrevive[k] == 1:
                constants.dead[k] = 0
                self.text += constants.playernames[k]
                self.text += "\n"

        self.anothertext = ""
        self.anothertext += "has/have been revived!\n (S)he is alive again!"
        self.comebackers = False
        constants.willrevive = [0, 0, 0, 0, 0, 0, 0, 0, 0]



    def WolfDie(self):
        alive = False
        for i in range(0, constants.playernumber):
            if constants.dead[i] == 0 and constants.playerroles[i] == "werewolf":
                alive = True

        if alive == True:
            return False #-> return
            print("4:56pm")
        else:
            return True
            print("4:56pm")

    def WolfWin(self):
        OnlyWolves = True
        for i in range(0, constants.playernumber):
            if constants.dead[i] == 0 and constants.playerroles[i] != "werewolf":
                OnlyWolves = False

        if OnlyWolves == True:
            return True
        else:
            return False


class Kill(Screen):
    namelist = ListProperty()
    dis = BooleanProperty(False)
    dyinglist = constants.willdie.copy()
    schondead = constants.dead.copy()
    dislist = [False, False, False, False, False, False, False, False, False]

    def got_it(self):
        self.namelist = constants.playernames.copy()

        self.dyinglist = constants.willdie.copy()

        self.schondead = constants.dead.copy()
        if constants.anlik == 1: self.dislist[0] = True
        elif constants.anlik == 2: self.dislist[1] = True
        elif constants.anlik == 3: self.dislist[2] = True
        elif constants.anlik == 4: self.dislist[3] = True
        elif constants.anlik == 5: self.dislist[4] = True
        elif constants.anlik == 6: self.dislist[5] = True
        elif constants.anlik == 7: self.dislist[6] = True
        elif constants.anlik == 8: self.dislist[7] = True
        elif constants.anlik == 9: self.dislist[8] = True

    def clean_afterwards(self):

        self.ids.sifir.text = ""
        self.ids.bir.text = ""
        self.ids.iki.text = ""
        self.ids.uc.text = ""
        self.ids.dort.text = ""
        self.ids.bes.text = ""
        self.ids.alti.text = ""
        self.ids.yedi.text = ""
        self.ids.sekiz.text = ""

    def fill_before(self):
        # votingdeki clear gibi hepsini buyuk kucuk olma durumuna gore geri doldur
        #bu fonksiyonu got_it ten cagir
        #olursa spy ve heal ekranlarına da uygula Fingers Crossed
        if constants.playernumber>0: self.ids.sifir.text = "{}".format(self.namelist[0]) # ID OF A BUTTON AMINAKOYIM
        if constants.playernumber>1: self.ids.bir.text = "{}".format(self.namelist[1])
        if constants.playernumber>2: self.ids.iki.text = "{}".format(self.namelist[2])
        if constants.playernumber>3: self.ids.uc.text = "{}".format(self.namelist[3])
        if constants.playernumber>4: self.ids.dort.text = "{}".format(self.namelist[4])
        if constants.playernumber>5: self.ids.bes.text = "{}".format(self.namelist[5]) # ID OF A BUTTON AMINAKOYIM
        if constants.playernumber>6: self.ids.alti.text = "{}".format(self.namelist[6])
        if constants.playernumber>7: self.ids.yedi.text = "{}".format(self.namelist[7])
        if constants.playernumber>8: self.ids.sekiz.text = "{}".format(self.namelist[8])


    def goahead(self):
        print("İçerdeyiz knk bunda sorun yok")
        constants.willdie = self.dyinglist.copy()
        constants.dead = self.schondead.copy()
        self.clean_afterwards()
        self.dis = False
        self.dislist = [False, False, False, False, False, False, False, False, False]
        print(constants.anlik)

class HolyWater(Screen):
    namelist = ListProperty()
    dis = BooleanProperty(False)
    dyinglist = constants.willdie.copy()
    schondead = constants.dead.copy()
    dislist = [False, False, False, False, False, False, False, False, False]

    def got_it(self):
        self.namelist = constants.playernames.copy()

        self.dyinglist = constants.willdie.copy()

        self.schondead = constants.dead.copy()
        if constants.anlik == 1: self.dislist[0] = True
        elif constants.anlik == 2: self.dislist[1] = True
        elif constants.anlik == 3: self.dislist[2] = True
        elif constants.anlik == 4: self.dislist[3] = True
        elif constants.anlik == 5: self.dislist[4] = True
        elif constants.anlik == 6: self.dislist[5] = True
        elif constants.anlik == 7: self.dislist[6] = True
        elif constants.anlik == 8: self.dislist[7] = True
        elif constants.anlik == 9: self.dislist[8] = True

    def clean_afterwards(self):

        self.dis = False
        self.dislist = [False, False, False, False, False, False, False, False, False]

        self.ids.sifir.text = ""
        self.ids.bir.text = ""
        self.ids.iki.text = ""
        self.ids.uc.text = ""
        self.ids.dort.text = ""
        self.ids.bes.text = ""
        self.ids.alti.text = ""
        self.ids.yedi.text = ""
        self.ids.sekiz.text = ""

    def fill_before(self):
        # votingdeki clear gibi hepsini buyuk kucuk olma durumuna gore geri doldur
        #bu fonksiyonu got_it ten cagir
        #olursa spy ve heal ekranlarına da uygula Fingers Crossed
        if constants.playernumber>0: self.ids.sifir.text = "{}".format(self.namelist[0]) # ID OF A BUTTON AMINAKOYIM
        if constants.playernumber>1: self.ids.bir.text = "{}".format(self.namelist[1])
        if constants.playernumber>2: self.ids.iki.text = "{}".format(self.namelist[2])
        if constants.playernumber>3: self.ids.uc.text = "{}".format(self.namelist[3])
        if constants.playernumber>4: self.ids.dort.text = "{}".format(self.namelist[4])
        if constants.playernumber>5: self.ids.bes.text = "{}".format(self.namelist[5]) # ID OF A BUTTON AMINAKOYIM
        if constants.playernumber>6: self.ids.alti.text = "{}".format(self.namelist[6])
        if constants.playernumber>7: self.ids.yedi.text = "{}".format(self.namelist[7])
        if constants.playernumber>8: self.ids.sekiz.text = "{}".format(self.namelist[8])


    def goahead(self, indis):
        if constants.playerroles[indis] == "werewolf":
            self.dyinglist[indis] = 1
        else:
            self.dyinglist[constants.cyclevar - 1] = 1

        constants.willdie = self.dyinglist.copy()
        constants.dead = self.schondead.copy()
        self.clean_afterwards()
        self.dis = False
        self.dislist = [False, False, False, False, False, False, False, False, False]
        print(constants.anlik)

class Revive(Screen):
    namelist = ListProperty()
    dis = BooleanProperty(False)
    dislist = [False, False, False, False, False, False, False, False, False]
    schondead = constants.dead.copy()
    med_using_list = constants.used_medium.copy()

    def got_it(self):
        self.schondead = constants.dead.copy()
        self.namelist = constants.playernames.copy()
        self.schondead = constants.dead.copy()
        if constants.anlik == 1:
            self.dislist[0] = True
        elif constants.anlik == 2:
            self.dislist[1] = True
        elif constants.anlik == 3:
            self.dislist[2] = True
        elif constants.anlik == 4:
            self.dislist[3] = True
        elif constants.anlik == 5:
            self.dislist[4] = True
        elif constants.anlik == 6:
            self.dislist[5] = True
        elif constants.anlik == 7:
            self.dislist[6] = True
        elif constants.anlik == 8:
            self.dislist[7] = True
        elif constants.anlik == 9:
            self.dislist[8] = True

    def clean_afterwards(self):
        self.ids.sifir.text = ""
        self.ids.bir.text = ""
        self.ids.iki.text = ""
        self.ids.uc.text = ""
        self.ids.dort.text = ""
        self.ids.bes.text = ""
        self.ids.alti.text = ""
        self.ids.yedi.text = ""
        self.ids.sekiz.text = ""
        self.dis = False


    def fill_before(self):
        if constants.playernumber > 0: self.ids.sifir.text = "{}".format(self.namelist[0])  # ID OF A BUTTON AMINAKOYIM
        if constants.playernumber > 1: self.ids.bir.text = "{}".format(self.namelist[1])
        if constants.playernumber > 2: self.ids.iki.text = "{}".format(self.namelist[2])
        if constants.playernumber > 3: self.ids.uc.text = "{}".format(self.namelist[3])
        if constants.playernumber > 4: self.ids.dort.text = "{}".format(self.namelist[4])
        if constants.playernumber > 5: self.ids.bes.text = "{}".format(self.namelist[5])  # ID OF A BUTTON AMINAKOYIM
        if constants.playernumber > 6: self.ids.alti.text = "{}".format(self.namelist[6])
        if constants.playernumber > 7: self.ids.yedi.text = "{}".format(self.namelist[7])
        if constants.playernumber > 8: self.ids.sekiz.text = "{}".format(self.namelist[8])

    def goahead(self, i):
        constants.willrevive[i] = 1
        constants.used_medium[constants.anlik - 1] = 1
        #Listeyi kopyala
        self.med_using_list = constants.used_medium.copy()
        self.clean_afterwards()
        constants.dead = self.schondead.copy()
        print("Anlık revive: ",constants.anlik)

class Heal(Screen):
    namelist = ListProperty()
    dis = BooleanProperty(False)
    healinglist = constants.willlive.copy()
    dislist = [False, False, False, False, False, False, False, False, False]
    schondead = constants.dead.copy()

    def got_it(self):
        self.namelist = constants.playernames.copy()

        self.healinglist = constants.willlive.copy()

        self.schondead = constants.dead.copy()
        if constants.anlik == 1:
            self.dislist[0] = True
        elif constants.anlik == 2:
            self.dislist[1] = True
        elif constants.anlik == 3:
            self.dislist[2] = True
        elif constants.anlik == 4:
            self.dislist[3] = True
        elif constants.anlik == 5:
            self.dislist[4] = True
        elif constants.anlik == 6:
            self.dislist[5] = True
        elif constants.anlik == 7:
            self.dislist[6] = True
        elif constants.anlik == 8:
            self.dislist[7] = True
        elif constants.anlik == 9:
            self.dislist[8] = True

    def clean_afterwards(self):
        self.ids.sifir.text = ""
        self.ids.bir.text = ""
        self.ids.iki.text = ""
        self.ids.uc.text = ""
        self.ids.dort.text = ""
        self.ids.bes.text = ""
        self.ids.alti.text = ""
        self.ids.yedi.text = ""
        self.ids.sekiz.text = ""

    def fill_before(self):
        # votingdeki clear gibi hepsini buyuk kucuk olma durumuna gore geri doldur
        #bu fonksiyonu got_it ten cagir
        #olursa spy ve heal ekranlarına da uygula Fingers Crossed
        if constants.playernumber>0: self.ids.sifir.text = "{}".format(self.namelist[0]) # ID OF A BUTTON AMINAKOYIM
        if constants.playernumber>1: self.ids.bir.text = "{}".format(self.namelist[1])
        if constants.playernumber>2: self.ids.iki.text = "{}".format(self.namelist[2])
        if constants.playernumber>3: self.ids.uc.text = "{}".format(self.namelist[3])
        if constants.playernumber>4: self.ids.dort.text = "{}".format(self.namelist[4])
        if constants.playernumber>5: self.ids.bes.text = "{}".format(self.namelist[5]) # ID OF A BUTTON AMINAKOYIM
        if constants.playernumber>6: self.ids.alti.text = "{}".format(self.namelist[6])
        if constants.playernumber>7: self.ids.yedi.text = "{}".format(self.namelist[7])
        if constants.playernumber>8: self.ids.sekiz.text = "{}".format(self.namelist[8])

    def goahead(self):
        print(constants.anlik)
        constants.willlive = self.healinglist.copy()
        constants.dead = self.schondead.copy()
        self.clean_afterwards()
        self.dis = False
        self.dislist = [False, False, False, False, False, False, False, False, False]

class LadyChose(Screen): #redlady
    namelist = ListProperty()
    dis = BooleanProperty(False)
    dislist = [False, False, False, False, False, False, False, False, False]
    schondead = constants.dead.copy()

    def got_it(self):
        self.namelist = constants.playernames.copy()
        self.schondead = constants.dead.copy()
        if constants.anlik == 1:
            self.dislist[0] = True
        elif constants.anlik == 2:
            self.dislist[1] = True
        elif constants.anlik == 3:
            self.dislist[2] = True
        elif constants.anlik == 4:
            self.dislist[3] = True
        elif constants.anlik == 5:
            self.dislist[4] = True
        elif constants.anlik == 6:
            self.dislist[5] = True
        elif constants.anlik == 7:
            self.dislist[6] = True
        elif constants.anlik == 8:
            self.dislist[7] = True
        elif constants.anlik == 9:
            self.dislist[8] = True

    def clean_afterwards(self):
        self.ids.sifir.text = ""
        self.ids.bir.text = ""
        self.ids.iki.text = ""
        self.ids.uc.text = ""
        self.ids.dort.text = ""
        self.ids.bes.text = ""
        self.ids.alti.text = ""
        self.ids.yedi.text = ""
        self.ids.sekiz.text = ""

    def fill_before(self):
        # votingdeki clear gibi hepsini buyuk kucuk olma durumuna gore geri doldur
        #bu fonksiyonu got_it ten cagir
        #olursa spy ve heal ekranlarına da uygula Fingers Crossed
        if constants.playernumber>0: self.ids.sifir.text = "{}".format(self.namelist[0]) # ID OF A BUTTON AMINAKOYIM
        if constants.playernumber>1: self.ids.bir.text = "{}".format(self.namelist[1])
        if constants.playernumber>2: self.ids.iki.text = "{}".format(self.namelist[2])
        if constants.playernumber>3: self.ids.uc.text = "{}".format(self.namelist[3])
        if constants.playernumber>4: self.ids.dort.text = "{}".format(self.namelist[4])
        if constants.playernumber>5: self.ids.bes.text = "{}".format(self.namelist[5]) # ID OF A BUTTON AMINAKOYIM
        if constants.playernumber>6: self.ids.alti.text = "{}".format(self.namelist[6])
        if constants.playernumber>7: self.ids.yedi.text = "{}".format(self.namelist[7])
        if constants.playernumber>8: self.ids.sekiz.text = "{}".format(self.namelist[8])

    def goahead(self, i):
        constants.lady_go[constants.anlik - 1] = i
        constants.dead = self.schondead.copy()
        self.clean_afterwards()
        self.dis = False
        self.dislist = [False, False, False, False, False, False, False, False, False]
        print(constants.lady_go)

class Gozle(Screen):
    namelist = ListProperty()
    dis = BooleanProperty(False)
    Rollen = constants.playerroles.copy()
    schondead = constants.dead.copy()
    anotherlove = BooleanProperty(False)
    dislist = [False, False, False, False, False, False, False, False, False]
    def got_it(self):
        self.namelist = constants.playernames.copy()
        self.Rollen = constants.playerroles.copy()
        self.schondead = constants.dead.copy()
        #for i in range(0,constants.playernumber):
        if constants.anlik == 1:
            self.dislist[0] = True
        elif constants.anlik == 2:
            self.dislist[1] = True
        elif constants.anlik == 3:
            self.dislist[2] = True
        elif constants.anlik == 4:
            self.dislist[3] = True
        elif constants.anlik == 5:
            self.dislist[4] = True
        elif constants.anlik == 6:
            self.dislist[5] = True
        elif constants.anlik == 7:
            self.dislist[6] = True
        elif constants.anlik == 8:
            self.dislist[7] = True
        elif constants.anlik == 9:
            self.dislist[8] = True


    def clear(self):
        if constants.playernumber>0: self.ids.sifir.text = constants.playernames[0] # ID OF A BUTTON AMINAKOYIM
        if constants.playernumber>1: self.ids.bir.text = constants.playernames[1]
        if constants.playernumber>2: self.ids.iki.text = constants.playernames[2]
        if constants.playernumber>3: self.ids.uc.text = constants.playernames[3]
        if constants.playernumber>4: self.ids.dort.text = constants.playernames[4]
        if constants.playernumber>5: self.ids.bes.text = constants.playernames[5]  # ID OF A BUTTON AMINAKOYIM
        if constants.playernumber>6: self.ids.alti.text = constants.playernames[6]
        if constants.playernumber>7: self.ids.yedi.text = constants.playernames[7]
        if constants.playernumber>8: self.ids.sekiz.text = constants.playernames[8]
    def clean_afterwards(self):
        self.ids.sifir.text = ""
        self.ids.bir.text = ""
        self.ids.iki.text = ""
        self.ids.uc.text = ""
        self.ids.dort.text = ""
        self.ids.bes.text = ""
        self.ids.alti.text = ""
        self.ids.yedi.text = ""
        self.ids.sekiz.text = ""
        self.dislist = [False, False, False, False, False, False, False, False, False]

    def fill_before(self):
        # votingdeki clear gibi hepsini buyuk kucuk olma durumuna gore geri doldur
        #bu fonksiyonu got_it ten cagir
        #olursa spy ve heal ekranlarına da uygula Fingers Crossed
        if constants.playernumber>0: self.ids.sifir.text = "{}".format(self.namelist[0]) # ID OF A BUTTON AMINAKOYIM
        if constants.playernumber>1: self.ids.bir.text = "{}".format(self.namelist[1])
        if constants.playernumber>2: self.ids.iki.text = "{}".format(self.namelist[2])
        if constants.playernumber>3: self.ids.uc.text = "{}".format(self.namelist[3])
        if constants.playernumber>4: self.ids.dort.text = "{}".format(self.namelist[4])
        if constants.playernumber>5: self.ids.bes.text = "{}".format(self.namelist[5]) # ID OF A BUTTON AMINAKOYIM
        if constants.playernumber>6: self.ids.alti.text = "{}".format(self.namelist[6])
        if constants.playernumber>7: self.ids.yedi.text = "{}".format(self.namelist[7])
        if constants.playernumber>8: self.ids.sekiz.text = "{}".format(self.namelist[8])

    def goahead(self):
        print(constants.anlik)
        self.dis = False
        constants.dead = self.schondead.copy()
        self.anotherlove = True

    def off(self, index):
        self.ids.lemmetry.text = "{} is a {}".format(self.namelist[index], self.Rollen[index])

    def shit(self):
        self.ids.lemmetry.text = "Choose two players "

class Dedektif(Screen):
    namelist = ListProperty()
    dis = BooleanProperty(False)
    Rollen = constants.playerroles.copy()
    schondead = constants.dead.copy()
    anotherlove = BooleanProperty(False)
    dislist = [False, False, False, False, False, False, False, False, False]
    def got_it(self):
        self.namelist = constants.playernames.copy()
        self.Rollen = constants.playerroles.copy()
        self.schondead = constants.dead.copy()
        #for i in range(0,constants.playernumber):
        if constants.anlik == 1:
            self.dislist[0] = True
        elif constants.anlik == 2:
            self.dislist[1] = True
        elif constants.anlik == 3:
            self.dislist[2] = True
        elif constants.anlik == 4:
            self.dislist[3] = True
        elif constants.anlik == 5:
            self.dislist[4] = True
        elif constants.anlik == 6:
            self.dislist[5] = True
        elif constants.anlik == 7:
            self.dislist[6] = True
        elif constants.anlik == 8:
            self.dislist[7] = True
        elif constants.anlik == 9:
            self.dislist[8] = True

        self.temp_list = ["", ""]
        self.i_list = ["", ""]
        self.firstnsecond = 0
        self.ids.above.text = "Choose two players and see,"
        self.ids.below.text = "if they belong the same team"


    def clear(self):
        if constants.playernumber>0: self.ids.sifir.text = constants.playernames[0] # ID OF A BUTTON AMINAKOYIM
        if constants.playernumber>1: self.ids.bir.text = constants.playernames[1]
        if constants.playernumber>2: self.ids.iki.text = constants.playernames[2]
        if constants.playernumber>3: self.ids.uc.text = constants.playernames[3]
        if constants.playernumber>4: self.ids.dort.text = constants.playernames[4]
        if constants.playernumber>5: self.ids.bes.text = constants.playernames[5]  # ID OF A BUTTON AMINAKOYIM
        if constants.playernumber>6: self.ids.alti.text = constants.playernames[6]
        if constants.playernumber>7: self.ids.yedi.text = constants.playernames[7]
        if constants.playernumber>8: self.ids.sekiz.text = constants.playernames[8]
    def clean_afterwards(self):
        self.ids.sifir.text = ""
        self.ids.bir.text = ""
        self.ids.iki.text = ""
        self.ids.uc.text = ""
        self.ids.dort.text = ""
        self.ids.bes.text = ""
        self.ids.alti.text = ""
        self.ids.yedi.text = ""
        self.ids.sekiz.text = ""
        self.dislist = [False, False, False, False, False, False, False, False, False]
        self.ids.above.text = "Choose two players and see,"
        self.ids.below.text = "if they belong the same team"
        #yazilari sifirla

    def fill_before(self):
        # votingdeki clear gibi hepsini buyuk kucuk olma durumuna gore geri doldur
        #bu fonksiyonu got_it ten cagir
        #olursa spy ve heal ekranlarına da uygula Fingers Crossed
        if constants.playernumber>0: self.ids.sifir.text = "{}".format(self.namelist[0]) # ID OF A BUTTON AMINAKOYIM
        if constants.playernumber>1: self.ids.bir.text = "{}".format(self.namelist[1])
        if constants.playernumber>2: self.ids.iki.text = "{}".format(self.namelist[2])
        if constants.playernumber>3: self.ids.uc.text = "{}".format(self.namelist[3])
        if constants.playernumber>4: self.ids.dort.text = "{}".format(self.namelist[4])
        if constants.playernumber>5: self.ids.bes.text = "{}".format(self.namelist[5]) # ID OF A BUTTON AMINAKOYIM
        if constants.playernumber>6: self.ids.alti.text = "{}".format(self.namelist[6])
        if constants.playernumber>7: self.ids.yedi.text = "{}".format(self.namelist[7])
        if constants.playernumber>8: self.ids.sekiz.text = "{}".format(self.namelist[8])

    def goahead(self):
        print(constants.anlik)
        constants.dead = self.schondead.copy()

    temp_list = ListProperty(["",""])
    i_list = ListProperty(["",""])
    def detective_func(self, dt):
        self.dis = False
        if (self.temp_list[0] == "werewolf" and self.temp_list[1] != "werewolf") or (self.temp_list[0] != "werewolf" and self.temp_list[1] == "werewolf"):
            self.ids.above.text = "{} and {} are".format(self.i_list[0], self.i_list[1])
            self.ids.below.text = "NOT from the same team [NO]"

        else:
            self.ids.above.text = "{} and {} are".format(self.i_list[0], self.i_list[1])
            self.ids.below.text = "from the same team [YES]"

        self.anotherlove = True

    firstnsecond = NumericProperty(0)
    def off(self, index):


        if self.firstnsecond == 0:
            self.ids.above.text = "{} and".format(self.namelist[index])
            self.ids.below.text = ""
            self.temp_list[0] = self.Rollen[index]
            self.i_list[0] = self.namelist[index]
            self.firstnsecond += 1
        elif self.firstnsecond == 1:
            self.ids.below.text = "{}".format(self.namelist[index])
            self.temp_list[1] = self.Rollen[index]
            self.i_list[1] = self.namelist[index]
            #0.7 sn bekle ve yazilari degistirecek bi fonksiyon cagir
            Clock.schedule_once(self.detective_func, .5)


    #def shit(self):
    #    self.ids.lemmetry.text = "See the role of one player "

class HealDoc(Screen):

    indeks = constants.cyclevar
    namelist = ListProperty()
    dis = BooleanProperty(False)
    healinglist = constants.willlive.copy()
    dislist = [False, False, False, False, False, False, False, False, False]
    schondead = constants.dead.copy()

    def got_it(self):
        self.namelist = constants.playernames.copy()
        self.healinglist = constants.willlive.copy()
        self.schondead = constants.dead.copy()
        self.indeks = constants.cyclevar
        print(constants.previous_choice_of_doc)
        for j in range(0,len(self.namelist)):
            if str(constants.previous_choice_of_doc[self.indeks - 1]) == str(self.namelist[j]):
                self.dislist[j] = True
                print("Ayni olduğunu görüyor")

        print(constants.previous_choice_of_doc[self.indeks - 1])
        print(self.dislist)

    def clean_afterwards(self):
        self.ids.sifir.text = ""
        self.ids.bir.text = ""
        self.ids.iki.text = ""
        self.ids.uc.text = ""
        self.ids.dort.text = ""
        self.ids.bes.text = ""
        self.ids.alti.text = ""
        self.ids.yedi.text = ""
        self.ids.sekiz.text = ""

    def fill_before(self):

        if constants.playernumber > 0: self.ids.sifir.text = "{}".format(self.namelist[0])  # ID OF A BUTTON AMINAKOYIM
        if constants.playernumber > 1: self.ids.bir.text = "{}".format(self.namelist[1])
        if constants.playernumber > 2: self.ids.iki.text = "{}".format(self.namelist[2])
        if constants.playernumber > 3: self.ids.uc.text = "{}".format(self.namelist[3])
        if constants.playernumber > 4: self.ids.dort.text = "{}".format(self.namelist[4])
        if constants.playernumber > 5: self.ids.bes.text = "{}".format(self.namelist[5])  # ID OF A BUTTON AMINAKOYIM
        if constants.playernumber > 6: self.ids.alti.text = "{}".format(self.namelist[6])
        if constants.playernumber > 7: self.ids.yedi.text = "{}".format(self.namelist[7])
        if constants.playernumber > 8: self.ids.sekiz.text = "{}".format(self.namelist[8])

    def goahead(self, i):
        print(constants.anlik)
        constants.willlive = self.healinglist.copy()
        constants.dead = self.schondead.copy()

        constants.previous_choice_of_doc[self.indeks - 1] = self.namelist[i] #hmm
        print(constants.previous_choice_of_doc)
        print("Liste üstümde")

        self.clean_afterwards()
        self.dis = False
        self.dislist = [False, False, False, False, False, False, False, False, False]


class Manager(ScreenManager):
    TF_Val = BooleanProperty(False)
    SchonUsed = constants.used_medium.copy()
    Indicator = constants.anlik - 1


kv = Builder.load_file("wolffile.kv")

class WolfApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    WolfApp().run()

#9lu ekran font kucult

#rol yazılarını düzerlt, sonra aktivite basliklarini

#RUN THIS COMMAND: python wolf/mainwolf.py -m screen:phone_oneplus_6t,portrait,scale=.5