from django.db import models
from django.core.files import File 
import hashlib
import random
import os
import urllib, urlparse


# Utility Functions
def photo_upload_name(instance, filename):
    randomname = hashlib.md5(str(random.randint(0,1000000))).hexdigest()
    fullname = os.path.join("images/full/",randomname)
    try:
        Photo.objects.get(photo=fullname)
        return photo_upload_name(instance,filename)
    except Photo.DoesNotExist:
        return fullname


class Photo(models.Model):
    name=models.CharField(max_length=100,blank=True,unique=True)
    photo=models.ImageField(upload_to=photo_upload_name,blank=False)
    create_ts=models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        super(Photo, self).save(*args, **kwargs) 
        if len(self.name)==0:
            self.name=os.path.basename(self.photo.name)
        super(Photo, self).save(*args, **kwargs)
        
    def grab_url(self, url):
        ''' Store image locally if we have a URL '''
        if url and not self.photo:
            result = urllib.urlretrieve(url)
            self.photo.save( urlparse.urlparse(url).path, File(open(result[0])) )
            self.save()
            
    def grab_facebook_profile(self, username):
        ''' Get the facebook pic from a facebook username '''
        facebook_url = "http://graph.facebook.com/"
        self.grab_url(facebook_url+username+'/picture?type=large')
        
    def _get_file(self):
        ''' Returns the URL to the image '''
        return '/image/%s' % (self.name)
    
    file = property(_get_file)

    
    