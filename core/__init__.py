import datetime


class SystemInfo:
    def get_time():
        pass

    @staticmethod
    def get_date():
        now = datetime.datetime.now()
        answer = 'São {} Horas {} Minutos {}'.format(
            now.hour, now.minute)
        return answer