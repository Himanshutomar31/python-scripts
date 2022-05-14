from PIL import Image, ImageFilter

img = Image.open("./pokedex/pikachu.jpg")
filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.convert('L') convert the image into grey colored image
filtered_img.save("blur.png", "png")
#resize = filtered_img.resize((300,300))
# better  to use thumnail func , it keeps the aspect ratio intact
print(img)
