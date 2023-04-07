from PIL import Image

image_path = "player_up_l.png"

data = []
datayellow = []
with Image.open(image_path) as im:
    for x in range(0, im.width):
        for y in range(0, im.height):
            px = im.getpixel((x,y))
            if px[3] == 0:
                continue #transparent px
            r, g, b = hex(px[0]), hex(px[1]), hex(px[2])
            val = "0x"
            for col in (r,g,b):
                if len(str(col)[2:]) == 1:
                    val += "0" + str(col)[2:]
                else:
                    val +=str(col)[2:]
            data.extend([str(x), str(y), val])
            datayellow.extend([str(x), str(y), "0xfff7a1"])
res = ', '.join(data)
with open("out.txt", "w") as f:
    f.write(res)
with open("outyellow.txt", "w") as f:
    f.write(', '.join(datayellow))
print(len(data))