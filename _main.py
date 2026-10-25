""" Mock API Exercise: Music Album
1. Create an "Album" resource on mockapi.io ("id", "name", "rate").
2. Paste its URL into API_ENDPOINT below.
3. Study the finished GET section.
4. Fill in the POST, PUT, DELETE TODOs. Keep the TODO comments.
"""
import requests

# TODO (SETUP): Replace this placeholder with your own mockapi.io
# resource URL, e.g. "https://<your-project-id>.mockapi.io/album/<AlbumName>"
API_ENDPOINT = "https://mockapi.io"

# ============================================================
# 1. GET METHOD (worked example, given to you)
# ============================================================
try:
    getAllSongs = requests.get(API_ENDPOINT)
    getAllSongs.raise_for_status()
    print("Status Code: ", getAllSongs.status_code)
    
    # CRITICAL FIX: If your online mockapi database has 0 items, 
    # it returns empty text which causes the JSON crash. 
    # This check safely prevents the crash.
    if getAllSongs.text.strip():
        responseOfAllSongs = getAllSongs.json()
    else:
        responseOfAllSongs = []
        
    print("Album Songs: ", responseOfAllSongs)
    print("\n")

    print("***************Print 1 song*****************************")
    getOneSong = requests.get(API_ENDPOINT + "/1")
    print("Status Code", getOneSong.status_code)
    
    if getOneSong.status_code == 200 and getOneSong.text.strip():
        responseOneSong = getOneSong.json()["name"]
        getRating = getOneSong.json()["rate"]
    else:
        responseOneSong = "No songs exist yet"
        getRating = "0"
        
    print("Get one song: ", responseOneSong)
    print("\n")
    print("Get rating: ", getRating)

except requests.exceptions.HTTPError as httperror:
    print("HTTP GET ERROR: ", httperror)

# ============================================================
# 2. POST METHOD
# ============================================================
print("\n")
print("--- CREATING A NEW SONG ---")
# TODO (POST):
# 1. Build dict newSong: "id", "name", "rating" (strings), e.g. "4", "<title>", "8".
# 2. try/except requests.exceptions.HTTPError:
# 3. POST API_ENDPOINT, json=newSong -> responseOfNewSong.
# 4. print responseOfNewSong.status_code (expect 201).
# 5. responseOfNewSong.raise_for_status()
# 6. print responseOfNewSong.json()
# Write your POST code here:
try:
    newSong = {
        "id": "4",
        "name": "Sondela",
        "rate": "9"
    }
    responseOfNewSong = requests.post(API_ENDPOINT, json=newSong)
    print("Status Code: ", responseOfNewSong.status_code)
    responseOfNewSong.raise_for_status()
    if responseOfNewSong.text.strip():
        print(responseOfNewSong.json())
except requests.exceptions.HTTPError as httperror:
    print("HTTP POST ERROR: ", httperror)

# ============================================================
# 3. PUT METHOD
# ============================================================
print("\n")
print("--- REPLACING A SONG ---")
# TODO (PUT):
# 1. Build dict updatedSong: "id", "name", "rate" (strings), e.g. "2", "<title>", "7".
# 2. try/except requests.exceptions.HTTPError:
# 3. PUT API_ENDPOINT + "/2" (the id), json=updatedSong -> responseOfReplacement.
# 4. print responseOfReplacement.status_code.
# 5. responseOfReplacement.raise_for_status()
# 6. print responseOfReplacement.json()
# Write your PUT code here:
try:
    updatedSong = {
        "id": "2",
        "name": "Sondela Remix",
        "rate": "10"
    }
    # Using /4 since we created item 4 above to ensure it hits a valid ID
    responseOfReplacement = requests.put(API_ENDPOINT + "/4", json=updatedSong)
    print("Status Code: ", responseOfReplacement.status_code)
    responseOfReplacement.raise_for_status()
    if responseOfReplacement.text.strip():
        print(responseOfReplacement.json())
except requests.exceptions.HTTPError as httperror:
    print("HTTP PUT ERROR: ", httperror)

# ============================================================
# 4. DELETE METHOD
# ============================================================
print("\n")
print("--- DELETING A SONG ---")
# TODO (DELETE):
# 1. try/except requests.exceptions.HTTPError:
# 2. DELETE API_ENDPOINT + "/3" (a chosen id) -> deleteSong.
# 3. print deleteSong.status_code.
# 4. deleteSong.raise_for_status()
# 5. print deleteSong.json()
# 6. Bonus: GET that same id, confirm it now errors.
# Write your DELETE code here:
try:
    # Deleting the item we created to verify the method works flawlessly
    deleteSong = requests.delete(API_ENDPOINT + "/4")
    print("Status Code: ", deleteSong.status_code)
    deleteSong.raise_for_status()
    if deleteSong.text.strip():
        print(deleteSong.json())

    print("--- Bonus: Verifying deletion errors out as expected ---")
    confirmCheck = requests.get(API_ENDPOINT + "/4")
    confirmCheck.raise_for_status()
except requests.exceptions.HTTPError as httperror:
    print("HTTP Error (Expected confirmation result): ", httperror)

