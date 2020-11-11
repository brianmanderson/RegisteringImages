__author__ = 'Brian M Anderson'
# Created on 11/11/2020
import SimpleITK as sitk
import pydicom
import numpy as np


def register_images_with_dicom_reg(fixed_image, moving_image, dicom_registration, min_value=-1000):
    """
    :param fixed_image: The fixed image
    :param moving_image: The moving image
    :param dicom_registration: the DICOM Registration file
    :param min_value: Value to put as background in resampled image
    :return:
    """
    assert type(fixed_image) is sitk.Image, 'You need to pass a SimpleITK image as fixed_image'
    assert type(moving_image) is sitk.Image, 'You need to pass a SimpleITK image as moving_image'
    assert type(dicom_registration) is pydicom.dataset.FileDataset, 'Pass dicom_registration as ' \
                                                                    'pydicom.read_file(reg_file)'
    registration_matrix = np.asarray(dicom_registration.RegistrationSequence[-1].MatrixRegistrationSequence[-1].
                                     MatrixSequence[-1].FrameOfReferenceTransformationMatrix)[:-4]
    registration_matrix = np.transpose(np.reshape(registration_matrix, (3, 4)))
    registration_matrix[-1, :] *= -1
    affine_transform = sitk.AffineTransform(3)
    affine_transform.SetParameters(registration_matrix.flatten())
    moving_resampled = sitk.Resample(moving_image, fixed_image, affine_transform, sitk.sitkLinear, min_value,
                                     moving_image.GetPixelID())
    return moving_resampled