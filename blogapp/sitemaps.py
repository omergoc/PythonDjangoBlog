from django.contrib.sitemaps import Sitemap
from articles.helpers import articles_list
 
 
class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return articles_list("All")

    def lastmod(self, obj):
        return obj['created_date']
        
    def location(self,obj):
        return '/%s/%s' % (obj['category_slug'],obj['slug'])