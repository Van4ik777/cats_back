from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import SpyCat, Mission, Target
from .serializers import SpyCatSerializer, MissionSerializer, TargetSerializer


class SpyCatViewSet(viewsets.ModelViewSet):
    queryset = SpyCat.objects.select_related('mission').prefetch_related('mission__targets').all()
    serializer_class = SpyCatSerializer


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    @action(detail=True, methods=['post'])
    def assign_cat(self, request, pk=None):
        mission = self.get_object()
        cat_id = request.data.get('cat_id')
        if mission.cat is not None:
            return Response({'error': 'Mission already assigned'}, status=400)
        try:
            cat = SpyCat.objects.get(id=cat_id)
        except SpyCat.DoesNotExist:
            return Response({'error': 'Cat not found'}, status=404)
        mission.cat = cat
        mission.save()
        return Response({'status': 'cat assigned'})

    def destroy(self, request, *args, **kwargs):
        mission = self.get_object()
        if mission.cat is not None:
            return Response({'error': 'Cannot delete mission assigned to a cat'}, status=400)
        return super().destroy(request, *args, **kwargs)


class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_completed or instance.mission.is_completed:
            return Response({'error': 'Target or mission is already completed'}, status=400)
        return super().update(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    def mark_complete(self, request, pk=None):
        target = self.get_object()
        target.is_completed = True
        target.save()
        mission = target.mission
        if mission.targets.filter(is_completed=False).count() == 0:
            mission.is_completed = True
            mission.save()
        return Response({'status': 'target marked as complete'})
