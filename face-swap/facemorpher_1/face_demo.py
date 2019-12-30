import facemorpher

# Get a list of image paths in a folder
imgpaths = facemorpher.list_imgpaths('imagefolder')

# To morph, supply an array of face images:
facemorpher.morpher(imgpaths, plot=True)

# To average, supply an array of face images:
facemorpher.averager(['image1.png', 'image2.png'], plot=True)