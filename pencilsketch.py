import cv2

def pencil_sketch(image_path, output_path):
    img = cv2.imread(image_path)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted_image = cv2.bitwise_not(gray_image)
    blurred = cv2.GaussianBlur(inverted_image, (111, 111), 0)
    inverted_blurred = cv2.bitwise_not(blurred)
    sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    cv2.imwrite(output_path, sketch)
    cv2.imshow('Original Image', img)
    cv2.imshow('Pencil Sketch', sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
image_path = 'C:/Users/91738/OneDrive/Pictures/ironman.jpeg'  
output_path = 'C:/Users/91738/OneDrive/Pictures/iron_pencil.jpeg'   
pencil_sketch(image_path, output_path)
