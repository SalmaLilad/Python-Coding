from PIL import Image
sunglasses =  Image.open("sunglasses.png")
sunglasses.size

help(Image.alpha_composite)

def add_images(base_image, new_image, dest = (0,0)):
    # .convert copies the image and translates it into an RGBA colorspace
    # (i.e., RGB + transparency). This is necessary for us to add images
    # with transparency on top of it.
    pasted = base_image.convert("RGBA")
    new = new_image.convert("RGBA")
    
       # The methods that operate in-place (like alpha_composite) don't
    # actually return the image (they return None), so you can't chain
    # them together (like market.copy().convert().alpha_composite()).
    pasted.alpha_composite(new , dest = dest)

    return pasted

gracie = Image.open("gracie.jpg")
gracie_plus_sunglasses = add_images(gracie,sunglasses)
gracie_plus_sunglasses

import ipywidgets

image = gracie 
print("Change the values of x and y from the dropdown menu so sunglasses are centered on Ms. Gracie's face.")
@ipywidgets.interact(
    x = [100, 200, 300, 400, 500, 600, 700],
    y = [150, 250, 350, 400, 550, 650, 700]
)
def _(x, y):
    return add_images(image, sunglasses, dest = (x,y))

x_gracie = 590
y_gracie = 350
add_images(image, sunglasses, dest = (x_gracie,y_gracie))

queen_gracie = Image.open("queen_gracie.jpg")
queen_gracie

import ipywidgets

image = queen_gracie 
@ipywidgets.interact(
    x = [0, 50, 100, 150, 250, 350],
    y = [0, 50, 100, 150, 250, 350],
)
def _(x, y):
    return add_images(image, sunglasses, dest = (x,y))

def base_plus_lens(base, lens, dest=(0, 0), scale=1, angle = 0):
    # .convert copies the image and translates it into an RGBA colorspace
    # (i.e., RGB + transparency). This is necessary for us to add images
    # with transparency on top of it.
    pasted = base.convert("RGBA")
    
    # scale the dimensions, round them to ints, and make sure they're >= 1px
    new_width = round(scale * lens.width)
    new_height = round(scale * lens.height)
    lens = lens.resize((new_width, new_height))
    lens = lens.rotate(angle)

    # The methods that operate in-place (like alpha_composite) don't
    # actually return the image (they return None), so you can't chain
    # them together (like market.copy().convert().alpha_composite()).
    pasted.alpha_composite(lens, dest=dest)

    return pasted

from ipywidgets import interact
print("Use the dropdown menu to pick values for x, y, scale, and angle that are well placed on Ms. Gracie.")
image = queen_gracie
@interact(
    x = [0, 50, 100, 150, 200, 250, 300, 350],
    y = [0, 50, 110, 150, 200, 250, 300, 350],
    scale = [0.1, 0.25, 0.5, 1.0, 1.25],
    angle = [0, 30, 60, -25, -40],
)
def _(x, y, scale, angle): ## using _ allows us to define a function with no name 
    return base_plus_lens(image, sunglasses, dest=(x, y), scale = scale, angle = angle)

x = 200
y = 110
scale = .3
angle = 340 ## can be between -180 and 180
base_plus_lens(image, sunglasses, dest=(x, y), scale = scale, angle = angle)
