import cv2
import os

class Basilio:
    def diffImg(self, t0, t1, t2):
        d1 = cv2.absdiff(t2, t1)
        d2 = cv2.absdiff(t1, t0)
        return cv2.bitwise_and(d1, d2)
    
    def getGreyScaleImage(self):
        return cv2.cvtColor(self.cam.read()[1], cv2.COLOR_RGB2GRAY)

    def getBinaryImage(self, image):
        (thresh, image) = cv2.threshold(image, 220, 255, cv2.THRESH_BINARY)
        return image
    
    def getNumberOfWhite(self, image):
        return cv2.countNonZero(image)

    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.max_number_of_white_ratio = 0.002
        self.camshot_file_path = "/tmp/camshot.avi"
    
    def motionDetected(self, image):
        number_of_white = self.getNumberOfWhite(image)
        number_of_white_ratio = float(number_of_white) / float(image.size)
        return number_of_white_ratio > self.max_number_of_white_ratio

    def waitForHim(self, frames_to_wait):
        t_minus = self.getGreyScaleImage()
        t = self.getGreyScaleImage()
        t_plus = self.getGreyScaleImage()
        is_here = False
        while frames_to_wait > 0:
            diff = self.diffImg(self.getBinaryImage(t_minus), self.getBinaryImage(t), self.getBinaryImage(t_plus))
            
            if self.motionDetected(diff):
                is_here = True
                break
            t_minus = t
            t = t_plus
            t_plus = self.getGreyScaleImage()
            frames_to_wait -= 1
        return is_here     

    def recordHim(self, number_of_frames):
        
        # Define the codec and create VideoWriter object
        fourcc = cv2.cv.CV_FOURCC(*'XVID')
        out = cv2.VideoWriter(self.camshot_file_path,fourcc, 20.0, (640,480))
    
        while number_of_frames > 0 and self.cam.isOpened():
            ret, frame = self.cam.read()
            if ret==True:
                number_of_frames -= 1
                out.write(frame)
        out.release()
        return open(self.camshot_file_path, 'rb')
    
    def callHim(self, voice_file_path):
        os.system("cvlc --play-and-exit -A alsa --alsa-audio-device hw:0,0  " + voice_file_path)

        
