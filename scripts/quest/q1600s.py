# [Silent Crusade] A Cry for Help

JAKE = 1052006
SUBWAY_TRANSTICKET = 2030028

sm.setSpeakerID(JAKE)
response = sm.sendAskYesNo("Somebody! Anybody! Help!")

if response == 1:
    sm.sendNext("A lady followed a bunch of creeps into the Subway. They looked really dangerous. "
                "Can you head into the #bSubway Construction Site#k and make sure she's okay?")

    sm.sendNext("Hurry to the Subway Ticket Booth!")

    if not sm.canHold(SUBWAY_TRANSTICKET):
        sm.sendSayOkay("Please make some room in your 'use' inventory.")
        sm.dispose()

    sm.giveItem(SUBWAY_TRANSTICKET)
    sm.startQuest(parentID)
    sm.showFieldEffect("Map/Effect.img/crossHunter/chapter/start1")

else:
    sm.sendSayOkay("Really Nigga?")