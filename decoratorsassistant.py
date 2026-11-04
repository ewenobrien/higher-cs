length = int(input("What is the length?"))
breadth = int(input("What is the breadth"))
height = int(input("What is the height?"))

floorArea = length*breadth
wallArea = 2*height*length+2*height*breadth
ceilingArea = floorArea

carpetTileSize = int(input("What is the area of ONE carpet tile"))
wallpaperRollSize = int(input("What is the area of ONE wallpaper roll for walls"))

numberOfLitres = ceilingArea
numberOfCarpetTiles = floorArea/carpetTileSize
numberOfWallpaperRolls = wallArea/wallpaperRollSize

print("You need", ceilingArea, "litres of paint for the celiling assuming 1 litre of paint per square metre")
print("You need", numberOfCarpetTiles, "carpet tiles for the floor")
print("You need", numberOfWallpaperRolls, "wallpaper rolls for the walls")


