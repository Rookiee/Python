import cv2

def main():
	cameraCapture = cv2.VideoCapture(0)

	fps = 30

	size = ( int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
		 int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

	videoWriter = cv2.VideoWriter('/Users/Haoyang/Downloads/MyOutAvi.avi',
								cv2.cv.CV_FOURCC('I','4','2','0'),
								fps, size)


	success, frame = cameraCapture.read()
	i = 1
	print i,(success)
	i = i+1
	numFramesRemaining = 10 * fps - 1

	while success and numFramesRemaining > 0:
		videoWriter.write(frame)
		print i,(success)
		i = i+1
		success, frame = cameraCapture.read()
		numFramesRemaining -= 1


main()
