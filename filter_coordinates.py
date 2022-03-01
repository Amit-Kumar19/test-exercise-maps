import pandas as pd
from geopy import distance

# Constant value on which filtering is done
CONSTANT_VALUE_IN_KM = 0.015


class FilterKmlData:
    """ Removes and calculates the distance between co-ordinates,
        Also convert the co-ordinates to a Excel file if needed.
    """

    total_distance = 0
    correct_co_ordinates = []

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def filter_kml_data(self) -> str:
        """ Removes the incorrect co-ordinates and calculates the total distance is KM"""

        coordinate_df = self.df.drop_duplicates(subset=['latitude', 'longitude'], keep='last').reset_index(drop=True)
        for index, row in coordinate_df.iterrows():
            try:
                # calculation of distance between two co-ordinates
                start_lat_long = (coordinate_df['latitude'][index], coordinate_df['longitude'][index])
                end_lat_long = coordinate_df['latitude'][index + 1], coordinate_df['longitude'][index + 1]
                calculated_distance = distance.distance(start_lat_long, end_lat_long).km

                # consider only those coordinates as correct which are less than the constant value
                if calculated_distance < CONSTANT_VALUE_IN_KM:
                    self.total_distance += calculated_distance
                    self.correct_co_ordinates.append(start_lat_long)
                    self.correct_co_ordinates.append(end_lat_long)

            except KeyError as e:
                return f"Total Distance covered is: {self.total_distance:.2f} Km"

    def correct_coordinates(self):
        """ Creates a Excel file with correct filtered co-ordinates"""

        correct_co_ordinates_df = pd.DataFrame(self.correct_co_ordinates, columns=['latitude', 'longitude'])
        correct_co_ordinates_df = correct_co_ordinates_df.drop_duplicates().reset_index(drop=True)

        correct_co_ordinates_df.to_excel("correct_ordinates.xlsx",index=False)
