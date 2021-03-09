#    Copyright 2019 Division of Medical Image Computing, German Cancer Research Center (DKFZ), Heidelberg, Germany
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from collections import OrderedDict
from glob import glob
from typing import List, Set

from batchgenerators.utilities.file_and_folder_operations import *

from nnunet.config import DEFAULT_RAW_DATASET_DIR, TARGET_TEST_DATA_DIR, \
    TARGET_TRAIN_LABELS_DIR, TARGET_TRAIN_DATA_DIR
from nnunet.utilities.argparse import ArgParserBuilder

KITS_TRAINING_CASES = {i for i in range(210)}
KITS_TEST_CASES = {i for i in range(210, 300)}
DATA_FILE_NAME = "imaging.nii.gz"
SEGMENTATION_FILE_NAME = "segmentation.nii.gz"



def get_kits_cases_directories(
    input_dataset_dir: str,
    cases_numbers: Set[int]
) -> List[str]:
    all_cases_dirs = glob(os.path.join(input_dataset_dir, "case_*"))
    return [
        d for d in all_cases_dirs
        if int(d.split("_")[-1]) in cases_numbers
    ]


if __name__ == "__main__":
    parser = ArgParserBuilder() \
        .initialize_build(parser_name="KiTS2019 dataset converter") \
        .add_input_dataset_dir_parameter() \
        .finish_build()
    args = parser.parse_args()
    out_folder = os.path.join(DEFAULT_RAW_DATASET_DIR, "KITS2019")
    target_train_data_path = os.path.join(out_folder, TARGET_TRAIN_DATA_DIR)
    target_train_labels_path = os.path.join(out_folder, TARGET_TRAIN_LABELS_DIR)
    target_test_data_path = os.path.join(out_folder, TARGET_TEST_DATA_DIR)
    for path in [target_train_data_path, target_train_labels_path, target_test_data_path]:
        os.makedirs(path, exist_ok=True)

    # train
    all_train_files = []
    patient_dirs_train = get_kits_cases_directories(
        input_dataset_dir=args.input_dataset_dir,
        cases_numbers=KITS_TRAINING_CASES
    )
    for current_dir in patient_dirs_train:
        case_identifier = int(current_dir.split("_")[-1])
        data_file_train = os.path.join(current_dir, DATA_FILE_NAME)
        segmentation_file_train = os.path.join(
            current_dir, SEGMENTATION_FILE_NAME
        )
        target_segmentation_file_path = os.path.join(
            target_train_labels_path, f"{case_identifier}_0000.nii.gz"
        )
        target_train_file_path = os.path.join(
            target_train_data_path, f"{case_identifier}_0000.nii.gz"
        )
        os.symlink(data_file_train, target_train_file_path)
        os.symlink(segmentation_file_train, target_segmentation_file_path)
        all_train_files.append(
            (target_train_file_path, target_segmentation_file_path)
        )

    # test
    all_test_files = []
    patient_dirs_test = get_kits_cases_directories(
        input_dataset_dir=args.input_dataset_dir,
        cases_numbers=KITS_TEST_CASES
    )
    for current_dir in patient_dirs_test:
        case_identifier = int(current_dir.split("_")[-1])
        data_file_test = os.path.join(current_dir, DATA_FILE_NAME)
        target_test_file_path = os.path.join(
            target_test_data_path,  f"{case_identifier}_0000.nii.gz"
        )
        os.symlink(data_file_test, target_test_file_path)
        all_test_files.append(target_test_file_path)

    json_dict = OrderedDict()
    json_dict['name'] = "KiTS2019"
    json_dict['description'] = "the 2019 Kidney and Kidney Tumor Segmentation Challenge"
    json_dict['tensorImageSize'] = "3D"
    json_dict['reference'] = "***"
    json_dict['licence'] = "MIT License"
    json_dict['release'] = "0.0"
    json_dict['modality'] = {
        "0": "CT",
    }
    json_dict['labels'] = {
        "0": "background",
        "1": "Kidney",
        "2": "Tumor"
    }
    json_dict['numTraining'] = len(all_train_files)
    json_dict['numTest'] = len(all_test_files)
    json_dict['training'] = [
        {
            'image': image_path,
            "label": label_path
        } for image_path, label_path in all_train_files
    ]
    json_dict['test'] = all_test_files
    save_json(json_dict, os.path.join(out_folder, "dataset.json"))
