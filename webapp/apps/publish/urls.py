from django.conf.urls import url
from django.urls import path

from .views import (
    ProjectView,
    ProjectDetailView,
    ProjectDetailAPIView,
    ProjectAPIView,
    TagAPIView,
    EmbedApprovalView,
    EmbedApprovalDetailView,
    DeploymentsView,
    DeploymentsDetailView,
    DeploymentsHashidView,
)


urlpatterns = [
    url(r"^$", ProjectView.as_view(), name="publish"),
    path(
        "api/v1/<str:username>/<str:title>/embedapprovals/",
        EmbedApprovalView.as_view(),
        name="embed_approval",
    ),
    path(
        "api/v1/<str:username>/<str:title>/embedapprovals/<str:ea_name>/",
        EmbedApprovalDetailView.as_view(),
        name="embed_approval_detail",
    ),
    path(
        "api/v1/<str:username>/<str:title>/deployments/<str:dep_name>/",
        DeploymentsDetailView.as_view(),
        name="deployments_detail",
    ),
    path(
        "api/v1/<str:username>/<str:title>/detail/",
        ProjectDetailAPIView.as_view(),
        name="project_detail_api",
    ),
    path(
        "api/v1/<str:username>/<str:title>/tags/",
        TagAPIView.as_view(),
        name="project_tags_api",
    ),
    path(
        "api/v1/deployments/<str:hashid>/",
        DeploymentsHashidView.as_view(),
        name="deployments_hashid_view",
    ),
    path("api/v1/deployments/", DeploymentsView.as_view(), name="list_deployments_api"),
    path("api/v1/", ProjectAPIView.as_view(), name="project_create_api"),
]
