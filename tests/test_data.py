from faker import Faker
import random
from datetime import datetime

fake = Faker()

def generate_transaction_data():
    transaction_sum = round(random.uniform(1000, 10000), 2)
    bank_account_balance = random.randint(50000, 59000)
    return transaction_sum, bank_account_balance

def format_date():
    date = datetime.now()
    cur_time = date.strftime("%H:%M")
    date_short = date.strftime("%d.%m.%y")
    date_long = date.strftime("%d.%m.%Y")
    return date_short, date_long, cur_time