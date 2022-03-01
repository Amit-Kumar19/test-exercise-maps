from pykml import parser
import pandas as pd


class KmlToDf:
    """ Reads the KML file passed and converts the co-ordinates into a pandasDF.
    """

    co_ordinate_value = []

    def __init__(self, filepath: str):
        self.filepath = filepath

    def kml_to_df(self):
        """ Converts the co-ordinates read into a PandasDF """

        column_names = ["longitude", "latitude", "altitude"]
        coordinates_df = pd.DataFrame(self.co_ordinate_value, columns=column_names)

        return coordinates_df

    def read_kml_file(self) -> pd.DataFrame:
        """Reads the KML file passed and extract the co-ordinates section. """

        try:
            with open(self.filepath) as kml_file:
                data = parser.parse(kml_file).getroot()

            co_ordinates = data.Document.Folder.Placemark.LineString.coordinates.text.strip().split(" ")
            for co_ordinate in co_ordinates:
                co_ordinate_val = co_ordinate.split(",")
                self.co_ordinate_value.append(co_ordinate_val)

            df = self.kml_to_df()

            return df

        except Exception as error:
            print(error)



