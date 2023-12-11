
from django.db import models

class TelegramUser(models.Model):

    class Meta:
        db_table = 'telegram_acaunt'
        verbose_name = 'telegram_acaunt'
        verbose_name_plural = 'telegram_acaunts'

    stile_for_gbt = (('test0','test0'), ('test1','test1'))

    image = models.ImageField(upload_to="icon_telegram/",blank=False, null=False, verbose_name='image')
    password_2fa = models.TextField(blank=True, null=True)
    get_code = models.TextField(blank=True, null=True)
    name = models.TextField(max_length=30, blank=False, null=False, verbose_name='name')
    familia = models.TextField(max_length=40, blank=True, null=True, verbose_name='familia')
    bio = models.TextField(blank=False, null=False, verbose_name='bio')
    phone = models.TextField(verbose_name='telefoh')
    api_id = models.TextField()
    api_hash = models.TextField()




    def __str__(self):
        return self.name


class Potoci(models.Model):

    class Meta:
        db_table = 'Potoci'
        verbose_name = 'potoci'
        verbose_name_plural = 'potocis'

    stile_for_gbt = (('test0','test0'), ('test1','test1'), ('text_zagatovga', 'text_zagatovga'), ('spintaxst', 'spintaxst'))

    title = models.TextField(blank=False, null=False, verbose_name='zagolovok')
    text = models.TextField(blank=True, null=True, verbose_name='promt')
    user = models.ManyToManyField(TelegramUser, verbose_name='users')
    paragraf_for_chat = models.TextField(blank=True, null=True, choices=stile_for_gbt)
    time_stop = models.FloatField()



    def __str__(self):
        return self.title

class Channel(models.Model):
    class Meta:
        db_table = 'kanal'
        verbose_name = 'kanali'
        verbose_name_plural = 'kanali'

    boti = models.ForeignKey(TelegramUser, models.RESTRICT)
    name_chanel = models.TextField(blank=True, null=True)
    link_for_cahal = models.TextField()
    setings = models.TextField(default='get_channel')

    def process_links(self):
        output_list = []
        parts = self.link_for_cahal.split(',')
        for part in parts:
            output_list.append(part.strip())
        return output_list

    def __str__(self):
       return self.name_chanel
    






class Api_tocken(models.Model):
    class Meta:
        db_table = 'api_tocken'

    api_key = models.TextField()


#######  for database mariadb  ########
#ALTER DATABASE test CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci
#ALTER TABLE test.kanal CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci
