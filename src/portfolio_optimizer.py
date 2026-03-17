import pandas as pd

def portfolio_allocation(risk):

    if risk == "High":
        return {
            "Stocks":60,
            "ETFs":20,
            "Bonds":10,
            "Cash":10
        }

    if risk == "Medium":
        return {
            "Stocks":40,
            "ETFs":30,
            "Bonds":20,
            "Cash":10
        }

    return {
        "Stocks":20,
        "ETFs":20,
        "Bonds":40,
        "Cash":20
    }


def investment_growth(initial, monthly, years, rate=0.08):

    months = years*12
    balance = initial

    values=[]

    for m in range(months):

        balance = balance*(1+rate/12)
        balance += monthly
        values.append(balance)

    df = pd.DataFrame({
        "Month":range(1,months+1),
        "Value":values
    })

    return df