import unittest

from bicimad.constants.rides import COL_BIKES_TRAVEL_TIME, COL_BIKES_DAY_OF_WEEK, COL_BIKES_DAY, COL_BIKES_MONTH
from bicimad.constants.paths import PATH_BIKES_RAW, PATH_AEMET_PER_DAY
from bicimad.constants.weather import COL_WEATHER_RAIN, COL_WEATHER_TEMP_MEAN, COL_WEATHER_WIND_MEAN
from bicimad.operations.cleaning import transform_types_bikes, remove_outliers_travel_time, clean_date_bikes, UPPER_QUANTILE, LOWER_QUANTILE, clean_weather_data
from general.operations.dataframe_operations import load_dataframe_from_csv, load_dataframe_from_json


class CleaningOperationsTest(unittest.TestCase):

    PATH_BIKES = '../../../' + PATH_BIKES_RAW
    PATH_WEATHER = '../../../' + PATH_AEMET_PER_DAY
    df_bikes = load_dataframe_from_csv(PATH_BIKES)
    df_weather = load_dataframe_from_json(PATH_WEATHER)

    def test_clean_stations(self):
        # TODO
        pass

    def test_transform_types(self):
        # TODO
        pass

    def test_remove_outliers_travel_time(self):
        # TODO improve test
        expected_shape = 0
        df_bikes = transform_types_bikes(self.df_bikes)
        upper_limit = df_bikes[COL_BIKES_TRAVEL_TIME].quantile(UPPER_QUANTILE)
        lower_limit = df_bikes[COL_BIKES_TRAVEL_TIME].quantile(LOWER_QUANTILE)
        df_bikes_clean = remove_outliers_travel_time(df_bikes)
        self.assertEqual(df_bikes_clean[(df_bikes_clean[COL_BIKES_TRAVEL_TIME] > upper_limit) &
                                        (df_bikes_clean[COL_BIKES_TRAVEL_TIME] < lower_limit)].shape[0],
                         expected_shape)

    def test_clean_date(self):
        # TODO improve test
        df_bikes = transform_types_bikes(self.df_bikes)
        df_bikes_clean = clean_date_bikes(df_bikes)
        self.assertIn(COL_BIKES_DAY_OF_WEEK, df_bikes_clean.columns)
        self.assertIn(COL_BIKES_DAY, df_bikes_clean.columns)
        self.assertIn(COL_BIKES_MONTH, df_bikes_clean.columns)

    def test_filter_out_employees(self):
        # TODO
        pass

    def test_clean_weather_data(self):
        df_weather_clean = clean_weather_data(self.df_weather)
        self.assertEqual(df_weather_clean[COL_WEATHER_RAIN].dtype, 'float32')
        self.assertEqual(df_weather_clean[COL_WEATHER_TEMP_MEAN].dtype, 'float32')
        self.assertEqual(df_weather_clean[COL_WEATHER_WIND_MEAN].dtype, 'float32')
