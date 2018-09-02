
status = -1

def init():
    sm.setSpeakerID(3001007)
    sm.sendNext("I'm sorry, but it's crazy around here. Our commanders, #b#p3001000##k and #b#p3001001##k, are cut off near the front.")

def action(response, answer):
    global status
    status += 1

    if status == 0:
        sm.sendSay("They're both top-quality warriors, but I'm worried about the troops with them. They may not have the fortitude to handle that kind of battle.")

    if status == 1:
        sm.sendSay("I don't really have time to go into further detail, but we need your help on the battlefield. I'll guide you there!")

    if status == 2:
        sm.sendAskYesNo("Please protect as may soldiers as you can! If you succeed, please go to the #b#m401000001##k and speak with both #b#p3001001##k and #b#p3001000##k. I wish you luck, Maple Warrior! \r\n \r\n #b(#ePress Accept to move automatically. You will have to forfeit the quest and restart if you fail.#n)#k")

    if status == 3:
        if response == 1:
            sm.setFlippedPlayerAsSpeaker()
            sm.sendNext("I'm ready to enter the Heliseum Reclamation HQ and hunt down my enemies.")
        elif response == 0:
            #TODO
            sm.dispose()

    if status == 4:
        sm.startQuest(31802)
        sm.warpInstanceIn(401070000)
        sm.dispose()