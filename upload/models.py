from __future__ import unicode_literals

from django.db import models

def get_upload_path(instance, filename):
    return 'upload/%d.wav' % instance.file_id

# Create your models here.
class UploadFileModel(models.Model):
    #file = models.FileField(null=True)
    file_id = models.AutoField(primary_key=True)
    #file = models.FileField(null=True, upload_to="upload/%d.amr" % file_id)
    file = models.FileField(upload_to=get_upload_path, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.file_id is None:
            temp_file = self.file
            self.file = None
            super().save(*args, **kwargs)
            self.file = temp_file
        super().save(*args, **kwargs)
            
