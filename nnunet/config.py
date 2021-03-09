import os

DEFAULT_DATA_PATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "data"
))
DEFAULT_RAW_DATASET_DIR = os.path.join(DEFAULT_DATA_PATH, "raw_dataset_dir")
DEFAULT_SPLITTED_4D_OUTPUT_DIR = os.path.join(
    DEFAULT_DATA_PATH, "splitted_4d_output_dir"
)
DEFAULT_CROPPED_OUTPUT_DIR = os.path.join(
    DEFAULT_DATA_PATH, "cropped_output_dir"
)
DEFAULT_PRE_PROCESSING_OUTPUT_DIR = os.path.join(
    DEFAULT_DATA_PATH, "pre_processing_output"
)
DEFAULT_NETWORK_TRAINING_OUTPUT_DIR = os.path.join(
    DEFAULT_DATA_PATH, "training_output"
)
DEFAULT_PLANS_IDENTIFIER = "plan_identifier"

RAW_DATASET_DIR_ENV = "RAW_DATASET_DIR"
SPLITTED_4D_OUTPUT_DIR_ENV = "SPLITTED_4D_OUTPUT_DIR"
CROPPED_OUTPUT_DIR_ENV = "CROPPED_OUTPUT_DIR"
PRE_PROCESSING_OUTPUT_DIR_ENV = "PRE_PROCESSING_OUTPUT_DIR"
NETWORK_TRAINING_OUTPUT_DIR_ENV = "NETWORK_TRAINING_OUTPUT_DIR"

RAW_DATASET_DIR = os.getenv(RAW_DATASET_DIR_ENV, DEFAULT_RAW_DATASET_DIR)
SPLITTED_4D_OUTPUT_DIR = os.getenv(
    SPLITTED_4D_OUTPUT_DIR_ENV, DEFAULT_SPLITTED_4D_OUTPUT_DIR
)
CROPPED_OUTPUT_DIR = os.getenv(
    CROPPED_OUTPUT_DIR_ENV, DEFAULT_CROPPED_OUTPUT_DIR
)
PRE_PROCESSING_OUTPUT_DIR = os.getenv(
    PRE_PROCESSING_OUTPUT_DIR_ENV, DEFAULT_PRE_PROCESSING_OUTPUT_DIR
)
NETWORK_TRAINING_OUTPUT_DIR = os.getenv(
    NETWORK_TRAINING_OUTPUT_DIR_ENV, DEFAULT_NETWORK_TRAINING_OUTPUT_DIR
)
TARGET_TRAIN_DATA_DIR = "imagesTr"
TARGET_TRAIN_LABELS_DIR = "labelsTr"
TARGET_TEST_DATA_DIR = "imagesTs"
