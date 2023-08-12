from rest_framework.routers import DefaultRouter

from .apis import PhoneCRUDApi, PhoneGroupCRUDApi

router = DefaultRouter()
router.register("phones", PhoneCRUDApi, "phones")
router.register("phone-groups", PhoneGroupCRUDApi, "phone-groups")

urlpatterns = router.urls + []
