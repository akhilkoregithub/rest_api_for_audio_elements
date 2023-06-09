from django.db import models

class AudioElement(models.Model):
    AUDIO_TYPES = [
        ('vo', 'Voice Over'),
        ('bg_music', 'Background Music'),
        ('video_music', 'Video Music'),
    ]

    id = models.CharField(primary_key=True, max_length=255)
    url = models.URLField(null=True, blank=True)
    type = models.CharField(choices=AUDIO_TYPES, max_length=20)
    high_volume = models.IntegerField()
    low_volume = models.IntegerField()
    #video_component_id = models.CharField(max_length=255, null=True, blank=True)
    #url = models.URLField(null=True, blank=True)
    start_time = models.IntegerField(null=True, blank=True)
    end_time = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Adjust start and end times for overlapping elements of the same type
        if self.type != 'video_music':
            existing_elements = AudioElement.objects.filter(type=self.type).exclude(id=self.id)
            for element in existing_elements:
                if self.start_time <= element.end_time and self.end_time >= element.start_time:
                    self.start_time = element.end_time + 1
                    self.end_time = self.start_time + (self.end_time - self.start_time)
        else:
            self.start_time = None
            self.end_time = None

        super().save(*args, **kwargs)
