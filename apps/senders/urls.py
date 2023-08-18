from rest_framework.routers import DefaultRouter

from .apis import SenderCRUDApi

router = DefaultRouter()
router.register("", SenderCRUDApi, "senders")

urlpatterns = router.urls + []
