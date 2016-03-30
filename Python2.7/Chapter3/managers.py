import cv2
import numpy
import time

class CaptureManager(object):
	def __init__(self,capture, previewWindowsManager = None, 
				 shouldMirrorPreview = False):
		self.previewWindowsManager = previewWindowsManager
		self.shouldMirrorPreview = shouldMirrorPreview


		self._capture = capture
		self._channel = 0
		self._enteredFrame = False
		self._frame = None
		self._imageFilename = None
		self._videoFilename = None
		self._videoEncoding = None
		self._videoWriter = None

		self._startTime = None
		self._framesElapsed = long(0)
		self._fpsEstimate = None

	@property
	def channel(self):
	    return self._channel

	@property
	def frame(self):
	    if self._enteredFrame and self._frame is None:
	    	_, self._frame = self._capture.retrieve(channel = self.channel)
	    return self._frame

	@channel.setter
	 def channel(self, value):
	 	if self._channel != value:
	 		self._channel = value
	 		slef._frame = None

	@property
	 def isWritingImage(self):
	     return self._isWritingImage is not None
	 
	@property
	def isWritingVideo(self):
	    return self._isWritingVideo is not None


	def enterFrame(self):
		'''Capture the next frame, if any. '''
		#But first check that any privious frame was exited.
		assert not self._enteredFrame, \
			'previous enterFrame() had no matching exitFrame()'
		if self._capture is not None:
			self._enteredFrame = self._capture.grab()


	def exitFrame(self):
		''' Draw to the windows. write to files. release the frame'''
		#Check whether any grabbed frame is retrievable.
		#The getter may retrieve and the frame.
		
	
	
