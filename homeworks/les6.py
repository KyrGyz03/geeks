class Streamer:    
    def live(self):       
        return "Запускаю стрим! Подписывайтесь, ставьте лайки!"
    
    def earn(self):       
        return "Заработал 500 донатов за 2 часа"


class TikToker:    
    def live(self):        
        return "Снимаю трендовый тикток под песню месяца!"
  
    def viral(self):        
        return "Набрал 3 миллиона просмотров за сутки!"
       

class Mutant:    
    def live(self):        
        return "Я... я свечусь в темноте... это мой вайб..."
    
    def superpower(self):       
        return "Летаю и стреляю лазерами из глаз"
    
#Если поменять местами родителей, то вызовется live() у стримера. Тот, что стоит первым - главнее
class MutStreamer(Mutant, Streamer):
    def ultimate_content(self):
        print(self.superpower(), self.earn())
#Если поменять местами родителей, то вызовется live() у стримера. Тот, что стоит первым - главнее
class StreamerTok(Streamer, TikToker):
    def ultimate_content(self):
        print(self.earn(), self.viral())
#Если поменять местами родителей, то вызовется live() у стримера. Тот, что стоит первым - главнее
class TikTokMut(TikToker, Mutant):
    def ultimate_content(self):
        print(self.viral(), self.superpower())

        
cyclope = MutStreamer()
print(cyclope.live())
cyclope.ultimate_content()
print(MutStreamer.mro())
print('')


natt = StreamerTok()
print(natt.live())
natt.ultimate_content()
print(StreamerTok.mro())
print('')

sleDuck = TikTokMut()
print(sleDuck.live())
sleDuck.ultimate_content()
print(TikTokMut.mro())
print('')