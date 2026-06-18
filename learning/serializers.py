from rest_framework import serializers
from .models import Score


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['id', 'category', 'score', 'total', 'percentage', 'created_at']
        read_only_fields = ['id', 'percentage', 'created_at']

    def create(self, validated_data):
        score = validated_data['score']
        total = validated_data['total']
        validated_data['percentage'] = round((score / total) * 100)
        return super().create(validated_data)