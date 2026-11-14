import matplotlib.pyplot as plt


def plot_tennis_career_matches(match_df):
    win_result = match_df["result"] == "W"
    loss_result = match_df["result"] == "L"
    match_wins = match_df[win_result]
    match_losses = match_df[loss_result]

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.scatter(match_wins["player_age"], match_wins["age_difference"], color=blue, label="Win", s=12)
    ax.scatter(match_losses["player_age"], match_losses["age_difference"], color=purple, label="Loss", s=12)

    ax.axhline(0, color="gray", linewidth=1)
    ax.set_xlabel("Player Age")
    ax.set_ylabel("Age Difference")
    ax.set_title("Age Differences in Tennis Career Matches")
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position("top")
    ax.grid(alpha=0.2)
    ax.legend()
    return fig


