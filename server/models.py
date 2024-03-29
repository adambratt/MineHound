from django.db import models
from django.contrib.auth.models import User
from django.db import connection
import datetime

class user(models.Model):
    ''' A Minecraft user '''
    username = models.CharField(max_length=50)

class server(models.Model):
    ''' A Minecraft server '''
    name = models.CharField(max_length=50)
    banner = models.ImageField(upload_to='/banner/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=100)
    website = models.CharField(max_length=100, blank=True, null=True)
    server_port = models.IntegerField(default=25565)
    query_port = models.IntegerField(default=25566)
    last_checked = models.DateTimeField()
    status = models.IntegerField(max_length=1, default=0)
    slots = models.IntegerField(default=0)
    owner = models.ForeignKey(User)
    uptime = models.DecimalField(max_digits=5, decimal_places=2)
    
    def hourly_sessions(self):
        cursor = connection.cursor()
        cursor.execute("SELECT DAY(`day`) as `day`, `hour`, `cnt` AS `users` FROM `server_hourlystats` where `server_id` = %s ORDER BY `id` desc LIMIT 24", [self.pk])
        user_list = dictfetchall(cursor)
        user_list.reverse()
        return user_list
        
    property(hourly_sessions)
    
    def daily_visitor_type(self):
        cursor = connection.cursor()
        cursor.execute("select new_users as `new`, returning_users as `returning` from server_visitors WHERE `day` = DATE(NOW() - INTERVAL 2 HOUR) and `server_id` = %s", [self.pk])
        return dictfetchall(cursor)
    
    def total_sessions(self):
        return session.objects.filter(server=self).count()
        
    def today_sessions(self):
        return session.objects.filter(server=self, last_update__gte=datetime.date.today()).count()
    
    property(total_sessions)
    property(today_sessions)
    
    def total_players(self):
        return session.objects.filter(server=self).values('user').distinct().count()
    
    def today_players(self):
        return session.objects.filter(server=self, last_update__gte=datetime.date.today()).values('user').distinct().count()
        
    property(today_players)
    property(total_players)
    
    def get_online_players(self):
        active_sessions = session.objects.filter(end__isnull=True, server=self)
        players = [ ]
        for p in active_sessions:
            players.append(p.user)
        return players
    
    def online_count(self):
        return session.objects.filter(end__isnull=True, server=self).count()
        
    def downtime(self):
        return (100-self.uptime)
    
    online_players = property(get_online_players)
    

class session(models.Model):
    ''' Individual sessions for minecraft users'''
    user = models.ForeignKey('server.user')
    server = models.ForeignKey('server.server')
    length = models.IntegerField(default=0)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(auto_now=True, null=True)
    last_update = models.DateTimeField()
    
def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]