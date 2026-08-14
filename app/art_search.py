import requests
import random

ART_LIST_URL = "https://collectionapi.metmuseum.org/public/collection/v1/search"
ART_OBJECT_URL = "https://collectionapi.metmuseum.org/public/collection/v1/objects"

def find_art(search_word):
    # searches the Met for art matching the search word, and returns a list of 10 random art pieces corresponding to the search word
    # only search ids for pieces that are on view and have an image (parameters)
    request_url = f"{ART_LIST_URL}?q={search_word}&hasImages=true&isOnView=true"

    response = requests.get(request_url)
    data = response.json()

    object_ids = data["objectIDs"]

    random.shuffle(object_ids)
    object_ids = object_ids[:10]  # limit to first 10 results

    if object_ids == None:
        return []
    
    print(object_ids)
    return object_ids


def get_object_details(object_id):
    # a function that can retrieve the details of a specific art object from the Met API, given its object ID
    # art specific detail is stored in a different table
    request_url = f"{ART_OBJECT_URL}/{object_id}"

    response = requests.get(request_url)
    data = response.json()
    # print(data)

    return data


def get_random_art_list(search_word):
    # gets details for my list of 10 object ids and returns the title, artist name, and an image
    object_ids = find_art(search_word)
    # gets my list of object ids

    results = []
    # create empty list to store my result list of art pieces

    # for each object id in my list of 10, get the details 
    for object_id in object_ids:
        details = get_object_details(object_id)
        art_summary = {
            "name": details["title"],
            "artist": details["artistDisplayName"],
            "photo": details["primaryImage"]
        }
        results.append(art_summary)

    return results


if __name__ == "__main__":
    # ONLY RUN THE CODE BELOW
    # IF WE ARE RUNNING THIS SCRIPT FROM THE COMMAND LINE
    # BUT NOT IF WE'RE TRYING TO JUST IMPORT SOME STUFF FROM THIS FILE

    print("MET ART SEARCH")
    search_word = input("What do you want to search for? ")

    art_list = get_random_art_list(search_word)

    if len(art_list) == 0:
        print("No on-view art with images found for that word, try something else.")
        quit()

    print(f"\nFOUND {len(art_list)} PIECES:\n")
    for art in art_list:
        print(art["name"])
        print(f"  Artist: {art['artist']}")
        print(f"  Photo: {art['photo']}")
        print()