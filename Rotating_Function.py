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
