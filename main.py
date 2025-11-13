import pandas as pd

FILE = "vgsales.csv"
df = pd.read_csv(FILE, on_bad_lines="skip")

required_columns = [
    "Name",
    "Platform",
    "Year",
    "Genre",
    "Publisher",
    "Global_Sales",
]
df = df[required_columns]

# Cleaning data
df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")


while True:
    game_info_input = input("Enter the game's name to get the general info\n").lower()
    game_row = df[df["Name"].str.lower().str.contains(game_info_input)]
    total_sales = game_row["Global_Sales"].sum()

    game_info_sort = input(
        "Do you want to sort the results in any order?\nType 'Y' for year, 'GS' for Global Sales and type 'N' fo 'No'\n"
    ).lower()

    if game_row.empty:
        print(
            f"\nSorry, I could not find a game named '{game_info_input.title()}' in the dataset."
        )
    else:
        if game_info_sort == "n":
            print(f"\n--- General Info for {game_info_input.title()} ---")
            print(game_row)
        elif game_info_sort == "y":
            print(
                f"\n--- General Info for {game_info_input.title()}, Sorted by 'Year' ---"
            )
            print(game_row.sort_values(by="Year"))
        elif game_info_sort == "gs":
            print(
                f"\n--- General Info for {game_info_input.title()}, Sorted by 'Year' ---"
            )
            print(game_row.sort_values(by="Global_Sales"))

    overall_sell = input(
        f"Do you also want to know how much {game_info_input} sold?\nType 'Y' or 'N'.\n"
    ).lower()

    if overall_sell == "y":
        print(f"The total sell for {game_info_input} is: {total_sales:.2f} Million")
    else:
        break

    top_10_games = input(
        "Do you want to know what the top 10 games are?\nType 'Y' or 'N'.\n"
    )

    if top_10_games == "y":
        print(df.sort_values(by="Global_Sales", ascending=False).head(10))
    else:
        break
