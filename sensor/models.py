from django.db import models


class Sensor(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    time_interval = models.FloatField()
    distance = models.FloatField()

    def __str__(self):
        return (
            str(self.distance)
            + "from "
            + str(self.start_time)
            + " to "
            + str(self.end_time)
            + " in "
            + str(self.time_interval)
            + " seconds"
        )
