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

# This function is defined in codexutils.py since it is not
# necessary to understand it for this lesson.
from codexutils import get_image_from_canvas
my_lens = get_image_from_canvas(canvas)
my_lens.save("my_lens.png", format = "png") ## this is how you save an image

import ipydraw
my_lens_img = Image.open("sunglasses2.png") # Or replace with my_lens.png  if you drew your own lens
print("Pick a point in the sunglasses where the left eye should be. Then pick a point where the right eye should be.")
print("Press clear to start over. Make sure they are roughly level.")
my_lens_pp = ipydraw.PointPicker.for_image(my_lens_img, n_points=2)
my_lens_pp

my_lens_points = my_lens_pp.get_points()
print(my_lens_points)

from eyedetectionutils import *
from autolensadjustutils import *
my_img_filename = "" ## replace with the name of your selfie img file 

my_img = load_and_resize_image(my_img_filename)

faces, eyes, visualized_image = detect_visualize_eyes(my_img_filename,'eye')
if eyes == []:
    print("Upload an image above for which the AI algortihm finds eyes.")
    my_custom_lens = None
else:
    angle_eyes_degrees, img_left_eye_xy, img_right_eye_xy = eyes_angle_degrees(eyes)
    distance_eyes = np.linalg.norm(np.array(img_left_eye_xy)- np.array(img_right_eye_xy))


    my_lens_left_eye_x = my_lens_points[0][0]
    my_lens_left_eye_y = my_lens_points[0][1]

    distance_lens_eyes = distance_2d_points(my_lens_points[0],my_lens_points[1])
    distance_img_eyes = distance_2d_points(img_left_eye_xy,img_right_eye_xy)
    estimated_scale = distance_img_eyes / distance_lens_eyes

    my_lens_width, my_lens_height = my_lens_img.size
    my_lens_left_eye_xy = (my_lens_left_eye_x, my_lens_left_eye_y)
    lens_dest = compute_rotated_lens_dest(img_left_eye_xy,my_lens_left_eye_xy,my_lens_width, my_lens_height,angle_eyes_degrees,estimated_scale)
    my_custom_lens = base_plus_lens(my_img,my_lens_img,  dest = lens_dest, angle = angle_eyes_degrees,scale = estimated_scale)

my_custom_lens

from PIL import ImageDraw, ImageFont
my_selfie_lensified = my_custom_lens
base =  my_selfie_lensified.convert("RGBA") 
# make a blank image for the text, initialized to transparent text color
txt = Image.new("RGBA", base.size, (255,255,255,0))

# set signature attributes 
signed_text = 'By Moi' # change it to your name. The \n puts a newline
signature_location = base.size # puts this at the bottom right - make sure you understand why
signature_color = 'orange'  # (optional) change it to a different color  

signature_font_size = 20  # change it to whatever font size you want

# if you upload a new ttf change next line to ttf_font_file = "your_font_filename.ttf"
ttf_font_file = 'data/ttf_fonts/mixedup.ttf' 
signature_font = ImageFont.truetype(ttf_font_file, size = signature_font_size)
    
# get a drawing context
d = ImageDraw.Draw(txt)

# draw text 
d.multiline_text(signature_location, signed_text, 
                 font = signature_font, 
                 anchor = "rd", # compare 'rs', 'rd', 'bs' and 'bd'
                 fill = signature_color)

# composite them together
my_signed_selfie_lens = Image.alpha_composite(base, txt)
    
my_signed_selfie_lens

my_signed_selfie_lens.save("me_and_my_auto_adjusted_lens.png", format = "png")
