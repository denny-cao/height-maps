import xml.etree.ElementTree as ET


def replace_heightmap(number):
    tree = ET.parse("heightmap0.world")
    root = tree.getroot()

    for uri in root.iter("uri"):
        uri.text =f"file://media/materials/textures/{number}.png"


    tree.write("heightmap0.world")

replace_heightmap(1)
