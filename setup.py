import json
import os
os.mkdir("saves")
with open("saves/saveNames.json", "w+") as file_out:
	json.dump("",file_out)