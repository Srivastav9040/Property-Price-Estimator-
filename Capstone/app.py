import streamlit as st
import pandas as pd
import folium

# Load your dataset with place names, latitude, and longitude
# Example dataset
data = {
    'Place': ['Place A', 'Place B', 'Place C'],
    'Latitude': [37.7749, 34.0522, 40.7128],
    'Longitude': [-122.4194, -118.2437, -74.0060]
}
places_df = pd.DataFrame(data)

# Streamlit app
st.title("Place Recommendation System")

# Select two places
selected_places = st.multiselect("Select two places:", places_df['Place'].tolist())

if len(selected_places) == 2:
    start_place, end_place = selected_places

    # Get latitude and longitude for the selected places
    start_location = places_df.loc[places_df['Place'] == start_place, ['Latitude', 'Longitude']].values.flatten()
    end_location = places_df.loc[places_df['Place'] == end_place, ['Latitude', 'Longitude']].values.flatten()

    # Display the map with selected places using Folium
    m = folium.Map(location=[(start_location[0] + end_location[0]) / 2, (start_location[1] + end_location[1]) / 2], zoom_start=10)

    # Add markers for start and end locations
    folium.Marker([start_location[0], start_location[1]], popup=start_place).add_to(m)
    folium.Marker([end_location[0], end_location[1]], popup=end_place).add_to(m)

    # Draw a line between start and end locations
    folium.PolyLine(locations=[[start_location[0], start_location[1]], [end_location[0], end_location[1]]], color='blue').add_to(m)

    # Display the map using Streamlit
    st.subheader(f"Map from {start_place} to {end_place}:")
    st.write(m)

# Display the map with all places
st.map(places_df)
