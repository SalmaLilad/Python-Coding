from PIL import Image
def base_plus_lens(base, lens, dest=(0, 0), scale = 1, angle = 0):
    # .convert copies the image and translates it into an RGBA colorspace
    # (i.e., RGB + transparency). This is necessary for us to add images
    # with transparency on top of it.
    pasted = base.convert("RGBA")
    
    
    lens = lens.rotate(angle,expand = True) # expand = True makes sure to enlarge image after rotation

    # scale the dimensions, round them to ints, and make sure they're >= 1px

    new_width = round(scale * lens.width)
    new_height = round(scale * lens.height)
    lens = lens.resize((new_width, new_height))

    # The methods that operate in-place (like alpha_composite) don't
    # actually return the image (they return None), so you can't chain
    # them together (like market.copy().convert().alpha_composite()).
    pasted.alpha_composite(lens, dest = dest)

    return pasted

from eyedetectionutils import * # the * means import all the functions in the module or package


import cv2 as cv # imports OpenCV and abbreviates it as cv in the namespace

def detect_visualize_eyes(image_filename,eye_model = 'eye'):
    
    frame =  cv.imread(image_filename)
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    #-- Detect faces
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades 
                                        + 'haarcascade_frontalface_alt.xml')
    faces = face_cascade.detectMultiScale(frame_gray)
    
    if len(faces) > 0 : # check to see if any faces are detected
    
        ## Some other code to zoom into only the face part of the image 
        eyes_cascade = cv.CascadeClassifier(cv_eye_model_file)
        eyes = eyes_cascade.detectMultiScale(faceROI) # faceROI is the part of image with the face 
            
    else: 
        print("no face detected")
        faces = None
        eyes_center = None
        visualized_image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        visualized_image = Image.fromarray(visualized_image)
            
    return faces, eyes_center, visualized_image

from eyedetectionutils import * # the * means import all the functions in the module or package
from ipywidgets import interact
print("Select a face from the menu - it will take 2 - 5 seconds to load, so be patient.")
@interact(face_number = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
def detect_eyes(face_number):
    image_file_name = "data/face" + str(face_number) + ".jpg"
    
    try:
        faces, eyes, visualized_image = detect_visualize_eyes(image_file_name,'eye')
        angle_eyes, left_eye, right_eye = eyes_angle_degrees(eyes)
        
        print("Left eye coordinates: ", str(left_eye))
        print("Right eye coordinates: ", str(right_eye))
        print("Right eye is  at " + str(angle_eyes) + " degrees (counter-clockwise) relative to left eye. \n ") 
        # the \n introduces a empty line
        print("Note: Positive degrees means right eye is tilted up or counter-clockwise relative to left eye.")
        print("Negative degrees means right eye is tilted down relative to left eye clockwise.")
        return display(visualized_image)
    except:
        input_image = Image.open(image_file_name)
        print("Eyes not detected")
        return input_image

from ipywidgets import interact
@interact(face_number = [12, 14, 1, 2], 
          angle_mode = ['no rotation', 'AI eye detection']
          )
def display_angled_sunglasss(face_number, angle_mode):
    image_filename = "data/face" + str(face_number) + ".jpg"
    
    sunglasses_img = Image.open("sunglasses.png")
    base_img = Image.open(image_filename)
    if angle_mode == 'AI eye detection':
        faces, eyes, visualized_image = detect_visualize_eyes(image_filename,'eye')
        angle_eyes, left_eye, right_eye = eyes_angle_degrees(eyes)
        print("Eyes estimated by AI to be  " + str(angle_eyes) + " degrees (counter-clockwise) ")
        return base_plus_lens(base_img,sunglasses_img, angle = angle_eyes) 
    else:
        return base_plus_lens(base_img,sunglasses_img)

sunglasses_img = Image.open("sunglasses.png")
sunglasses_img

import ipydraw
bg = Image.open("sunglasses.png")
print("Click on a point in the sunglasses where the left eye should be. Then pick a point where the right eye should be.")
pp = ipydraw.PointPicker.for_image(bg, n_points=2)
pp

points = pp.get_points()
print(points) 

sun_left_eye_x = 175
sun_left_eye_y = 110
sun_left_eye_xy = (175, 110)
sun_right_eye_xy = (485,110)    

import numpy as np
def distance_2d_points(point1_xy, point2_xy):

    x1 = point1_xy[0] # the first element in a Python list has index 0! 
    y1 = point1_xy[1] # the second element in a Python list has index 1!
    
    x2 = point2_xy[0]
    y2 = point2_xy[1]
    
    distance_squared = (x1 - x2)**2 + (y1 - y2)**2
    distance = np.sqrt(distance_squared) # take square root of distance_squared variable using appopriate numpy function
    
    return distance

distance_lens_eyes = distance_2d_points(sun_left_eye_xy,sun_right_eye_xy)
print(distance_lens_eyes)

from ipywidgets import interact
sunglasses_img = Image.open("sunglasses.png")

@interact(face_number = [1, 10, 11, 12, 14] ,
           anchor = ['left eye', 'right eye'],
          )
def display_angled_sunglasss(face_number, anchor):
    image_filename = "data/face" + str(face_number) + ".jpg"
    base_img = Image.open(image_filename)
    
    faces, eyes, visualized_image = detect_visualize_eyes(image_filename,'eye')
    angle_eyes, left_eye_xy, right_eye_xy = eyes_angle_degrees(eyes)
    
    distance_lens_eyes = distance_2d_points(sun_left_eye_xy,sun_right_eye_xy)
    distance_img_eyes = distance_2d_points(left_eye_xy,right_eye_xy)
    estimated_scale = distance_img_eyes / distance_lens_eyes
    print("Scaling factor : ", estimated_scale)

        
    print("Right eye estimated by AI to be  " + str(angle_eyes) + " degrees (anti-clockwise) relative to left eye.")

    if anchor == 'left eye':
        return base_plus_lens(base_img,sunglasses_img,  dest = left_eye_xy, angle = angle_eyes,scale = estimated_scale) 
    else:
        return base_plus_lens(base_img,sunglasses_img,  dest = right_eye_xy, angle = angle_eyes, scale = estimated_scale)

  import math
def rotate_img_coords(x,y,w,h,theta_radians = 0):
    
    r = math.sqrt(x**2 + y**2) # replace so that it matches the expression for r.
    gamma_radians = math.atan2(y,x)
    
    ## Assume theta is counter clockwise rotation
    net_rotation = gamma_radians - theta_radians
    
    x_bar = r * math.cos(net_rotation) 
    y_bar = r * math.sin(net_rotation)
    
    if theta_radians <= 0 :
        x_new = x_bar + h * math.sin(theta_radians)
        y_new = y_bar
    else:
        x_new = x_bar
        y_new = y_bar + w * math.sin(theta_radians)
    
    x_new = int(x_new) # make them integers since x, y coordinates of image are integers
    y_new = int(y_new)
    
    return x_new, y_new 

import math 
def compute_rotated_lens_dest(img_left_eye_xy,sun_left_eye_xy,sun_width, sun_height,angle_eyes_degrees,new_scale):
    
    sun_left_eye_x = sun_left_eye_xy[0] 
    sun_left_eye_y = sun_left_eye_xy[1]
    
    ang_eyes_radians = angle_eyes_degrees * math.pi/180 
    
    sun_leye_new_x, sun_leye_new_y = rotate_img_coords(sun_left_eye_x,sun_left_eye_y,sun_width,sun_height,ang_eyes_radians)
    
    sun_leye_new_x = new_scale * sun_leye_new_x # because rescaling just multiplies everything up/down by factor
    sun_leye_new_y = new_scale * sun_leye_new_y
    
    img_left_eye_x = img_left_eye_xy[0] # again, because first element in python has index 0!
    img_left_eye_y = img_left_eye_xy[1] # again, because second element in python has index 1!
    
    dest_x = img_left_eye_x - sun_leye_new_x
    dest_y = img_left_eye_y - sun_leye_new_y
    
    dest = (int(dest_x),int(dest_y))
    
    return dest

from PIL import Image
from ipywidgets import interact
sunglasses_img = Image.open("sunglasses.png")

print("Compare the dumb method vs the (new) AI auto adjust method to see if the math works.")
@interact(face_number = [2, 3, 4, 10, 12, 14])
def display_angled_shifted_sunglasss(face_number,comp = ['(dumb) method','(new) AI auto adjust']):
    image_filename = "data/face" + str(face_number) + ".jpg"
    base_img = Image.open(image_filename)
    
    faces, eyes, visualized_image = detect_visualize_eyes(image_filename,'eye')
    
    angle_eyes_degrees, img_left_eye_xy, img_right_eye_xy = eyes_angle_degrees(eyes)
    
    global sun_left_eye_xy
    global sun_right_eye_xy
    
    distance_lens_eyes = distance_2d_points(sun_left_eye_xy, sun_right_eye_xy)
    distance_img_eyes = distance_2d_points(img_left_eye_xy, img_right_eye_xy)
    estimated_scale = distance_img_eyes / distance_lens_eyes
    print("estimated scale = ",estimated_scale)
    
    sun_width, sun_height = sunglasses_img.size
    sun_left_eye_xy = (sun_left_eye_x, sun_left_eye_y)
    
    dest = compute_rotated_lens_dest(img_left_eye_xy,sun_left_eye_xy,sun_width, sun_height,angle_eyes_degrees,estimated_scale)
    print("Left eye estimated by AI to be  " + str(angle_eyes_degrees) + " degrees (anti-clockwise) relative to right eye.")
    print("Left eye location in image = ", img_left_eye_xy)
    print("Dest computed by AI to be = ", dest)
    if comp == '(dumb) method':
        return base_plus_lens(base_img,sunglasses_img,  dest = img_left_eye_xy, angle = angle_eyes_degrees,scale = estimated_scale) 
    else:
        return base_plus_lens(base_img,sunglasses_img,  dest = dest, angle = angle_eyes_degrees,scale = estimated_scale)
