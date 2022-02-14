from PIL import Image
 
im= Image.new("RGB", (16, 16), "#FFFFFF")
im.paste((0,0,0),(0,0,8,16))

im.save('test4.jpeg')