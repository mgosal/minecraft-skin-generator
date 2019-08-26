# Show an image picker dialog (allowing multiple selection) and print the result

import photos
assets = photos.pick_asset(title='Pick photo', multi=False)
print(assets)
