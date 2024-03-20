# This code provides functionality for registering a fixed and moving image based on the Dicom Registration file
# Installation guide
    pip install RegisteringImages
## Highly recommend to also have DicomRTTool installed
    pip install DicomRTTool
Example:

    from DicomRTTool import DicomReaderWriter
    from RegisterImages.WithDicomReg import register_images_with_dicom_reg, pydicom, sitk
    
    fixed_reader = DicomReaderWriter()
    moving_reader = DicomReaderWriter()
    
    registration_file = 'some_path_to_registration'
    dicom_registration = pydicom.read_file(registration_file)
    
    fixed_path = 'some_path_to_fixed_image'
    moving_path = 'some_path_to_moving_image'

    fixed_reader.down_folder(fixed_path)
    moving_reader.down_folder(moving_path)
    fixed_image = sitk.Cast(primary_reader.dicom_handle, sitk.sitkFloat32)
    moving_image = sitk.Cast(secondary_reader.dicom_handle, sitk.sitkFloat32)
    
    resampled_moving = register_images_with_dicom_reg(fixed_image=fixed_image, moving_image=moving_image, dicom_registration=dicom_registration)
    
