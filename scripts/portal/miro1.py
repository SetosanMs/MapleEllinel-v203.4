# Used in Party Quest - Escape
def init():
    if sm.mobsPresentInField():
        sm.warp(921160400, 0) # A secret Door to the Aerial Prison
    else:
        sm.chat("Please eliminate all mobs.")
    sm.dispose()