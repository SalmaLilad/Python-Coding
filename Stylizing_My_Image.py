from stylingutils  import * ## this library contains functions that let  us  style an image and display it 
from codexutils import * # this contains the load_and_resize function to load and resize image if it is too big
from ipywidgets import interact
# replace question marks below with  the name of the file you uploaded  - leave quotes as is
image_file = ''    # be sure to include the .png/.jpg file extension e.g. queen_gracie.jpg

# These models are pre-loaded into the kernel workspace as onnx files
style_models = ["candy", "mosaic", "pointilism", "rain-princess", "udnie"]
@interact(model = style_models)
def stylize(model):
    model_file = "data/onnx_files/" + model + "-9.onnx"
    image = load_and_resize_image(image_file)
    result = style_transfer(model_file, image_file)
    display_images(image,result)

import io

from PIL import Image
import ipydraw
print("You can change the color by clicking on the color palette next to the Clear button")
print("Click the clear button to start over. You'll have to reselect the color after every clear.")
canvas = ipydraw.Canvas(
    # optional arguments
    size=(400, 200),
    color=True,
#     line_width=5,
)
canvas

# This function is defined in codexutils.py since it is not
# necessary to understand it for this lesson.
from codexutils import get_image_from_canvas
my_lens = get_image_from_canvas(canvas)
my_lens.save("my_lens.png", format = "png") ## this is how you save an image

queen_gracie = Image.open("queen_gracie.jpg")
queen_gracie

from ipywidgets import interact
import ipywidgets
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

image = queen_gracie
@interact(
    x = ipywidgets.IntSlider(default = 0, min= 0, max = image.width, continuous_update=False),
    y = ipywidgets.IntSlider(default = 0, min = 0, max = image.height, continuous_update=False),
    scale = ipywidgets.FloatSlider(1, min = 0.2, max = 1.5, continuous_update = False),
    angle = ipywidgets.FloatSlider(min = -180, max = 180, continuous_update = False),
)
def _(x, y, scale, angle):
    return base_plus_lens(image, my_lens, dest=(x, y), scale = scale, angle = angle)

queen_gracie_lensified = base_plus_lens(queen_gracie, my_lens, dest = (132, 71), scale = 0.7, angle = -13.50)
queen_gracie_lensified.save("queen_gracie_lensified.png", format = "png")

import io

from PIL import Image
import ipydraw
print("You can change the color by clicking on the color pallette next to the Clear button")
print("Click the clear button to start over.")
canvas = ipydraw.Canvas(
    # optional arguments
    size=(400, 200),
    color=True,
#     line_width=5,
)
canvas

from codexutils import get_image_from_canvas, load_and_resize_image
my_drawn_img = get_image_from_canvas(canvas)
my_drawn_img

my_selfie = load_and_resize_image("top-25-largest-lakes.png") # replace with filename of your selfie image 
my_selfie

import ipywidgets
from ipywidgets import interact
image = my_selfie
@interact(
    x = ipywidgets.IntSlider(default = 0, min= 0, max = image.width, continuous_update=False),
    y = ipywidgets.IntSlider(default = 0, min = 0, max = image.height, continuous_update=False),
    scale = ipywidgets.FloatSlider(1, min = 0.2, max = 1.5, continuous_update = False),
    angle = ipywidgets.FloatSlider(min = -180, max = 180, continuous_update = False),
)
def _(x, y, scale, angle):
    return base_plus_lens(image, my_drawn_img, dest=(x, y), scale = scale, angle = angle)

my_selfie_lensified = base_plus_lens(my_selfie, my_drawn_img, dest = (227, 110), scale = 1.00, angle = 0.00)

from PIL import ImageDraw, ImageFont

base =  my_selfie_lensified.convert("RGBA") 
# make a blank image for the text, initialized to transparent text color
txt = Image.new("RGBA", base.size, (255,255,255,0))

# set signature attributes 
signed_text = 'Made By \n Moi' # change it to your name. The \n puts a newline
signature_location = (0,0) # change it to where you want signature to appear
signature_color = 'red'  # (optional) change it to a different color  

signature_font_size = 10  # change it to whatever font size you want

ttf_font_file = 'data/Poseidonia.ttf' # if you upload a new ttf file  remove data/ since it will upload to main directory
signature_font = ImageFont.truetype(ttf_font_file, size = signature_font_size)
    
# get a drawing context
d = ImageDraw.Draw(txt)

# draw text 
d.multiline_text(signature_location, signed_text, font = signature_font, fill = signature_color)

# composite them together
my_signed_selfie_lens = Image.alpha_composite(base, txt)
    
my_signed_selfie_lens
my_signed_selfie_lens.save("my_signed_selfie_lensified.png", format = "png")
