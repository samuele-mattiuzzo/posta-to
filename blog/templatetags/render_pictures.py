from django import template
from google.appengine.api import images

register = template.Library()

@register.simple_tag
def get_resized_image(image, size):
	blob_key = str(image.blobstore_info.key()) 
	thumbnail_picture_url = images.get_serving_url(blob_key, size)
	return thumbnail_picture_url
