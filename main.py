# World_Cup Application
# Made by Kasra Tookallo in 2025
# Senior Python engineer solution: Group B ranking calculator
# Input is received directly from the applicant (user) via stdin

# Define teams and match order
teams = ["Iran", "Portugal", "Spain", "Morocco"]
matches = [
    ("Iran", "Spain"),
    ("Iran", "Portugal"),
    ("Iran", "Morocco"),
    ("Spain", "Portugal"),
    ("Spain", "Morocco"),
    ("Portugal", "Morocco"),
]


def parse_scores():
    scores = []
    for i in range(6):
        line = input().strip()
        try:
            # for getting scores in x-y style as string
            a_str, b_str = line.split("-")

            # converting string to integer
            a, b = int(a_str), int(b_str)

        except Exception:
            raise ValueError(f"Invalid score format: '{line}'. Use 'x-y'.")
        scores.append((a, b))
    return scores


def compute_stats(matches, scores):
    stats = {t: {"wins": 0, "loses": 0, "draws": 0, "gd": 0, "points": 0} for t in teams}
    for (home, away), (gh, ga) in zip(matches, scores):
        # update goal difference
        # gaal home (gh) and goal away (ga)
        stats[home]["gd"] += gh - ga
        stats[away]["gd"] += ga - gh

        # outcome
        if gh > ga:
            stats[home]["wins"] += 1
            stats[home]["points"] += 3
            stats[away]["loses"] += 1
        elif gh < ga:
            stats[away]["wins"] += 1
            stats[away]["points"] += 3
            stats[home]["loses"] += 1
        else:
            stats[home]["draws"] += 1
            stats[away]["draws"] += 1
            stats[home]["points"] += 1
            stats[away]["points"] += 1
    return stats


def rank_teams(stats):
    # Sort by: points desc, wins desc, team name asc
    ranked = sorted(
        stats.items(),
        key=lambda item: (-item[1]["points"], -item[1]["wins"], item[0])
    )
    return ranked


def print_results(ranked):
    for team, s in ranked:
        print(
            f"{team}  wins:{s['wins']} , loses:{s['loses']} , draws:{s['draws']} , goal difference:{s['gd']} , points:{s['points']}")


def main():
    scores = parse_scores()
    stats = compute_stats(matches, scores)
    ranked = rank_teams(stats)
    print_results(ranked)


if __name__ == "__main__":
    main()

'''
در گروه B مسابقات جام‌جهانی تیم‌های ایران، پرتغال، اسپانیا و مراکش حضور دارند. برنامه‌ای بنویسید که با دریافت نتایج بازی‌ها، نام تیم و تعداد برد و باخت و تفاضل گل و امتیاز آن‌ها را به ترتیب در یک خط چاپ کند. هر تیم به ترتیب امتیاز در یک خط چاپ شود. (در صورتی که امتیاز برابر بود، تعداد برد مدنظر قرار گیرد. در صورتی که هم تعداد برد و هم امتیاز برابر بود، بر اساس ترتیب حروف الفبا چاپ شوند.)

نکته: تیم در صورت باخت صفر امتیاز، در صورت تساوی یک امتیاز و در صورت برد سه امتیاز کسب می کند.
تفاضل گل تفاوت گل های زده و گل های خورده یک تیم است

نتایج بازی‌ها را به ترتیب زیر بخواند: (در ورودی نمونه عدد سمت چپ مربوط به تیم سمت راست می‌باشد.)
ایران – اسپانیا
ایران – پرتغال
ایران – مراکش
اسپانیا – پرتغال
اسپانیا – مراکش
پرتغال - مراکش




ورودی نمونه:

2-2
2-1
1-2
2-2
3-1
2-1
خروجی نمونه:

Spain  wins:1 , loses:0 , draws:2 , goal difference:2 , points:5
Iran  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Portugal  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Morocco  wins:1 , loses:2 , draws:0 , goal difference:-2 , points:3
'''