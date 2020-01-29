import numpy as np
import cv2, os, glob


objectPoints = []
imagePoints = []
cameraIntrinsicValues = []
# Distortion coefficients
cameraExtrinsicValues = []

def getObjectAndImagePoints():
    global objectPoints, imagePoints

    # Number of inside corners per row and column
    cornersPerRow = 10
    cornersPerColumn = 7

    # Initializing the object points to zero
    chessboardObjectPoints = np.zeros((cornersPerColumn * cornersPerRow, 3), np.float32)

    # Prepare a meshgrid for object points
    # (0,0,0), (1,0,0), (2,0,0) ..., (cornersPerRow,cornersPerColumn,0)
    # We can do this since we know how many corners there are on our printed chessboard
    chessboardObjectPoints[:,:2] = np.mgrid[0:cornersPerRow, 0:cornersPerColumn].T.reshape(-1, 2)

    # List of calibration images
    images = []
    
    # To make sure you can run the script on any image filetype
    extensions = ['*.gif', '*.png', '*.jpeg', '*.jpg', '*.tiff']
    for extension in extensions:
        images.extend(glob.glob('calibration_images/'+extension))
    
    print(images)
    # Step through the list and search for chessboard corners
    for calibrationImageFileName in images:
        calibrationImage = cv2.imread(calibrationImageFileName)

        # The detector doesn't work well with images larger than 1280x720
        # So we'll resize any until they're 720p or smaller
        height, width = calibrationImage.shape[:2]
        while width > 1280:
            width //= 2
            height //= 2
            calibrationImage = cv2.resize(calibrationImage, (width, height))
        
        # Convert it to grayscale
        grayCalibrationImage = cv2.cvtColor(calibrationImage, cv2.COLOR_BGR2GRAY)

        # Find the image points
        cornersFound, foundCorners = cv2.findChessboardCorners(grayCalibrationImage, (cornersPerRow, cornersPerColumn),None)

        # If corners were found on the images
        # Append the found image points and defined object points to global variables
        if cornersFound:
            objectPoints.append(chessboardObjectPoints)
            imagePoints.append(foundCorners)
            
            # If you want to visualize the found corners
            cv2.drawChessboardCorners(calibrationImage, (cornersPerRow, cornersPerColumn), foundCorners, cornersFound)
            cv2.imshow('Preview', calibrationImage)
            cv2.waitKey(500)

def calibrateCamera(imageSize):
    global cameraIntrinsicValues, cameraExtrinsicValues, objectPoints, imagePoints
    retVal, cameraIntrinsicValues, cameraExtrinsicValues, rotationVectors, translationVectors = cv2.calibrateCamera(objectPoints, imagePoints, imageSize, None, None)

def undistortImage(image):
    # Returns the undistorted image
    return cv2.undistort(image, cameraIntrinsicValues, cameraExtrinsicValues, None, cameraIntrinsicValues)