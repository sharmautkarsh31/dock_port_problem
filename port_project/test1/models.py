from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Port(models.Model):
    port_no= models.IntegerField()
    no_of_containers=models.IntegerField()

    def __str__(self):
        return str(self.port_no)


class Container(models.Model):
    port= models.ForeignKey(Port, null=True, blank=True, on_delete=models.CASCADE, related_name='container')
    position=models.CharField(null=True, blank=True, max_length=225)

    def __str__(self):
        return str(self.position)