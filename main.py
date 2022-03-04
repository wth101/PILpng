# Make pixels grey based on current rgb values
# find average of rgb and set all channels to avg
from PIL import Image
img = Image.open("img.png").convert('RGB')
#data = list(img.getdata())
width, height = img.size
img2 = Image.new(mode="RGB", size=(width,height))
for y in range(height):
	for x in range(width):
		rgb = img.getpixel((x,y))
		avg = int(sum(rgb)/3)
		img2.putpixel((x,y), (avg, avg, avg))
img2.save("img2.png")







	
	



