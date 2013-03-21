from django.contrib.sitemaps import Sitemap
from models import Project, Document

class ProjectSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return Project.objects.all()

class DocumentSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return Document.objects.all()