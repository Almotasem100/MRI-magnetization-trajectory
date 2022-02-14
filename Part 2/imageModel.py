## This is the abstract class that the students should implement  

import numpy as np
import cv2 as cv
import numpy as np
# from main import ApplicationWindow


class ImageModel():
    """
    A class that represents the ImageModel"
    """

    def __init__(self):
        pass

    def __init__(self, imgPath: str):
        self.imgPath = imgPath
        ###
        # ALL the following properties should be assigned correctly after reading imgPath
        ###
        self.imgByte = cv.cvtColor(cv.imread(self.imgPath), cv.COLOR_BGR2GRAY)
        self.dft = np.fft.fft2(self.imgByte)
        self.real = np.real(self.dft)
        self.imaginary = np.imag(self.dft)
        self.magnitude = np.abs(self.dft)
        self.phase = np.angle(self.dft,deg=False)

    def mix(self, imageToBeMixed: 'ImageModel', magnitudeOrRealRatio: float, phaesOrImaginaryRatio: float,mode: 'Modes') -> np.ndarray:
        if mode == Modes.realAndImaginary :
            real=(self.real*magnitudeOrRealRatio)+(imageToBeMixed.real*(1-magnitudeOrRealRatio))
            imaginary=(imageToBeMixed.imaginary*phaesOrImaginaryRatio)+(self.imaginary*(1-phaesOrImaginaryRatio))
            Result= real + imaginary * 1J
            inverse_fourier=np.fft.ifft2(Result)

        elif mode == Modes.magnitudeAndPhase:
            magnitude = (self.magnitude * magnitudeOrRealRatio) + (imageToBeMixed.magnitude * (1 - magnitudeOrRealRatio))
            phase = (imageToBeMixed.phase * phaesOrImaginaryRatio) + (self.phase * (1 - phaesOrImaginaryRatio))
            Result = magnitude * np.exp(phase * 1j)
            inverse_fourier = np.fft.ifft2(Result)

        elif mode == Modes.uniformMagnitude :
            magnitude=np.ones(self.imgByte.shape)
            phase=(imageToBeMixed.phase * phaesOrImaginaryRatio) + (self.phase * (1 - phaesOrImaginaryRatio))
            Result = magnitude * np.exp(phase * 1j)
            inverse_fourier = np.fft.ifft2(Result)

        elif mode == Modes.uniformPhase :
            magnitude =(self.magnitude * magnitudeOrRealRatio) + (imageToBeMixed.magnitude * (1 - magnitudeOrRealRatio))
            phase = np.zeros(self.imgByte.shape)
            Result = magnitude * np.exp(phase * 1j)
            inverse_fourier = np.fft.ifft2(Result)


        elif mode==Modes.uniformMagnitudeAndPhase :
            magnitude = np.ones(self.imgByte.shape)
            phase = np.zeros(self.imgByte.shape)
            Result = magnitude * np.exp(phase * 1j)
            inverse_fourier = np.fft.ifft2(Result)
        return np.abs(inverse_fourier)