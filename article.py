import pandas as pd

df = pd.read_csv("articles.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")


class Article:
    def __init__(self, article_id):
        self.article_id = article_id
        self.article_name = df.loc[df["id"] == article_id, "name"].squeeze()
        self.article_price = df.loc[df["id"] == article_id, "price"].squeeze()

    def available(self):
        in_stock = df.loc[df["id"] == self.article_id, "in stock"].squeeze()
        if in_stock > 0:
            return True
        else:
            return False

    def book(self):
        in_stock = df.loc[df["id"] == self.article_id, "in stock"].squeeze()
        df.loc[df["id"] == self.article_id, "in stock"] = in_stock - 1
        df.to_csv("articles.csv", index=False)
        print("Booking was successfully.")
