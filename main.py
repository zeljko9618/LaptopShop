import pandas as pd
from article import Article
from pdfConfirmation import Pdf
from creditCard import CreditCard

df = pd.read_csv("articles.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")

print(df)
id = input("Enter the id of the product you want to buy: ")

article = Article(id)

if article.available():
    decision = input(f"Do you want to buy {article.article_name}? ")
    if decision == "yes":
        card_number = input("Enter your Credit Card Number: ")
        credit_card = CreditCard(number=card_number)
        name = input("Enter the name of the card holder: ")
        expiration = input("Enter your expiration date: ")
        cvc = input("Enter your cvc: ")
        if credit_card.validate(name=name, expiration=expiration, cvc=cvc):
            article.book()
            print(f"Congratulations {name}! Your order was successfully!" + "\n" +
                  f"You can find your pdf confirmation in the Project Source")
            pdf = Pdf(article)
            pdf.create_pdf()
        else:
            print("Validation failed. Your card information is invalid.")
    else:
        print("Good!")
else:
    print("Article is not available.")

