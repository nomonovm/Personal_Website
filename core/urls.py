from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from main.views import (
    AboutDetailView,

    SkillListView, SkillCreateView, SkillDetailView,
    EducationListView, EducationCreateView, EducationDetailView,
    ExperienceListView, ExperienceCreateView, ExperienceDetailView,
    WorkListView, WorkCreateView, WorkDetailView,

    BlogArticleListView, BlogArticleCreateView, BlogArticleDetailView,
    BlogImageUploadView,

    ContactInfoView,
    ContactMessageCreateView,
)

from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="Personal Website API",
        default_version='v1',
        description="Shaxsiy Website uchun API",
        contact=openapi.Contact(email="mnomonov707@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # About
    path('api/about/', AboutDetailView.as_view(), name='about'),

    # Skills
    path('api/skills/', SkillListView.as_view(), name='skill-list'),
    path('api/skills/create/', SkillCreateView.as_view(), name='skill-create'),
    path('api/skills/<int:pk>/', SkillDetailView.as_view(), name='skill-detail'),

    # Education
    path('api/education/', EducationListView.as_view(), name='education-list'),
    path('api/education/create/', EducationCreateView.as_view(), name='education-create'),
    path('api/education/<int:pk>/', EducationDetailView.as_view(), name='education-detail'),

    # Experience
    path('api/experience/', ExperienceListView.as_view(), name='experience-list'),
    path('api/experience/create/', ExperienceCreateView.as_view(), name='experience-create'),
    path('api/experience/<int:pk>/', ExperienceDetailView.as_view(), name='experience-detail'),

    # My Works
    path('api/works/', WorkListView.as_view(), name='work-list'),
    path('api/works/create/', WorkCreateView.as_view(), name='work-create'),
    path('api/works/<int:pk>/', WorkDetailView.as_view(), name='work-detail'),

    # Blog
    path('api/blog/', BlogArticleListView.as_view(), name='blog-list'),
    path('api/blog/create/', BlogArticleCreateView.as_view(), name='blog-create'),
    path('api/blog/<slug:slug>/', BlogArticleDetailView.as_view(), name='blog-detail'),
    path('api/blog/upload-image/', BlogImageUploadView.as_view(), name='blog-image-upload'),

    # Contact
    path('api/contact/info/', ContactInfoView.as_view(), name='contact-info'),
    path('api/contact/message/', ContactMessageCreateView.as_view(), name='contact-message'),

    # Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
