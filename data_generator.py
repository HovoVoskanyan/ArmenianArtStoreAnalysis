from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta
import uuid


fake = Faker()

NUM_REGIONS = 50
NUM_USERS = 500
NUM_PRODUCTS = 200
NUM_EVENTS = 50
NUM_ORDERS = 1000
NUM_USER_SESSIONS = 500
NUM_VARIANT_EVENTS = 500

DATE_RANGE_START = datetime(2023, 10, 1)
DATE_RANGE_END = datetime(2023, 11, 30)

import random

continent_country_city_pairs = {
    "North America": {
        "United States": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
        "Canada": ["Toronto", "Vancouver", "Montreal", "Calgary", "Ottawa"]
    },
    "Europe": {
        "France": ["Paris", "Marseille", "Lyon", "Toulouse", "Nice"],
        "Germany": ["Berlin", "Munich", "Frankfurt", "Hamburg", "Cologne"]
    },
    "Asia": {
        "Japan": ["Tokyo", "Osaka", "Kyoto", "Yokohama", "Nagoya"]
    }
}

def generate_regions(region_id):
    
    continent = random.choice(list(continent_country_city_pairs.keys()))
    
    country = random.choice(list(continent_country_city_pairs[continent].keys()))
    
    city = random.choice(continent_country_city_pairs[continent][country])
    
    return {
        "RegionId": region_id,
        "Continent": continent,
        "Country": country,
        "City": city
    }


def generate_users(user_id):
    return {
        "UserId": user_id,
        "SessionId": random.randint(1, NUM_USER_SESSIONS),
        "DeviceType": random.choice(["Mobile", "Desktop", "Tablet"]),
        "UserType": random.choice(["Regular", "Premium"]),
        "RegionId": random.randint(1, NUM_REGIONS)
    }

def generate_products(product_id):
    return {
        "ProductId": product_id,
        "Name": fake.word().capitalize(),
        "Description": fake.sentence(),
        "Images": fake.image_url(),
        "UnitPrice": round(random.uniform(10, 500), 2),
        "CreationDate": fake.date_between(start_date=DATE_RANGE_START, end_date=DATE_RANGE_END),
        "AuthorFullName": fake.name(),
        "Type": random.choice(["Art", "Print", "Sculpture", "Photography"])
    }

def generate_variant_events(event_id):
    return {
        "Id": event_id,
        "VariantId": random.choice([1, 2]),  
        "EventId": random.randint(1, NUM_EVENTS)
    }

def generate_events(event_id):
    event_types = ["Click", "Scroll", "Add to Cart", "Remove from Cart", "Purchase"]
    return {
        "EventId": event_id,
        "EventName": random.choice(event_types)  
    }

def generate_orders(order_id):
    order_date = fake.date_time_between(start_date=DATE_RANGE_START, end_date=DATE_RANGE_END)
    return {
        "OrderId": order_id,
        "OrderDate": order_date,
        "ProductId": random.randint(1, NUM_PRODUCTS),
        "UserId": random.randint(1, NUM_USERS),
        "VariantId": random.choice([1, 2])  
    }

def generate_user_sessions(session_id):
    start_time = fake.date_time_between(start_date=DATE_RANGE_START, end_date=DATE_RANGE_END)
    end_time = start_time + timedelta(hours=random.randint(1, 5))
    return {
        "Id": session_id,
        "UserId": random.randint(1, NUM_USERS),
        "VariantId": random.choice([1, 2]), 
        "SessionStartDate": start_time,
        "SessionEndDate": end_time,
        "SessionToken": str(uuid.uuid4())
    }

def generate_variant_events(event_id):
    return {
        "Id": event_id,
        "VariantId": random.choice([1, 2]),  
        "EventId": random.randint(1, NUM_EVENTS)
    }


