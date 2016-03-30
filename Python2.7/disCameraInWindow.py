import cv2

def main():
	cameraCapture = cv2.VideoCapture(0)

	cv2.namedWindow("Video")
	
	fps = 24
	'''
	size = (int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
			int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
	videoWriter = cv2.videoWriter("/Users/Haoyang/Downloads/test.avi",
									cv2.cv.CV_FOURCC('I','4','2','0'),
									fps,size)
'''
	sucess, frame = cameraCapture.read()

	numFrames = 10 * fps -1
	while sucess and numFrames > 0:
		cv2.imshow("Video",frame)
		sucess,frame = cameraCapture.read()
		numFrames = numFrames - 1


	cv2.destroyWindow('Video')
	#cv2.waitKey(0)


main()
