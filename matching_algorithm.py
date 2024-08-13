import sqlite3
import os
import pandas as pd
import numpy as np
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

# Define the User class
class User:
    def __init__(self, user_id, name, age, gender, location, interests,
                 liked_users=None, disliked_users=None, matches=None):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.gender = gender
        self.location = location
        self.interests = interests
        # might not be empty if existing user (future)
        self.liked_users = liked_users if liked_users is not None else []
        self.disliked_users = disliked_users if disliked_users is not None else []
        self.matches = matches if matches is not None else []

    def like(self, other_user):
        if other_user.user_id not in self.liked_users:
            self.liked_users.append(other_user.user_id)
        if self.user_id in other_user.liked_users and other_user.user_id not in self.matches:
            self.matches.append(other_user.user_id)
            other_user.matches.append(self.user_id)

    def dislike(self, other_user):
        if other_user.user_id not in self.disliked_users:
            self.disliked_users.append(other_user.user_id)

    def __repr__(self):
        return (f'User({self.user_id}, {self.name}, {self.age}, {self.gender}, '
                f'{self.location}, {self.interests}, {self.liked_users}, '
                f'{self.disliked_users}, {self.matches})')


def setup_database():
    db_file = 'users.db'
    # If DB exists - delete it upon setup:
    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"Deleted existing database file: {db_file}")
    # Create a connection to the SQLite database

    conn = sqlite3.connect(db_file)

    # Create a cursor object
    cursor = conn.cursor()

    # Create a table for storing user information
    cursor.execute('''
      CREATE TABLE IF NOT EXISTS users (
          user_id INTEGER PRIMARY KEY,
          name TEXT,
          age INTEGER,
          gender TEXT,
          location TEXT,
          interests TEXT,
          liked_users TEXT,
          disliked_users TEXT,
          matches TEXT
      )
  ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()


def insert_user(user):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Convert lists to comma-separated strings for storage
    liked_users = ','.join(map(str, user.liked_users))
    disliked_users = ','.join(map(str, user.disliked_users))
    matches = ','.join(map(str, user.matches))

    cursor.execute('''
        INSERT INTO users (user_id, name, age, gender, location, interests, liked_users, disliked_users, matches)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (user.user_id, user.name, user.age, user.gender, user.location,
          ','.join(user.interests), liked_users, disliked_users, matches))

    conn.commit()
    conn.close()


def delete_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # First, update other users' liked_users, disliked_users, and matches lists to remove this user
    cursor.execute('SELECT * FROM users')
    all_users = cursor.fetchall()

    for user_data in all_users:
        current_user_id, name, age, gender, location, interests, liked_users, disliked_users, matches = user_data

        liked_users_list = list(map(int, liked_users.split(','))) if liked_users else []
        disliked_users_list = list(map(int, disliked_users.split(','))) if disliked_users else []
        matches_list = list(map(int, matches.split(','))) if matches else []

        if user_id in liked_users_list:
            liked_users_list.remove(user_id)
        if user_id in disliked_users_list:
            disliked_users_list.remove(user_id)
        if user_id in matches_list:
            matches_list.remove(user_id)

        # Update the current user with the modified lists
        liked_users = ','.join(map(str, liked_users_list))
        disliked_users = ','.join(map(str, disliked_users_list))
        matches = ','.join(map(str, matches_list))

        cursor.execute('''
            UPDATE users
            SET liked_users = ?, disliked_users = ?, matches = ?
            WHERE user_id = ?
        ''', (liked_users, disliked_users, matches, current_user_id))

    # Now delete the user from the database
    cursor.execute('DELETE FROM users WHERE user_id = ?', (user_id,))

    conn.commit()
    conn.close()


def update_user(user):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    liked_users = ','.join(map(str, user.liked_users))
    disliked_users = ','.join(map(str, user.disliked_users))
    matches = ','.join(map(str, user.matches))

    cursor.execute('''
        UPDATE users
        SET liked_users = ?, disliked_users = ?, matches = ?
        WHERE user_id = ?
    ''', (liked_users, disliked_users, matches, user.user_id))

    conn.commit()
    conn.close()


def fetch_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user_data = cursor.fetchone()

    conn.close()

    if user_data:
        user_id, name, age, gender, location, interests, liked_users, disliked_users, matches = user_data

        # Convert comma-separated strings back to lists
        interests = interests.split(',')
        liked_users = list(map(int, liked_users.split(','))) if liked_users else []
        disliked_users = list(map(int, disliked_users.split(','))) if disliked_users else []
        matches = list(map(int, matches.split(','))) if matches else []

        return User(user_id, name, age, gender, location, interests, liked_users, disliked_users, matches)
    else:
        return None  # User not found


# Assuming the User class is already defined as provided.
# Load All Users into a Pandas DataFrame
def fetch_all_users():
    conn = sqlite3.connect('users.db')
    df = pd.read_sql_query("SELECT * FROM users", conn)

    # Convert each comma-separated string in the 'interests' column to a list of interests
    df['interests'] = df['interests'].apply(
        lambda x: x.split(',') if x else [])
    # lambda x:        -> Defines an anonymous function with 'x' as the input (each element in the 'interests' column)
    # x.split(',')     -> Splits the string 'x' by commas into a list (e.g., "hiking,reading" becomes ['hiking', 'reading'])
    # if x             -> Checks if 'x' is not empty or None. If 'x' has content, split it by commas.
    # else []          -> If 'x' is empty or None, return an empty list instead of trying to split 'x'

    conn.close()
    return df


# Compute Compatibility Scores
def compute_compatibility_scores(logged_in_user, users_df):
    # Exclude the logged-in user from potential matches
    potential_matches = users_df[users_df['user_id'] != logged_in_user.user_id].copy()
    # Calculate location compatibility score using a boolean mask and convert to float
    potential_matches['location_score'] = (potential_matches['location'] == logged_in_user.location).astype(float)

    # more creative: use Geo-location (so convert address to GPS point)
    def get_coordinate(city):
        geolocator = Nominatim(user_agent="your_app_name")
        try:
            location1 = geolocator.geocode(city)
            if location1:
                #print(f"City: {location1.address}, Coordinates: {location1.latitude}, {location1.longitude}")
                return location1.latitude, location1.longitude
            else:
                print("Location not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    logged_in_user_cor = get_coordinate(logged_in_user.location)
    potential_matches['new location score'] = [1 / (1 + geodesic(logged_in_user_cor, get_coordinate(city)).kilometers) for city in potential_matches['location']]
    print(potential_matches['new location score'])

    # Calculate age difference score using NumPy's vectorized operations
    potential_matches['age_diff_score'] = 1 / (1 + np.abs(potential_matches['age'] - logged_in_user.age))

    # Convert interests lists into a set for the logged-in user for faster comparison
    logged_in_interests_set = set(logged_in_user.interests)

    # Optimize shared interests score calculation using list comprehension and apply
    def calculate_jaccard_similarity_vectorized(interests):
        # Convert list to set for potential matches
        interests_set = set(interests)
        # Calculate intersection and union sizes directly
        intersection_size = len(logged_in_interests_set & interests_set)
        union_size = len(logged_in_interests_set | interests_set)
        # Return the Jaccard similarity score
        return intersection_size / union_size if union_size > 0 else 0

    # Apply the vectorized Jaccard similarity calculation to all potential matches
    potential_matches['interests_score'] = potential_matches['interests'].apply(calculate_jaccard_similarity_vectorized)

    # Combine the individual scores into a final compatibility score using NumPy's vectorized operations
    potential_matches['compatibility_score'] = (
            0.4 * potential_matches['location_score'] +
            0.3 * potential_matches['age_diff_score'] +
            0.3 * potential_matches['interests_score']
    )

    # Sort by the compatibility score in descending order
    potential_matches = potential_matches.sort_values(by='compatibility_score', ascending=False)

    return potential_matches


# Rank the Potential Matches and Display the Top 5
def display_top_matches(potential_matches, top_n=5):
    top_matches = potential_matches[['user_id', 'name', 'location', 'age', 'compatibility_score']].head(top_n)
    print("Top Matches:")
    print(top_matches)
    return top_matches


# Select and Like a Match
def select_and_like_match(logged_in_user, selected_match_id):
    # Fetch the selected match as a User object
    print(selected_match_id)
    selected_user = fetch_user(selected_match_id)
    print(selected_user)
    # Use the User class's like method
    logged_in_user.like(selected_user)

    # Update both users in the database
    update_user(logged_in_user)
    update_user(selected_user)


# Update and Display the Logged-In User's Profile
def update_and_display_user_profile(logged_in_user):
    # Update the logged-in user's profile in the database
    update_user(logged_in_user)

    # Fetch and display the updated profile
    updated_user = fetch_user(logged_in_user.user_id)
    print("Updated User Profile:")
    print(vars(updated_user))


# Example Scenario
def scenario1():

    setup_database()

    # Create users
    user1 = User(1, "Alice", 25, "Female", "New York", ["hiking", "reading"])
    user2 = User(2, "Bob", 27, "Male", "New York", ["reading", "movies"])
    user3 = User(3, "Charlie", 30, "Male", "Boston", ["hiking", "gaming"])

    # Insert users into the database
    insert_user(user1)
    insert_user(user2)
    insert_user(user3)

    # Step 1: Fetch the logged-in user
    logged_in_user = fetch_user(1)  # Assume user_id=1, Alice, is the logged-in user
    print('Variables of the logged in user: ', vars(logged_in_user))

    # Step 2: Load all users into a DataFrame
    all_users_df = fetch_all_users()
    print('head of df:')
    print(all_users_df.head(3))
    # Step 3: Compute and rank top matches based on compatibility score
    potential_matches = compute_compatibility_scores(logged_in_user, all_users_df)

    # Step 4: Display the top 5 matches
    top_matches = display_top_matches(potential_matches)

    # Step 5: Select and like a match
    selected_match_id = int(top_matches.iloc[0]['user_id'])  # Assume the user selects the top match
    print('selected_match_id', selected_match_id)
    select_and_like_match(logged_in_user, selected_match_id)

    # Step 6: Update and display the logged-in user's profile
    update_and_display_user_profile(logged_in_user)

# Run the example scenario
scenario1()