import datetime
import matplotlib.pyplot as plt
def create_plot(timeline, name):
    confirmed_cases = []
    dates = []

    for key, value in timeline.items():
        confirmed_cases.append(value)
        dates.append(datetime.datetime.strptime(key,"%Y-%m-%dT%H:%M:%SZ").date())

    plt.figure(figsize=(6.4*2, 4.8*2))
    plt.plot(dates, confirmed_cases, label=f"Confirmed Cases in {name}")
    plt.legend()

    plt.ylabel(f"Confirmed Cases in {name}")
    plt.xlabel("Dates (Y-M)")

    plt.savefig(f"{name}")