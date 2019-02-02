import numpy as np
from PIL import Image
import ShrinkImageByFactorN as sfn

def MainScript():
    fileName = './circles_concentric.png'
    img = Image.open(fileName)
    img.load()

    img_mat = np.asarray(img, dtype="float32")/255.0
    img_uint8 = Image.fromarray((img_mat * 255).astype(np.uint8))
    img_uint8.save('circles_concentric_copy.png')

    #############################################################
    # write your code here

    img_mat_by2 = sfn.ShrinkImageByFactorN(img_mat,2)
    img_mat_by3 = sfn.ShrinkImageByFactorN(img_mat,3)
    img_uint8_by2 = Image.fromarray((img_mat_by2* 255).astype(np.uint8))
    img_uint8_by2.save('Shrinkedby2.png')
    img_uint8_by3 = Image.fromarray((img_mat_by3* 255).astype(np.uint8))
    img_uint8_by3.save('Shrinkedby3.png')

    # your code ends here
    #############################################################
    


MainScript()
