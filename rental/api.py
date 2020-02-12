from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin

from core import views as core_views


class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass


router = NestedDefaultRouter()
friends = router.register("friends", core_views.FriendViewset)
friends.register(
    "borrowings",
    core_views.BelongingViewset,
    basename="friend-borrow",
    parents_query_lookups=["to_who"],
)
router.register(r"belongings", core_views.BelongingViewset)
router.register(r"borrowings", core_views.BorrowedViewset)