## Image Tagger
This is an image tagger that can tag images from all around the web.

### Training
The model is trained from images from Instagram, Google and OpenImages. 
 - To begin, place images inside the data folder. Images of each category must be placed inside its respective folder (category = folder name)
 - Next run the final model, which will train an image tagger and store the final result.

### Testing
The model comes with a web interface that can tag images on the fly.
 - Run the backend server (`python img/server.py`)
 - RUn the frontend
 `cd img/image-tagger`
 `ng serve`