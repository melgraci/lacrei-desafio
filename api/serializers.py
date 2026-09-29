from rest_framework import serializers

from .models import Consulta, Profissional


class ProfissionalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profissional
        fields = '__all__'

    def validate(self, data):
        if not data.get('nome_social', '').strip():
            raise serializers.ValidationError(
                'O nome social é obrigatório.'
            )

        if not data.get('profissao', '').strip():
            raise serializers.ValidationError(
                'A profissão é obrigatória.'
            )

        if not data.get('endereco', '').strip():
            raise serializers.ValidationError(
                'O endereço é obrigatório.'
            )

        if not data.get('contato', '').strip():
            raise serializers.ValidationError(
                'O contato é obrigatório.'
            )

        return data


class ConsultaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consulta
        fields = '__all__'

    def validate(self, data):
        if not data.get('data'):
            raise serializers.ValidationError(
                'A data da consulta é obrigatória.'
            )

        if not data.get('profissional'):
            raise serializers.ValidationError(
                'O profissional é obrigatório.'
            )

        return data

    