import cv2, numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import PIL

print("opencv: " + cv2.__version__)
print("numpy: " + np.__version__)
print("pillow: " + Image.__version__)
print()

img1 = cv2.imread(r"C:\Users\renaa\OneDrive\Pictures\backphoto.jpg")
img2 = cv2.imread(r"C:\Users\renaa\OneDrive\Pictures\hepta100ml.jpeg")
img3 = cv2.imread(r"C:\Users\renaa\OneDrive\Pictures\download.jpg")
my_images=[img1,img2,img3]
counter=0
for x in my_images:
    print("Shape: ",x.shape)
    print("Num Of Dimintions: ",x.ndim)
    print("Data Type: ", x.dtype)
    print("Size:", x.size)
    print()
    h,w,c = x.shape
    cy,cx=h//2,w//2
    r =min(h,w)//10
    y,xx= np.ogrid[:h,:w]
    mask = (xx-cx)**2 + (y-cy)**2 <= r**2
    x[mask] = [255,255,255]
    center_pixel = x[cy, cx]
    ff=x.astype(np.float32)/255.0
    result=(ff*255).astype(np.uint8)
    filename=rf"C:\Users\renaa\OneDrive\Pictures\output_{counter}.jpg"

    B,G,R =x[:,:,0],x[:,:,1],x[:,:,2]
    fig, axes = plt.subplots(1, 3,figsize=(12,4))
    for ax, ch, name in zip(axes, [B, G, R], ['Blue', 'Green', 'Red']):
        ax.imshow(ch, cmap='gray') 
        ax.set_title(name)
        ax.axis('off')
    channels_filename = rf"C:\Users\renaa\OneDrive\Pictures\channels_{counter}.png"
    plt.savefig(channels_filename)
    print("Center Pixel (BGR):", center_pixel)
    print("Center Pixel (float):", ff[cy,cx])
    print("Center Pixel (unit8):", result[cy,cx])
    print("Blue Channel: ",x[cy,cx,0])
    print("green Channel: ",x[cy,cx,1])
    print("red Channel: ",x[cy,cx,2])
    cv2.imshow('Window',x)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(filename,x)
    counter+=1
    
 



