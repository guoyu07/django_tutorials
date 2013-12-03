from django.db import models

class School(models.Model):
  #sid = models.CharField(max_length=9, primary_key=True)
  real_name = models.CharField(max_length=30)

  def __unicode__(self):
    return u'%s' %(self.real_name)

  class Meta:
    db_table = "schools"