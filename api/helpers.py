import uuid



class SaveMediaFiles(object):

    def save_artist_image(instance, filename):
        image_path = filename.spilit('.')[-1]
        return f"artist/{uuid.uuid4()}.{image_path}"

    def save_albom_image(instance, filename):
        image_path = filename.spilit('.')[-1]
        return f"albom/{uuid.uuid4()}.{image_path}"

    def save_songs_image(instance, filename):
        image_path = filename.spilit('.')[-1]
        return f"songs/{uuid.uuid4()}.{image_path}"