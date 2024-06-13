import csv
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import time

# Function to get the coordinates (latitude, longitude) of a location with retries
def get_coordinates(location, retries=3, delay=1):
    geolocator = Nominatim(user_agent="city_locator")
    for i in range(retries):
        try:
            location = geolocator.geocode(location, timeout=10)
            if location:
                return (location.latitude, location.longitude)
            else:
                raise ValueError("Location not found")
        except Exception as e:
            print(f"Error retrieving coordinates: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
            delay *= 2
    raise ConnectionError("Failed to retrieve coordinates after several attempts")

# Function to calculate distance between two coordinates
def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).miles

# Function to filter cities within a specified distance
def filter_cities_within_distance(target_coords, cities, max_distance):
    filtered_cities = []
    for city, city_coords in cities.items():
        try:
            distance = calculate_distance(target_coords, city_coords)
            if distance <= max_distance:
                filtered_cities.append((city, distance))
        except Exception as e:
            print(f"Error calculating distance for {city}: {e}")
    return filtered_cities

# Function to read cities from a CSV file
def read_cities_from_csv(filepath):
    cities = {}
    with open(filepath, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            city = row['Cities'].strip()  # Adjust column name here
            latitude = float(row['Latitude'])
            longitude = float(row['Longitude'])
            cities[city] = (latitude, longitude)
    return cities

# Filepath to the CSV file
filepath = "C:\\New folder\\50miles_radius_newyork2.csv"

# Read cities from the CSV file
cities = read_cities_from_csv(filepath)

# Input target city
target_city = input("Enter the target city: ")

# Get coordinates of the target city
try:
    target_coords = get_coordinates(target_city)
except Exception as e:
    print(f"Failed to get coordinates for {target_city}: {e}")
    target_coords = None

if target_coords:
    # Maximum distance in miles
    max_distance = 50

    # Filter cities within 50 miles from the target city
    filtered_cities = filter_cities_within_distance(target_coords, cities, max_distance)

    # Print filtered cities with numbers, excluding the target city
    print(f"Cities within {max_distance} miles from {target_city}:")
    for i, (city, distance) in enumerate(filtered_cities, start=1):
        if city.lower() != target_city.lower():
            print(f"{i}. {city} - Distance: {round(distance, 2)} miles")

    # Print total number of cities within the specified distance
    print(f"Total cities within {max_distance} miles: {len(filtered_cities)}")

    # Filepath to save the extracted details
    output_filepath = "C:\\New folder\\50miles_radius_dallas2.csv"

    # Write the extracted details to the CSV file
    with open(output_filepath, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["City", "Distance (miles)"])  # Write header
        for city, distance in filtered_cities:
            writer.writerow([city, round(distance, 2)])

    print(f"Data saved to: {output_filepath}")
else:
    print("Unable to proceed without target city coordinates.")
