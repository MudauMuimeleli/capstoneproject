"""Mock API Exercise: Music Album

1. Create an "Album" resource on mockapi.io (fields: id, name, rate).
2. Paste its URL into API_ENDPOINT below.
3. Study the finished GET section.
4. Complete the POST, PUT, and DELETE sections.
"""

import requests

# TODO (SETUP): Replace this placeholder with your own mockapi.io resource URL.
# Example: "https://<your-project-id>.mockapi.io/album"
API_ENDPOINT = "https://<your-project-id>.mockapi.io/album"


# ============================================================
# 1. GET METHOD (worked example, given to you)
# ============================================================
try:
    response = requests.get(API_ENDPOINT)
    response.raise_for_status()
    print("Status Code: ", response.status_code)

    # Safe handling in case the mock API has no records yet.
    if response.text.strip():
        albums = response.json()
    else:
        albums = []

    print("Album Songs: ", albums)
    print("\n")

    print("*************** Print 1 song *****************************")
    single_response = requests.get(API_ENDPOINT + "/1")
    print("Status Code: ", single_response.status_code)

    if single_response.status_code == 200 and single_response.text.strip():
        song_name = single_response.json().get("name", "No name")
        song_rating = single_response.json().get("rate", "0")
    else:
        song_name = "No songs exist yet"
        song_rating = "0"

    print("Get one song: ", song_name)
    print("\n")
    print("Get rating: ", song_rating)

except requests.exceptions.RequestException as error:
    print("HTTP GET ERROR: ", error)


# ============================================================
# 2. POST METHOD
# ============================================================
print("\n")
print("--- CREATING A NEW SONG ---")
try:
    new_song = {
        "id": "4",
        "name": "Sondela",
        "rate": "9"
    }

    response_of_new_song = requests.post(API_ENDPOINT, json=new_song)
    print("Status Code: ", response_of_new_song.status_code)
    response_of_new_song.raise_for_status()

    if response_of_new_song.text.strip():
        print(response_of_new_song.json())

except requests.exceptions.RequestException as error:
    print("HTTP POST ERROR: ", error)


# ============================================================
# 3. PUT METHOD
# ============================================================
print("\n")
print("--- REPLACING A SONG ---")
try:
    updated_song = {
        "id": "2",
        "name": "Sondela Remix",
        "rate": "10"
    }

    # Update an existing item by its ID.
    response_of_replacement = requests.put(API_ENDPOINT + "/2", json=updated_song)
    print("Status Code: ", response_of_replacement.status_code)
    response_of_replacement.raise_for_status()

    if response_of_replacement.text.strip():
        print(response_of_replacement.json())

except requests.exceptions.RequestException as error:
    print("HTTP PUT ERROR: ", error)


# ============================================================
# 4. DELETE METHOD
# ============================================================
print("\n")
print("--- DELETING A SONG ---")
try:
    delete_song = requests.delete(API_ENDPOINT + "/4")
    print("Status Code: ", delete_song.status_code)
    delete_song.raise_for_status()

    if delete_song.text.strip():
        print(delete_song.json())

    print("--- Bonus: Verifying deletion errors out as expected ---")
    confirm_check = requests.get(API_ENDPOINT + "/4")
    confirm_check.raise_for_status()

except requests.exceptions.RequestException as error:
    print("HTTP Error (Expected confirmation result): ", error)
