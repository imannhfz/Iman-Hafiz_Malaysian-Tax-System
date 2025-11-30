import pandas as pd

def verify_user(ic_number, password):
    """
    Check IC length and password (last 4 digits of IC).
    """
    if len(ic_number) != 12:
        return False

    if password == ic_number[-4:]:
        return True
    else:
        return False

def calculate_tax(income, tax_relief):
    chargeable = income - tax_relief
    if chargeable < 0:
        chargeable = 0

    tax = 0

    # 5,001 – 20,000 : 1% on next 15,000
    if chargeable > 5000:
        tax += min(chargeable - 5000, 15000) * 0.01

    # 20,001 – 35,000 : 3% on next 15,000
    if chargeable > 20000:
        tax += min(chargeable - 20000, 15000) * 0.03

    # 35,001 – 50,000 : 6% on next 15,000
    if chargeable > 35000:
        tax += min(chargeable - 35000, 15000) * 0.06

    # 50,001 – 70,000 : 11% on next 20,000
    if chargeable > 50000:
        tax += min(chargeable - 50000, 20000) * 0.11

    # 70,001 – 100,000 : 19% on next 30,000
    if chargeable > 70000:
        tax += min(chargeable - 70000, 30000) * 0.19

    # 100,001 – 250,000 : 25% on next 150,000
    if chargeable > 100000:
        tax += min(chargeable - 100000, 150000) * 0.25

    # 250,001 – 400,000 : 26% on next 150,000
    if chargeable > 250000:
        tax += min(chargeable - 250000, 150000) * 0.26

    # 400,001 – 600,000 : 28% on next 200,000
    if chargeable > 400000:
        tax += min(chargeable - 400000, 200000) * 0.28

    # 600,001 – 1,000,000 : 30% on next 400,000
    if chargeable > 600000:
        tax += min(chargeable - 600000, 400000) * 0.30

    # 1,000,001 – 2,000,000 : 32% on next 1,000,000
    if chargeable > 1000000:
        tax += min(chargeable - 1000000, 1000000) * 0.32

    # Above 2,000,000 : 33% on the rest
    if chargeable > 2000000:
        tax += (chargeable - 2000000) * 0.33

    return tax

def save_to_csv(data, filename):
    try:
        df = pd.read_csv(filename)
        df = df.append(data, ignore_index=True)
        df.to_csv(filename, index=False)
    except:
        df = pd.DataFrame([data])
        df.to_csv(filename, index=False)

def read_from_csv(filename):

    try:
        df = pd.read_csv(filename)
        return df
    except:
        return None