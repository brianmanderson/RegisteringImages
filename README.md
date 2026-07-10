# RegisteringImages

Small Python package that applies a DICOM Spatial Registration (REG) file to a pair of images: it reads the 4x4 `FrameOfReferenceTransformationMatrix` from the registration DICOM, inverts it into a SimpleITK affine transform, and resamples the moving image onto the fixed image's grid. Lets you reproduce in Python a rigid/affine registration that was created elsewhere and saved as a DICOM REG object, instead of re-registering from scratch.

## Installation

    pip install RegisteringImages

Recommended companion for loading DICOM image series:

    pip install DicomRTTool

## Key functions (`RegisterImages.WithDicomReg`)

- `register_images_with_dicom_reg(fixed_image, moving_image, dicom_registration, min_value=-1000, method=sitk.sitkLinear)` — uses the last registration in the file; also accepts a raw 4x4 matrix in place of the pydicom dataset. Returns the resampled moving image.
- `registerDicom(fixed_image, moving_image, moving_series_instance_uid, dicom_registration, ...)` — for registration files containing multiple registrations: selects the one matching the moving image's SeriesInstanceUID. Pass `return_affine=True` to also get the `sitk.AffineTransform`.

Use `sitk.sitkLinear` for images and `sitk.sitkNearestNeighbor` for masks. `min_value` sets the background fill (default -1000, i.e. air in HU).

## Requirements

Python 3 with SimpleITK, pydicom, and numpy.

## Example

    from DicomRTTool import DicomReaderWriter
    from RegisterImages.WithDicomReg import register_images_with_dicom_reg, pydicom, sitk

    fixed_reader = DicomReaderWriter()
    moving_reader = DicomReaderWriter()

    dicom_registration = pydicom.read_file('some_path_to_registration')

    fixed_reader.down_folder('some_path_to_fixed_image')
    moving_reader.down_folder('some_path_to_moving_image')

    fixed_image = sitk.Cast(fixed_reader.dicom_handle, sitk.sitkFloat32)
    moving_image = sitk.Cast(moving_reader.dicom_handle, sitk.sitkFloat32)

    resampled_moving = register_images_with_dicom_reg(fixed_image=fixed_image, moving_image=moving_image,
                                                      dicom_registration=dicom_registration)

Credit: Bastien Rigaud contributed substantially to the original implementation. Licensed under GPL v3 (see LICENSE.txt).
