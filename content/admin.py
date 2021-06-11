from django.contrib import admin
from .models import Cour,Document,Devoir,Exam,Comment,Annonce

# Register your models here.
admin.site.register(Cour)
admin.site.register(Document)
admin.site.register(Devoir)
admin.site.register(Exam)
admin.site.register(Annonce)

admin.site.site_header = 'Said Tkatek '
admin.site.site_title='site de cours  '
admin.site.index_title='site de cours  '