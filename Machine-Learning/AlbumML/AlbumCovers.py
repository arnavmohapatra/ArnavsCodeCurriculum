#Retrieve 250x250 images of selected album covers

#Currently selected Albums:
#0 - Igor - Tyler, The Creator [4603cee3-ece6-435c-b0b7-7d9eb1842d36] 
#1 - CALL ME IF YOU GET LOST - Tyler, The Creator [0d8d50e3-6899-4bad-8780-3713f2b87e10]
#2 - Flower Boy - Tyler, The Creator [dd09e440-879d-447b-9dfa-8547b369548e] 
#3 - Ginger - BROCKHAMPTON [09aff2d8-a861-49e4-b502-eedd05ed5fe2]
#4 - SATURATION III - BROCKHAMPTON [090f442c-ae2c-4eb7-9178-51b11e4f7deb]
#5 - BALLADS 1 - Joji [cc1da3fc-19c9-4691-aeb9-fe45dc260ffb]
#6 - Nectar - Joji [92abd49f-0a1a-46dc-a1f8-65593b9e7123]
#7 - CTV3: Cool Tape, Vol. 3 - Jaden [7808b847-432b-48e9-b4c1-9271955ef1e3]


import musicbrainzngs as mb
import os
import numpy as np
from PIL import Image, ImageEnhance

def load_data():
        
    mb.set_useragent("AlbumML", "0.1", "https://github.com/Rocket720/ArnavsCodeCurriculum/tree/master/Machine%20Learning/AlbumNN")

    selected_albums = {"4603cee3-ece6-435c-b0b7-7d9eb1842d36": "Igor - Tyler, The Creator", 
                    "0d8d50e3-6899-4bad-8780-3713f2b87e10": "CALL ME IF YOU GET LOST - Tyler, The Creator", 
                    "dd09e440-879d-447b-9dfa-8547b369548e": "Flower Boy - Tyler, The Creator", 
                    "09aff2d8-a861-49e4-b502-eedd05ed5fe2": "Ginger - BROCKHAMPTON",
                    "090f442c-ae2c-4eb7-9178-51b11e4f7deb": "SATURATION III - BROCKHAMPTON",
                    "cc1da3fc-19c9-4691-aeb9-fe45dc260ffb": "BALLADS 1 - Joji",
                    "92abd49f-0a1a-46dc-a1f8-65593b9e7123": "Nectar - Joji",
                    "7808b847-432b-48e9-b4c1-9271955ef1e3": "CTV3: Cool Tape, Vol. 3 - Jaden"
    }

    class_names = {i:selected_albums[id] for i, id in enumerate(selected_albums)}

    # train_test_split = 0.8
    images, labels = [], []
    for index, album_id in enumerate(selected_albums):

        if not os.path.exists("dataset/album_" + str(index) + ".jpeg"):
            tmp = mb.get_image_front(album_id, size = "250")
            with open(os.path.join("dataset/album_" + str(index) + ".jpeg"), 'wb') as f:
                f.write(tmp)
            
        images.append(np.asarray(Image.open("dataset/album_" + str(index) + ".jpeg")))
        labels.append(index)
        

    #Applying Visual/Color Transformations to generate more data

    for image, index in zip(images, class_names):
        image = Image.fromarray(image)
        transformed = []
        
        filter = ImageEnhance.Color(image)
        transformed.append(np.asarray(filter.enhance(0.8)))
        transformed.append(np.asarray(filter.enhance(1.2)))
        
        filter = ImageEnhance.Contrast(image)
        transformed.append(np.asarray(filter.enhance(0.8)))
        transformed.append(np.asarray(filter.enhance(1.2)))
        
        filter = ImageEnhance.Brightness(image)
        transformed.append(np.asarray(filter.enhance(0.8)))
        transformed.append(np.asarray(filter.enhance(1.2)))
        
        filter = ImageEnhance.Sharpness(image)
        transformed.append(np.asarray(filter.enhance(0.8)))
        transformed.append(np.asarray(filter.enhance(1.2)))
        
        images+=transformed
        labels+=[index for _ in range(8)]

    images = np.array(images)
    labels = np.array(labels)

    p = np.random.permutation(len(images))
    images, labels = images[p], labels[p]
    
    return images, labels, class_names