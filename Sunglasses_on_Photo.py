from autolensadjustutils import *
from eyedetectionutils import *
my_img_filename = "" ## replace with name of file you uploaded 
my_img = load_and_resize_image(my_img_filename)
faces, eyes, visualized_image = detect_visualize_eyes(my_img_filename,'eye')
visualized_image

if eyes == []:
    print("Upload an image above for which the AI algortihm finds eyes.")
    my_lensified_img = None
else:
    angle_eyes_degrees, img_left_eye_xy, img_right_eye_xy = eyes_angle_degrees(eyes)

    distance_eyes = np.linalg.norm(np.array(img_left_eye_xy)- np.array(img_right_eye_xy))


    sunglasses_img = Image.open("sunglasses.png")
    sun_left_eye_x = 170
    sun_left_eye_y = 110
    distance_lens_eyes = 310
    distance_img_eyes = distance_2d_points(img_left_eye_xy, img_right_eye_xy)
    estimated_scale = distance_img_eyes / distance_lens_eyes


    estimated_scale = distance_eyes / distance_lens_eyes
    sun_width, sun_height = sunglasses_img.size
    sun_left_eye_xy = (sun_left_eye_x, sun_left_eye_y)
    lens_dest = compute_rotated_lens_dest(img_left_eye_xy,sun_left_eye_xy,sun_width, sun_height,angle_eyes_degrees,estimated_scale)
    my_lensified_img = base_plus_lens(my_img,sunglasses_img,  dest = lens_dest, angle = angle_eyes_degrees,scale = estimated_scale)
my_lensified_img

my_lensified_img.save("my_auto_lensified.png",  format = "png")
