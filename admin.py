from django.contrib import admin
from .models import Collection,Piece,Story

class PieceAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'collection')
    list_filter = ('collection',)  # This adds a filter in the admin panel
    search_fields = ('title', 'artist')  # Enables search in admin

admin.site.register(Collection)
admin.site.register(Piece, PieceAdmin)  # Register with the admin class
admin.site.register(Story)
