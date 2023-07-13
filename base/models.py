from django.db import models
import uuid 
#unique identifier,primary alpha numeric key(and a meta (key) so that it treats it as a class not a django model)


class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)#default value of uuid added
    created_at =models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    #so that it doesnt becomes a model
    class Meta:
        abstract = True