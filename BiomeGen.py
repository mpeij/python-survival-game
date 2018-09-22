import random

newTerrain = True
water = False
TerrainWater = ["Creek","River","Lake","Stream","Waterfall"]
TerrainGround = ["Dirt","Grass","Rocks","Podzol"]
TerrainAttribute = ["Trees","Cliffs"]


if newTerrain == True:
	water = random.choice([True, False])
	TGF = random.choice(TerrainGround)	
	TAF = random.choice(TerrainAttribute)
	if water == True:
		TWF = random.choice(TerrainWater)
		print (TGF,TAF,TWF)
	else:
		print (TGF,TAF)
