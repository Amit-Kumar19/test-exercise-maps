import sys
from readkmlfile import KmlToDf
from filter_coordinates import FilterKmlData


def main(file_path: str) -> str:
    """ Driver method which processes the KML file passed and filters the correct co-ordinates ,
    calculates the total distance covered in KM.
    """

    read_kml_file = KmlToDf(file_path)
    coordinates_df = read_kml_file.read_kml_file()

    correct_co_ordinates = FilterKmlData(coordinates_df)
    total_distance = correct_co_ordinates.filter_kml_data()

    # Uncomment the below line to convert correct co-ordinates to a Excel File.
    # correct_coordinates = correct_co_ordinates.correct_coordinates()

    return total_distance


if __name__ == '__main__':
    kml_file_path = sys.argv[1]
    if kml_file_path.endswith(".kml"):
        print(main(kml_file_path))
    else:
        print("Kindly pass a KML file!")
