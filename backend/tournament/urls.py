from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("api/tournament", views.TournamentViewSet, basename="tournament")
router.register("api/city", views.CityViewSet, basename="city")
router.register("api/sport", views.SportViewSet, basename="sport")
router.register("api/level", views.LevelViewSet, basename="level")
urlpatterns = router.urls
