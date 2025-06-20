from rest_framework import serializers
from .models import SpyCat, Mission, Target
import requests


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = '__all__'
        read_only_fields = ('mission',)

    def update(self, instance, validated_data):
        new_notes = validated_data.get('notes', instance.notes)
        if (instance.is_completed or instance.mission.is_completed) and new_notes != instance.notes:
            raise serializers.ValidationError("Cannot update notes if target or mission is completed")
        return super().update(instance, validated_data)


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        fields = ['id', 'cat', 'is_completed', 'targets']

    def create(self, validated_data):
        targets_data = validated_data.pop('targets')
        mission = Mission.objects.create(**validated_data)
        for target_data in targets_data:
            Target.objects.create(mission=mission, **target_data)
        return mission


class SpyCatSerializer(serializers.ModelSerializer):
    mission = MissionSerializer(read_only=True)

    class Meta:
        model = SpyCat
        fields = '__all__'

    def validate_breed(self, value):
        response = requests.get('https://api.thecatapi.com/v1/breeds')
        if response.status_code == 200:
            breeds = [b['name'].lower() for b in response.json()]
            if value.lower() not in breeds:
                raise serializers.ValidationError("Invalid breed name")
        return value
