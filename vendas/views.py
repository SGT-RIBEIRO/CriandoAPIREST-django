from rest_framework import mixins
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from .models import Produto, Categoria, Avaliacao
from .serializers import ProdutoSerializer, CategoriaSerializer, AvaliacaoSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from .permissions import NotDeleteCategoria


"""
API versão 1
"""


class ProdutosAPIView(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def get_queryset(self):

        if self.kwargs.get('categoria_pk'):
            return self.queryset.filter(categoria_id=self.kwargs.get('categoria_pk'))
        return self.queryset.all()


class ProdutoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def get_object(self):
        if self.kwargs.get('categoria_pk'):
            return get_object_or_404(self.get_queryset(), categoria_id=self.kwargs.get('categoria_pk'), pk=self.kwargs.get('produto_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('produto_pk'))


class CategoriasAPIView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer



class CategoriaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer



class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):

        if self.kwargs.get('produto_pk'):
            return self.queryset.filter(produto_id=self.kwargs.get('produto_pk'))
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('produto_pk'):
            return get_object_or_404(self.get_queryset(), produto_id=self.kwargs.get('produto_pk'), pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))


"""
API versão 2
"""

class ProdutoviewsSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        self.pagination_class.page_size = 1
        avaliacoes = Avaliacao.objects.filter(produto_id=pk)
        page = self.paginate_queryset(avaliacoes)
        if page:

        #produto = self.get_object()
        #serializer = AvaliacaoSerializer(produto.avaliacoes.all(), many=True)
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

'''
class AvaliacaoviewsSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
'''


class AvaliacaoviewsSet(mixins.ListModelMixin,
                        #mixins.Response,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer


class CategoriaviewsSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    #permission_classes = (NotDeleteCategoria, permissions.DjangoModelPermissions)
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    @action(detail=True, methods=['get'])
    def produtos(self, request, pk=None):
        categoria = self.get_object()
        serializer = ProdutoSerializer(categoria.produtos.all(), many=True)

        return Response(serializer.data)




