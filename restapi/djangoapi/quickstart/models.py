from django.db import models

# Create your models here.


class Companies(models.Model):
    id = models.IntegerField(blank=True, null=True)
    attr1 = models.TextField(db_column='Attr1', blank=True, null=True)
    attr2 = models.TextField(db_column='Attr2', blank=True, null=True)
    attr3 = models.TextField(db_column='Attr3', blank=True, null=True)
    attr4 = models.TextField(db_column='Attr4', blank=True, null=True)
    attr5 = models.TextField(db_column='Attr5', blank=True, null=True)
    attr6 = models.TextField(db_column='Attr6', blank=True, null=True)
    attr7 = models.TextField(db_column='Attr7', blank=True, null=True)
    attr8 = models.TextField(db_column='Attr8', blank=True, null=True)
    attr9 = models.TextField(db_column='Attr9', blank=True, null=True)
    attr10 = models.TextField(db_column='Attr10', blank=True, null=True)
    attr11 = models.TextField(db_column='Attr11', blank=True, null=True)
    attr12 = models.TextField(db_column='Attr12', blank=True, null=True)
    attr13 = models.FloatField(db_column='Attr13', blank=True, null=True)
    attr14 = models.TextField(db_column='Attr14', blank=True, null=True)
    attr15 = models.TextField(db_column='Attr15', blank=True, null=True)
    attr16 = models.TextField(db_column='Attr16', blank=True, null=True)
    attr17 = models.TextField(db_column='Attr17', blank=True, null=True)
    attr18 = models.TextField(db_column='Attr18', blank=True, null=True)
    attr19 = models.FloatField(db_column='Attr19', blank=True, null=True)
    attr20 = models.FloatField(db_column='Attr20', blank=True, null=True)
    attr21 = models.TextField(db_column='Attr21', blank=True, null=True)
    attr22 = models.TextField(db_column='Attr22', blank=True, null=True)
    attr23 = models.FloatField(db_column='Attr23', blank=True, null=True)
    attr24 = models.TextField(db_column='Attr24', blank=True, null=True)
    attr25 = models.TextField(db_column='Attr25', blank=True, null=True)
    attr26 = models.TextField(db_column='Attr26', blank=True, null=True)
    attr27 = models.TextField(db_column='Attr27', blank=True, null=True)
    attr28 = models.TextField(db_column='Attr28', blank=True, null=True)
    attr29 = models.TextField(db_column='Attr29', blank=True, null=True)
    attr30 = models.FloatField(db_column='Attr30', blank=True, null=True)
    attr31 = models.FloatField(db_column='Attr31', blank=True, null=True)
    attr32 = models.TextField(db_column='Attr32', blank=True, null=True)
    attr33 = models.TextField(db_column='Attr33', blank=True, null=True)
    attr34 = models.TextField(db_column='Attr34', blank=True, null=True)
    attr35 = models.TextField(db_column='Attr35', blank=True, null=True)
    attr36 = models.TextField(db_column='Attr36', blank=True, null=True)
    attr37 = models.TextField(db_column='Attr37', blank=True, null=True)
    attr38 = models.TextField(db_column='Attr38', blank=True, null=True)
    attr39 = models.FloatField(db_column='Attr39', blank=True, null=True)
    attr40 = models.TextField(db_column='Attr40', blank=True, null=True)
    attr41 = models.TextField(db_column='Attr41', blank=True, null=True)
    attr42 = models.FloatField(db_column='Attr42', blank=True, null=True)
    attr43 = models.FloatField(db_column='Attr43', blank=True, null=True)
    attr44 = models.FloatField(db_column='Attr44', blank=True, null=True)
    attr45 = models.TextField(db_column='Attr45', blank=True, null=True)
    attr46 = models.TextField(db_column='Attr46', blank=True, null=True)
    attr47 = models.TextField(db_column='Attr47', blank=True, null=True)
    attr48 = models.TextField(db_column='Attr48', blank=True, null=True)
    attr49 = models.FloatField(db_column='Attr49', blank=True, null=True)
    attr50 = models.TextField(db_column='Attr50', blank=True, null=True)
    attr51 = models.TextField(db_column='Attr51', blank=True, null=True)
    attr52 = models.TextField(db_column='Attr52', blank=True, null=True)
    attr53 = models.TextField(db_column='Attr53', blank=True, null=True)
    attr54 = models.TextField(db_column='Attr54', blank=True, null=True)
    attr55 = models.FloatField(db_column='Attr55', blank=True, null=True)
    attr56 = models.FloatField(db_column='Attr56', blank=True, null=True)
    attr57 = models.TextField(db_column='Attr57', blank=True, null=True)
    attr58 = models.FloatField(db_column='Attr58', blank=True, null=True)
    attr59 = models.TextField(db_column='Attr59', blank=True, null=True)
    attr60 = models.TextField(db_column='Attr60', blank=True, null=True)
    attr61 = models.TextField(db_column='Attr61', blank=True, null=True)
    attr62 = models.FloatField(db_column='Attr62', blank=True, null=True)
    attr63 = models.TextField(db_column='Attr63', blank=True, null=True)
    attr64 = models.TextField(db_column='Attr64', blank=True, null=True)
    class_field = models.IntegerField(db_column='class', blank=True, null=True)

    class Meta:
        db_table = 'Companies'
