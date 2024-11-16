#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from sqlalchemy import create_engine, Session
import random

# Fetch variants from the db schema
variants = session.execute("SELECT * FROM db.Variants").fetchall()

# Process variant statistics
variant_stats = {
    variant["VariantId"]: {"alpha": variant["alpha"], "beta": variant["beta"]}
    for variant in variants
}

# Thompson Sampling function
def thompson_sampling():
    samples = {}
    for variant_id, stats in variant_stats.items():
        # Sample from the Beta distribution
        sample = np.random.beta(stats["alpha"], stats["beta"])
        samples[variant_id] = sample
    return max(samples, key=samples.get)

# Function to record user feedback and update the database
def record_user_feedback(user_id, variant_id, event_success):
    if event_success:
        variant_stats[variant_id]["alpha"] += 1
    else:
        variant_stats[variant_id]["beta"] += 1

    # Update the alpha and beta values in the db schema
    session.execute("""
        UPDATE db.Variants
        SET alpha = :alpha, beta = :beta
        WHERE VariantId = :variant_id
    """, {"alpha": variant_stats[variant_id]["alpha"], "beta": variant_stats[variant_id]["beta"], "variant_id": variant_id})
    session.commit()

