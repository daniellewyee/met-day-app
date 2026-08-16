# this is the "test/test_art_search.py" file...

# todo: test the functionality in the "app/art_search.py" file


from app.art_search import find_art, get_random_art_list


def test_find_art_returns_list():
    # check that a search term returns a list of object ids greater than 0 but less than or equal to 10
    object_ids = find_art("sunflower")
    assert isinstance(object_ids, list)
    assert len(object_ids) > 0
    assert len(object_ids) <= 10

# check a few different words
def test_find_art_returns_list():
    # check that a search term returns a list of object ids greater than 0 but less than or equal to 10
    object_ids = find_art("dog")
    assert isinstance(object_ids, list)
    assert len(object_ids) > 0
    assert len(object_ids) <= 10

def test_find_art_returns_list():
    # check that a search term returns a list of object ids greater than 0 but less than or equal to 10
    object_ids = find_art("bear")
    assert isinstance(object_ids, list)
    assert len(object_ids) > 0
    assert len(object_ids) <= 10

def test_find_art_returns_list():
    # check that a search term returns a list of object ids greater than 0 but less than or equal to 10
    object_ids = find_art("water")
    assert isinstance(object_ids, list)
    assert len(object_ids) > 0
    assert len(object_ids) <= 10

def test_find_art_returns_list():
    # check that a search term returns a list of object ids greater than 0 but less than or equal to 10
    object_ids = find_art("soda")
    assert isinstance(object_ids, list)
    assert len(object_ids) > 0
    assert len(object_ids) <= 10

def test_find_art_returns_list():
    # check that a search term returns a list of object ids greater than 0 but less than or equal to 10
    object_ids = find_art("otter")
    assert isinstance(object_ids, list)
    assert len(object_ids) > 0
    assert len(object_ids) <= 10


def test_find_art_fake_word():
    # check that a fake word should come back as an empty list
    object_ids = find_art("asdkfjhasldkfjhasdlkfjh")
    assert isinstance(object_ids, list)

def test_get_random_art_list():
    # check that a search term returns a list of dictionaries with name, artist, and photo
    art_list = get_random_art_list("sunflower")
    assert len(art_list) > 0
    assert "name" in art_list[0]
    assert "artist" in art_list[0]
    assert "photo" in art_list[0]

# check a few different words
def test_get_random_art_list():
    # check that a search term returns a list of dictionaries with name, artist, and photo
    art_list = get_random_art_list("dog")
    assert len(art_list) > 0
    assert "name" in art_list[0]
    assert "artist" in art_list[0]
    assert "photo" in art_list[0]

def test_get_random_art_list():
    # check that a search term returns a list of dictionaries with name, artist, and photo
    art_list = get_random_art_list("bear")
    assert len(art_list) > 0
    assert "name" in art_list[0]
    assert "artist" in art_list[0]
    assert "photo" in art_list[0]

def test_get_random_art_list():
    # check that a search term returns a list of dictionaries with name, artist, and photo
    art_list = get_random_art_list("water")
    assert len(art_list) > 0
    assert "name" in art_list[0]
    assert "artist" in art_list[0]
    assert "photo" in art_list[0]

def test_get_random_art_list():
    # check that a search term returns a list of dictionaries with name, artist, and photo
    art_list = get_random_art_list("soda")
    assert len(art_list) > 0
    assert "name" in art_list[0]
    assert "artist" in art_list[0]
    assert "photo" in art_list[0]

def test_get_random_art_list():
    # check that a search term returns a list of dictionaries with name, artist, and photo
    art_list = get_random_art_list("otter")
    assert len(art_list) > 0
    assert "name" in art_list[0]
    assert "artist" in art_list[0]
    assert "photo" in art_list[0]