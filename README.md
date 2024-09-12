# Hurricane Tracker

A Python program to visualize the path of hurricanes in the North Atlantic Basin.

## Author

Rodolfo Lopez

## Date

Fall 2019

## Features

- Animates hurricane paths using turtle graphics
- Color-codes hurricane intensity based on the Saffir-Simpson scale
- Displays hurricane category numbers along the path

## Dependencies

- Python 3.x
- Turtle graphics library (included in Python standard library)

## Usage

1. Ensure you have Python installed on your system.
2. Place the `hurricane_tracker.py` file, the `atlantic-basin.gif` image, and the `hurricane.gif` image in the same directory.
3. Run the program:

   ```
   python hurricane_tracker.py
   ```

4. When prompted, enter the name of the CSV file containing hurricane data (e.g., "irma.csv").

## CSV File Format

The program expects hurricane data in CSV format with the following columns:

1. Date and time
2. Time zone
3. Latitude
4. Longitude
5. Wind speed (in mph)
6. Pressure (in millibars)

## Acknowledgments

Dr. Sat Garcia wrote the starter code and I implemented the animate, get_category, and get_color fucntions.
