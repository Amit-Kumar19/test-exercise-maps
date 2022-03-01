# Test Exercise

Scripts reads the KML file passed as a command line argument and filters out the incorrect co-ordinates and calculates the total distance covered.

## Installation

1. Clone this code:

    - `git clone https://github.com/Amit-Kumar19/test-exercise-maps.git`

2. Create a Virtual enviroment (venv or conda) and activate it.

3. Install the dependencies:
    - `pip install -r requirements.txt`

4. Try it:

    - `python main.py <kml_file_path_name> or python3 main.py <kml_file_path_name>` 
    - `Usage: python main.py F:\testexercise-ENG\task_2_sensor.kml`
    - `Expected Output: Total Distance covered is: 9.44 Km`

5. To convert the correct co-ordinates in a Excel file:
    - `Uncomment line 15 in main.py and run the code`

## Filtering Logic

1. KML file is read using pykml and the co-ordinates is extracted and converted to a Pandas DataFrame.

2. The Duplicate co-ordinates are removed.

3. Now the distance between two co-ordinates is calculated with the help of geopy and if the distance is less than a constant value then that co-ordinate is considered as correct.Constant value considered in our case = 0.015 KM. 
