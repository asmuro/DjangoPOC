import numpy as np
import cv2

class generate_npz_process(object):
    """description of class"""

    def createNPZ(pSourceImagesPaths, pDestinationPath):
        list_images = []
        for n in pSourceImagesPaths:
            image = cv2.imread(n)    
            if len(image) == 0:
                raise Exception('Error reading image'+str(n))
            image_resized = cv2.resize(image,(256,256),interpolation=cv2.INTER_AREA)
            list_images.append(np.array(image_resized)[np.newaxis,...])


        images_np = np.concatenate(list_images,axis=0)
        np.savez(pDestinationPath+'\\poc_images.npz',images=images_np)
        return
