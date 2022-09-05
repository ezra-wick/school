from django.contrib import admin
from main.models import Block, BlockImage, FeedBack, BotUsers
# Register your models here.


class BlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'position', 'tag')


admin.site.register(Block, BlockAdmin)


class BlockImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'block', 'tag', 'image')
    search_display = ('id', 'block', 'tag')

admin.site.register(BlockImage, BlockImageAdmin)


class FeedBackAdmin(admin.ModelAdmin):
    search_display = ('id', 'name', 'phone')

admin.site.register(FeedBack, FeedBackAdmin)

class BotUsersAdmin(admin.ModelAdmin):
    search_display = ('id', 'username', "userid", "firstname", "lastname")

admin.site.register(BotUsers, BotUsersAdmin)
