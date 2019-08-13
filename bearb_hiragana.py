from PIL import Image, ImageFilter

img = Image.open("sasagami-hiragana-chart.jpg")

beg_x=124
beg_y=123

size_x=154
size_y=206


nx = 10
ny = 5


for ix in range(nx):
	for iy in range(ny):
		img.crop((beg_x+size_x*ix,beg_y+size_y*iy,beg_x+size_x*(ix+1),beg_y+size_y*(iy+1),)).save("bearb/test"+str(ix)+"_"+str(iy)+".jpg")