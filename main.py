import cv2 as cv
import numpy as np
import os

filepath = "GenarateData/Source/BG/"
itemname = ["beaker", "goggle", "hammer", "kapton_tape", "pipette", "screwdriver", "thermometer", "top", "watch", "wrench"]
chooesImage = "wrench"
imagepath = filepath + chooesImage + ".png"
savelocation = "GenarateData/data/" + chooesImage + "/"
item = ["beaker","goggle","hammer","kapton_tape","pipette","screwdriver","thermometer","top","watch","wrench"]
def show_img(path):
    img = cv.imread(path)
    cv.imshow("IMG", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def show_rotate_img(path, angle):
    img = cv.imread(path)
    rotated = rotate_image(img, angle)
    cv.imshow("Rotated IMG", rotated)
    cv.waitKey(0)
    cv.destroyAllWindows()

def rotate_image(image, angle):
    # Get the image dimensions
    (h, w) = image.shape[:2]
    # Calculate the center of the image
    center = (w // 2, h // 2)
    # Get the rotation matrix
    M = cv.getRotationMatrix2D(center, angle, 1.0)
    
    # Calculate the new bounding dimensions of the image
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    new_w = int((h * sin) + (w * cos))
    new_h = int((h * cos) + (w * sin))
    
    # Adjust the rotation matrix to take into account the translation
    M[0, 2] += (new_w / 2) - center[0]
    M[1, 2] += (new_h / 2) - center[1]
    
    # Perform the rotation and resize the image, specifying a white border
    rotated = cv.warpAffine(image, M, (new_w, new_h), borderValue=(255, 255, 255))
    return rotated

def save_rotated_image(input_path, angle, output_path):
    img = cv.imread(input_path)
    if img is None:
        print(f"Error: Unable to load image at {input_path}")
        return
    rotated_img = rotate_image(img, angle)
    
    # Ensure the output directory exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # Create the full output file path with extension
    filename = f"{chooesImage}-{angle}.png"
    full_output_path = os.path.join(output_path, filename)
    
    # Resize the rotated image
    target_size = (478, 478)  # Change the target size as needed
    resized_image = cv.resize(rotated_img, target_size)
    
    # Save the resized image
    cv.imwrite(full_output_path, resized_image)
    print(f"Image saved to {full_output_path}")


# Example usage
# save_rotated_image(imagepath, 30, savelocation)

mkdir_path = "GenarateData/data/"
for name in item:
    newpath = mkdir_path + name
    os.makedirs(newpath)

for name in item:
    for i in range (0,360,5):
        chooesImage = name
        imagepath = filepath + chooesImage + ".png"
        savelocation = "GenarateData/data/" + chooesImage + "/"
        save_rotated_image(imagepath, i, savelocation)
        print(i)
    print("-----------------------------")
