from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings

import os
from collections import defaultdict
import glob

from . import utils

def index(request):
    ROOT = os.path.join(settings.BASE_DIR, "docs", "*", "*.y*ml")
    context = defaultdict(list)
    for path in glob.glob(ROOT):
        project = os.path.basename(os.path.dirname(path))
        filename = os.path.basename(path)
        info = utils.get_info(path)
        info["filename"] = filename
        context[project].append(info)
    return render(request, 'hub/home.html', context={"context" : dict(context)})


class SwaggerUIView(TemplateView):
    template_name = 'hub/swagger.html'

    def get(self, request, *args, **kwargs):
        project = request.GET.get('project')
        filename = request.GET.get('filename')
        fullpath = f"/docs/{project}/{filename}"
        return self.render_to_response({'url': fullpath})