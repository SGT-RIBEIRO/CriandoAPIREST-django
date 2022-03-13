from rest_framework import serializers
from .models import Categoria, Produto, Avaliacao


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Categoria
        fields = (
            'id',
            'descricao',
            'criacao',
            'atualizacao',
            'ativo',
        )


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Produto
        fields = (
            'id',
            'nome',
            'preco',
            'categoria',
            'criacao',
            'atualizacao',
            'ativo',
        )


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:

        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'produto',
            'avaliador',
            'email',
            'comentario',
            'nota',
            'criacao',
            'atualizacao',
            'ativo',
        )
