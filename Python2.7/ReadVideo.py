import cv2
def main():
	videoCapture = cv2.videoCapture("/Users/Haoyang/MyOutAvi.")

	fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)

	size = (int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
			int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

	success, frame = videoCapture.read()
	cv2.namedWindow("Test")
	while success:
		cv2.imshow("Test",frame)
		success, frame = videoCapture.read()


main()
