import netpbmfile, os
import numpy as np
from imageai.Detection import ObjectDetection

execution_path = os.getcwd()

def object_filtering(file_name1,file_name2,file_name3,output):
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()  

    detections1 = detector.detectObjectsFromImage(input_image=os.path.join(execution_path,file_name1),output_image_path=os.path.join(execution_path,"detection.ppm"))
    for eachObject in detections1:
        print(eachObject["name"], ":", eachObject["percentage_probability"])
    """
    use netpbmfile to convert ppm file to 3d numpy array
    then just make manual framing of perceived foreign objects.
    Otherwise input of computer vision technology is necessary.
    """ 

    def padding(image,image1,image2):
        """
        calculate necessary padding and image positions for foriegn objects
        """
        padding_length = max([image.shape[0],image1.shape[0],image2.shape[0]])
        padding_width = sum([image.shape[1],image1.shape[1],image2.shape[1]])
        rgb = 3
        image_colpos = image.shape[1]
        image1_colpos = image_colpos + image1.shape[1]
        image2_colpos = image1_colpos + image2.shape[1] 
        return np.zeros([padding_length,padding_width,rgb],dtype=np.int64),image_colpos,image1_colpos,image2_colpos

    # open user input files simulataneously
    with netpbmfile.NetpbmFile(file_name1) as ppm, \
    netpbmfile.NetpbmFile(file_name2) as ppm1, \
    netpbmfile.NetpbmFile(file_name3) as ppm2:

        # convert ppm to numpy array
        image,image1,image2 = ppm.asarray(),ppm1.asarray(),ppm2.asarray()
        #frame perceived foreign objects
        image = image[(image.shape[0])//3:((image.shape[0])//3)*2,:(image.shape[1])//2]
        image1 = image1[(image1.shape[0])//2:(image1.shape[0]//3)*2,(image1.shape[1])//3:(image1.shape[1]//3) *2]
        image2 = image2[(image2.shape[0])//8:((image2.shape[0])//8)*4,((image2.shape[1]//3))*2:]

        # padding and decide concantenation points for new image
        result,image_colpos,image1_colpos,image2_colpos = padding(image,image1,image2)
        # position foreign objects to new image
        result[:image.shape[0],:image_colpos] = image
        result[:image1.shape[0],image_colpos:image1_colpos] = image1
        result[:image2.shape[0],image1_colpos:image2_colpos] = image2
        # write to file
        netpbmfile.imwrite("{output}.ppm".format(output=output),result)
        
    

def shades_of_gray(file_name1, output):
    """
    iterate through 3d numpy array, aggregate inner most nested RGBs
    to average original RGB.
    then just write to file.
    """
    with netpbmfile.NetpbmFile(file_name1) as ppm:
        ppm.axes
        ppm.shape
        ppm.dtype
        ppm.maxval
        ppm.magicnum
        image = ppm.asarray()
        for row in image:
            for i,column in enumerate(row):
                row[i] = column.shape[0] * [column.mean()]
        netpbmfile.imwrite("{output}".format(output=output),image)

def horizontal_flip(file_name,output):
    """
    use numpy.fliplr to flip image that
    was written to 3d numpy array
    """
    with netpbmfile.NetpbmFile(file_name) as ppm:
        ppm.axes
        ppm.shape
        ppm.dtype
        ppm.maxval
        ppm.magicnum
        image = ppm.asarray()

        netpbmfile.imwrite("{output}".format(output=output),np.fliplr(image))
    



