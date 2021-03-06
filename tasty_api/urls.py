from my_app.api.resources import MyModelResource
from django.conf.urls import url, include
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(MyModelResource())

urlpatterns = [
  # ...more URLconf bits here...
  # Then add:
  url(r'^api/', include(v1_api.urls)),
]