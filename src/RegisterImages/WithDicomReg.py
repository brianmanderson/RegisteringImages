__author__ = 'Brian M Anderson'
# Created on 11/11/2020
import SimpleITK as sitk
import pydicom
import numpy as np


def register_images_with_dicom_reg(fixed_image, moving_image, dicom_registration=None, min_value=-1000,
                                   method=sitk.sitkLinear):
    """
    :param fixed_image: The fixed image
    :param moving_image: The moving image
    :param dicom_registration: the DICOM Registration file, if registration is from CTT 8 to 11, fixed is CT 11, moving is CT 8, 
    :param min_value: Value to put as background in resampled image
    :param method: interpolating method, recommend sitk.sitkLinear for images and sitk.sitkNearestNeighbor for masks
    :return:
    """
    assert type(fixed_image) is sitk.Image, 'You need to pass a SimpleITK image as fixed_image'
    assert type(moving_image) is sitk.Image, 'You need to pass a SimpleITK image as moving_image'
    assert type(dicom_registration) is pydicom.dataset.FileDataset \
           or dicom_registration is None, 'Pass dicom_registration as pydicom.read_file(reg_file) or None'
    affine_transform = sitk.AffineTransform(3)
    if dicom_registration is not None:
        registration_matrix = np.asarray(dicom_registration.RegistrationSequence[-1].MatrixRegistrationSequence[-1].
                                         MatrixSequence[-1].FrameOfReferenceTransformationMatrix).reshape((4, 4))
        registration_matrix = np.linalg.inv(registration_matrix)
        affine_transform.SetMatrix(registration_matrix[:3, :3].ravel())
        affine_transform.SetTranslation(registration_matrix[:3, -1])
    moving_resampled = sitk.Resample(moving_image, fixed_image, affine_transform, method, min_value,
                                     moving_image.GetPixelID())
    return moving_resampled


if __name__ == '__main__':
    pass
