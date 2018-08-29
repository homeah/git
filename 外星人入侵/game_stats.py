import pickle
class GameStats():
    def __init__(self,ai_setting):
        self.ai_setting = ai_setting
        self.game_active = False
        with open('High_Score.pkl','rb') as f:
            self.Hi_Score = pickle.load(f)
        self.high_score = int(self.Hi_Score['Score'])
        self.reset_stats()

    def reset_stats(self):
        self.ship_left = self.ai_setting.ship_limit
        self.score = 0
        self.level = 1
