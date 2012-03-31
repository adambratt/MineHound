from django.shortcuts import redirect
from images.models import Photo
from django.http import Http404

from minehound import settings
import os

# On Mac environments PIL works differently
try:
    from PIL import Image
except ImportError:
    import Image
    

# Loads an image file
def load(request, image_id, **kwargs):
    
    if image_id == "nophoto":
        path = settings.MEDIA_ROOT+'images/full/'+image_id
    else:  
        try:
            p = Photo.objects.get(name=image_id)
            path = p.photo.path
        except:
            raise Http404
    
    if (not 'width' in kwargs) or (not 'height' in kwargs):
        size = 'full'
    else:
        size = kwargs['width']+'x'+kwargs['height']
    
    # get size dir/check if image exists
    sizedir=settings.MEDIA_ROOT+'images/'+size+'/'
    
    if os.path.isfile(sizedir+image_id):
        return redirect(settings.MEDIA_URL+'images/'+size+'/'+image_id)
    elif size == 'full':
        return Http404 # Must not exist
    
    # make image dir
    if not os.path.exists(sizedir):
        os.makedirs(sizedir)
        
    # open up the image
    img=Image.open(path)
    if img.mode not in ('L','RGB'):
            img=img.convert('RGB')
    img=img.resize((int(kwargs['width']), int(kwargs['height'])), Image.ANTIALIAS)
    img.save(sizedir+image_id,'PNG')
    
    return redirect(settings.MEDIA_URL+'images/'+size+'/'+image_id)
