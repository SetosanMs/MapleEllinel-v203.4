def init():
	warp = True
	fieldID = sm.getFieldID()
	if fieldID == 930100400:
		map = 930100500
		portal = 0

	# Party Quest - Escape
	elif fieldID / 10000 == 92116:
		if fieldID == 921160600:
			warp = False
			if sm.getReactorQuantity() > 1:
				sm.chat("Unlock all the prison doors.")
			else:
				warp = True

		map = fieldID + 100
		portal = 0

	# Monster Park
	elif fieldID / 1000000 == 952 or fieldID / 1000000 == 953 or fieldID / 1000000 == 954:
		map = fieldID + 100
		portal = 0

	# To Crimson Queen
	elif fieldID == 105200300:
		# if sm.mobsPresentInField():
		# 	sm.chat("Eliminate all monster before proceeding.")
		# else:
			map = 105200310
			portal = 0

	# To Pierre
	elif fieldID == 105200200:
		# if sm.mobsPresentInField():
		# 	sm.chat("Eliminate all monster before proceeding.")
		# else:
			map = 105200210
			portal = 0

	# To VonBon
	elif fieldID == 105200100:
		# if sm.mobsPresentInField():
		# 	sm.chat("Eliminate all monster before proceeding.")
		# else:
			map = 105200110
			portal = 0

	# To VonBon
	elif fieldID == 105200400:
		# if sm.mobsPresentInField():
		# 	sm.chat("Eliminate all monster before proceeding.")
		# else:
			map = 105200410
			portal = 0

	else:
		sm.chat("(Portal) This script (next00.py) is not coded for this map. (ID: " + str(fieldID) + ")")
		map = sm.getChr().getField().getReturnMap()
		portal = 0

	if warp:
		sm.warp(map, portal)
		sm.dispose()