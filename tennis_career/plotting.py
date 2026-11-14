import matplotlib.pyplot as plt

def plot_tennis_career_matches(match_df):
    wins = match_df[match_df["result"] == "W"]
    losses = match_df[match_df["result"] == "L"]

    fig, ax = plt.subplots(figsize=(12, 7))

    ax.scatter(wins["player_age"], wins["age_difference"], color="blue", s=8, label="Matches won")
    ax.scatter(losses["player_age"], losses["age_difference"], color="purple", s=8, label="Matches lost")

    ax.axhline(0, color="gray")
    ax.set_title("Professional Tennis Matches by Age")
    ax.set_xlabel("Player Age (Years)")
    ax.set_ylabel("Age Difference (Years)")
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position("top")
    ax.legend()

    return fig



