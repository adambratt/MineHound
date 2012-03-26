from django.db import models
import datetime



class user(models.Model):
    ''' A Minecraft user '''
    username = models.CharField(max_length=50)

class server(models.Model):
    ''' A Minecraft server '''
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    server_port = models.IntegerField(default=25565)
    query_port = models.IntegerField(default=25566)
    last_checked = models.DateTimeField()
    status = models.IntegerField(max_length=1, default=0)
    
    def total_sessions(self):
        return session.objects.filter(server=self).count()
        
    def today_sessions(self):
        return session.objects.filter(server=self, last_update__gte=datetime.date.today()).count()
    
    property(total_sessions)
    property(today_sessions)
        
    
    def get_online_players(self):
        active_sessions = session.objects.filter(end__isnull=True, server=self)
        players = [ ]
        for p in active_sessions:
            players.append(p.user)
        return players
    
    def online_count(self):
        return session.objects.filter(end__isnull=True, server=self).count()
    
    property(online_count)
    online_players = property(get_online_players)
    

class session(models.Model):
    ''' Individual sessions for minecraft users'''
    user = models.ForeignKey('server.user')
    server = models.ForeignKey('server.server')
    length = models.IntegerField(default=0)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(auto_now=True, null=True)
    last_update = models.DateTimeField()