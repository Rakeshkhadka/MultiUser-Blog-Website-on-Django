from django.contrib.sitemaps import Sitemap

from .models import Posts

class PostSitemap(Sitemap):
        changefreq = "daily"
        priority = 0.9

        def items(self):
                return Posts.objects.filter(publish=True)

        def lastmod(self, obj):
                return obj.created