import pickle

from choicesFunctions import getOptionOneOrTwo

def saveOrLoad(data):
	option = getOptionOneOrTwo('Save', 'Load')
	if option == 1:
		saveGame(data)
	if option == 2:
		loadGame(data)

def saveGame(data):
	pickle_out = open("saveData.pickle", "wb")
	pickle.dump(data, pickle_out)
	pickle_out.close

def loadGame():
	pickle_in = open("saveData.pickle","rb")
	data = pickle.load(pickle_in)
	return data