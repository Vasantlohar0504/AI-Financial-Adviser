def financial_score(savings_rate, debt_ratio):
    
    score = 50

    score += savings_rate * 50
    score -= debt_ratio * 30

    return max(0,min(100,int(score)))


def generate_advice(risk):

    if risk == "High":
        return "You have high risk tolerance. Consider more stocks and ETFs."

    if risk == "Medium":
        return "Balanced investor. Diversified portfolio recommended."

    return "Low risk tolerance. Focus on bonds and stable investments."