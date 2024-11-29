def select_bandit(bandits):
    """
    Selects a bandit using Thompson Sampling.

    Receives the bandits, applies Thompson Sampling to select one,
    and returns the chosen bandit's details.

    Parameters:
    - bandits: Our project's bandits.

    Returns:
    - Bandit: The chosen bandit's details or None if no bandits are provided.
    """
    if not bandits:
        return {"message": "No bandits provided"}

    # Perform Thompson Sampling to choose a bandit
    samples = [np.random.beta(bandit.alpha, bandit.beta) for bandit in bandits]

    # Select the bandit with the highest sample
    chosen_bandit = bandits[np.argmax(samples)]

    return chosen_bandit


def apply_reward(chosen_bandit, liked: bool):
    """
    Applies user feedback to the chosen bandit's performance parameters.

    Parameters:
    - chosen_bandit (Bandit): The previously selected bandit.
    - liked (bool): Whether the user liked the bandit's output (True) or not (False).

    Returns:
    - bool: True if the feedback was successfully applied, False otherwise.
    """
    if not chosen_bandit:
        return {"message": "Chosen bandit not found"}

    # Update bandit's performance based on user feedback
    if liked:
        chosen_bandit.alpha += 1
    else:
        chosen_bandit.beta += 1
    chosen_bandit.n += 1

    return {"message": "Feedback applied successfully"}
