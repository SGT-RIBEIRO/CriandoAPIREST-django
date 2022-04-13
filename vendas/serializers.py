from rest_framework import serializers
from .models import Categoria, Produto, Avaliacao



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


class ProdutoSerializer(serializers.ModelSerializer):
    #Nested Relationsship
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    #Hyperlinked Related Field
    avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    #Primary key Related Field
    #avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

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
            'avaliacoes',
        )


class CategoriaSerializer(serializers.ModelSerializer):

    # Nested Relationsship
    #produtos = ProdutoSerializer(many=True, read_only=True)

    # Hyperlinked Related Field
    produtos = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='produto-detail')

    # Primary key Related Field
    # produtos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:

        model = Categoria
        fields = (
            'id',
            'descricao',
            'criacao',
            'atualizacao',
            'ativo',
            'produtos'
        )

