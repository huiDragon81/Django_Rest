from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, renderer_classes
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from blog.models import Post
from rest_framework.generics import GenericAPIView
from rest_framework import serializers,mixins, schemas, response

# ################################## 요고 해주면 걍 지가 알아서 내 사이트에 있는거 다 뽑아오네 씨발
@api_view()
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='blogs API')
    return response.Response(generator.get_schema(request=request))
# ###################################

def blog_page(request):
    return HttpResponse('hello world' + Post.objects.all()[0].title);


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post

class blog_api(GenericAPIView, mixins.ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args,**kwargs)
