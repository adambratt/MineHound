from django.db import models



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
    
    def get_online_players(self):
        active_sessions = session.objects.filter(last_update=self.last_checked)
        players = [ ]
        for p in active_sessions:
            players.append(p.user)
        return players
    
    online_players = property(get_online_players)
    

class session(models.Model):
    ''' Individual sessions for minecraft users'''
    user = models.ForeignKey('server.user')
    server = models.ForeignKey('server.server')
    length = models.IntegerField(default=0)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField()