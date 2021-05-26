from api.views import UserViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', UserViewset)

# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrive