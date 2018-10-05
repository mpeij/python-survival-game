def SaveBiome(Biome):
    try: 
        Biomefile = open("biomes.txt", "w")
        Biomefile.write(str(Biome))
        Biomefile.close()
    except IOError:
        # Hm, can't write it.
        print("Unable to save biomes.")
