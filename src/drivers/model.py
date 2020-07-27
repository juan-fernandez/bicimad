import argparse
from argparse import Namespace
from src.general.operations.dataframe_operations import load_dataframe_from_csv, load_dataframe_from_json, save_dataframe
from src.bicimad.operations.cleaning_operations import clean_weather_data
from src.bicimad.operations.aggregation_operations import prepare_daily_data

from src.bicimad.constants.paths import *
from src.bicimad.constants.weather_constants import *
from src.bicimad.constants.bikes_constants import *

# Before executing: export PYTHONPATH="/home/irene/dev/keepler-prueba/keepler-bicimad:$PYTHONPATH"

def create_path(home_path: str, relative_path: str) -> str:
    return home_path + '/' + relative_path


def runner(args: Namespace) -> None:
    dataset = load_dataframe_from_csv(create_path(args.home_path, PATH_DATASET.get(args.sampling_frequency)))


def main():
    # args: --home-path /home/irene/dev/keepler-prueba/keepler-bicimad --sampling-frequency daily
    print("[data-modeling] Starting ... ")
    parser = argparse.ArgumentParser(description='[BiciMad Project] Data Cleaning')
    parser.add_argument('--home-path', type=str, default='.', metavar='H',
                        help='home path')
    parser.add_argument('--sampling-frequency', type=str, default='daily', metavar='S',
                        help='Sampling frequency of data: daily/hourly ')

    args: Namespace = parser.parse_args()
    print("[data-modeling] Setting home path as: {}".format(args.home_path))
    print("[data-modeling] Preparing [{}] data".format(args.sampling_frequency))
    runner(args)
    print("[data-modeling] Success: Prepared data stored in {}.".format(create_path(args.home_path, PATH_DATASET.get(args.sampling_frequency))))


if __name__ == '__main__':
    main()