import pandas as pd

df = pd.read_csv("articles.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, name, expiration, cvc):
        card_dict = {'number': self.number, 'expiration': expiration, 'holder': name, 'cvc': cvc}
        if card_dict in df_cards:
            return True
        else:
            return False
