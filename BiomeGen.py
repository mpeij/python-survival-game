import random

newTerrain = True
water = False
TerrainWater = ["creek","river","lake","stream","waterfall"]
TerrainGround = ["grassy","rocky","sandy"]
TerrainAttribute = ["trees","cliffs"]
TerrainLevel = ["mountains","lowlands","highlands"]

if newTerrain == True:
	water = random.choice([True, False])
	TGF = random.choice(TerrainGround)	
	TAF = random.choice(TerrainAttribute)
	TLF = random.choice(TerrainLevel)
	if water == True:
		TWF = random.choice(TerrainWater)
		print ("There are", TGF, TLF, "with", TAF, "and a", TWF)
	else:
		print ("There are", TGF, TLF, "with", TAF)
        data = []
        Biomes = [biome[0], biome[1]]
        biome = [x, y, data]
