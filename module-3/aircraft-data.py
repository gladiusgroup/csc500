from array import array

# Initialize an array to store aircraft data
aircraft_data = array('d')  # need the 'd' for double-precision or it gets mad

# Function to add a new data
def add_location(lat, long, alt, hdg, spd, dt):
    global aircraft_data
    aircraft_data.extend([lat, long, alt, hdg, spd, dt])

# Let's add some samele data points, we'll use epoch time so this whole array thing works okay
add_location(40.7128, -74.0060, 30000, 180, 500, 1701363600)
add_location(41.8781, -87.6298, 35000, 190, 520, 1701363601)

# Display the data we saved in the array
data_len = len(aircraft_data)
for i in range(0, data_len, 6):
    lat, long, alt, hdg, spd, dt = aircraft_data[i:i+6]
    print(f'Latitude: {lat}, Longitude: {long}, Altitude: {alt}, Heading: {hdg}, Speed: {spd}, Datetime (Unix epoch): {dt}')
