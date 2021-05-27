from api.views import UserViewset
from api.views import LaporViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', UserViewset)
router.register('lapor', LaporViewset)

# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrive
