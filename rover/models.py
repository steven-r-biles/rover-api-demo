from typing import Dict

from django.db import models

class Mission(models.Model):
    name = models.CharField(max_length=100)
    accepted = models.BooleanField(default=False)
    reject_reason = models.CharField(max_length=100, blank=True)

    def is_valid(self):
        commands = self.command_set.all().order_by('sequence_number')
        power = 100 # starting power
        for i, command in enumerate(commands):
            power -= command.power_requirement
            if power <= 0:
                self.reject_reason = f"Insufficient power after command {i + 1}"
                return False
        return True
    
    @classmethod
    def from_json(cls, mission_json: Dict, mission_id: int | None):
        if mission_id:
            mission = cls.objects.get(pk=mission_id)
            mission.name = mission_json.get('name')
            mission.accepted = False
            mission.reject_reason = ''
            mission.save()
            Command.objects.filter(mission=mission).delete()
        else:
            mission = cls.objects.create(name=mission_json.get('name'))
        for i, command in enumerate(mission_json.get('commands')):
            Command.objects.create(
                mission=mission,
                sequence_number=i,
                command=command,
            )
        return mission

    def to_json(self):
        commands = self.command_set.all().order_by('sequence_number')
        data = {
            'id': self.id,
            'name': self.name,
            'accepted': self.accepted,
            'commands': [command.command for command in commands],
        }
        if not self.accepted:
            data['reject_reason'] = self.reject_reason
        return data
    
    def to_csv(self):
        commands = self.command_set.all().order_by('sequence_number')
        return '\n'.join([command.command for command in commands])


class Command(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    sequence_number = models.IntegerField()
    command = models.CharField(max_length=100)

    @property
    def power_requirement(self) -> int:
        if self.command.startswith('forward'):
            return int(self.command.split(' ')[1])
        elif self.command.startswith('right') or self.command.startswith('left'):
            return int(self.command.split(' ')[1]) // 5
        elif self.command.startswith('wait'):
            return 0
        elif self.command.startswith('picture'):
            return 1
        return 0