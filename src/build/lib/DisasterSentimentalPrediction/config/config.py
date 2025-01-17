import pathlib
import os
import DisasterSentimentalPrediction

PACKAGE_ROOT = pathlib.Path(DisasterSentimentalPrediction.__file__).resolve().parent
DATAPATH = os.path.join(PACKAGE_ROOT, "data")
TRAIN_FILE = os.path.join(DATAPATH, "train.csv")
TEST_FILE = os.path.join(DATAPATH, "test.csv")
VAL_FILE = os.path.join(DATAPATH, "val.csv")
MODEL_NAME = 'models'
SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT, 'trained_models', MODEL_NAME)


TARGET = 'target'

FEATURES = ["index","id","keyword","location","text"]

FEATURES_TO_PREDICT = "text"

STRING_FEATURES = ["test"]

COLUMNS_TO_DROP = ["index","id","keyword","location"]

