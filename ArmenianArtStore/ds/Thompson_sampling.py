import numpy as np 
from sqlalchemy import create_engine, text 
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:group3@db:5432/ArmenianArtStore"  
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Fetch variants from the Variants table
variants = session.execute(text("SELECT * FROM public.Variants")).fetchall()

# Process variant statistics
variant_stats = {
    variant.VariantId: {"alpha": variant.alpha, "beta": variant.beta}
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

    # Update the alpha and beta values in the Variants table
    session.execute(
        text("""
            UPDATE public.Variants
            SET alpha = :alpha, beta = :beta
            WHERE VariantId = :variant_id
        """),
        {"alpha": variant_stats[variant_id]["alpha"], 
         "beta": variant_stats[variant_id]["beta"], 
         "variant_id": variant_id}
    )
    session.commit()
