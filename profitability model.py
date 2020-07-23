from matplotlib import pyplot as plt
import numpy as np


def calculate_profitability(efficiency, hourly_consumption_rate_per_machine_in_tonnes):

    # efficiency = 0.72

    # in tonne
    unit_weight = 0.018

    # in usd
    cost_per_tonne_of_units = 45

    # in usd / unit
    unit_cost = (unit_weight) * cost_per_tonne_of_units

    # in usd / tonne
    price_per_tonne = 120

    # in units / hour / machine
    hourly_consumption_rate_per_machine_in_units = 17

    # # in tonne / hour / machine
    # hourly_consumption_rate_per_machine_in_tonnes = hourly_consumption_rate_per_machine_in_units * \
    #     unit_weight

    number_of_machines = 3

    # in tonne / hour
    total_hourly_consumption_rate = hourly_consumption_rate_per_machine_in_tonnes * \
        number_of_machines

    # in tonne / hour / machine
    hourly_production_rate_per_machine = hourly_consumption_rate_per_machine_in_tonnes * efficiency

    # in tonne / hour
    total_hourly_production_rate = hourly_production_rate_per_machine * number_of_machines

    # CONSUMPTIONS
    daily_consumption_rate = total_hourly_consumption_rate * 8
    weekly_consumption_rate = daily_consumption_rate * 5
    monthly_consumption_rate = weekly_consumption_rate * 4

    # PRODUCTIONS
    daily_production_rate = total_hourly_production_rate * 8
    weekly_production_rate = daily_production_rate * 5
    monthly_production_rate = weekly_production_rate * 4

    # in usd
    monthly_salaries = 3000

    # in kWh
    electricity_consumption_per_tonne = 8.6

    # in usd / kWh
    cost_of_kwh = 0.082

    # in usd / month
    total_monthly_electricity_consumption = monthly_consumption_rate * \
        electricity_consumption_per_tonne * cost_of_kwh

    monthly_material_costs = monthly_consumption_rate * cost_per_tonne_of_units

    monthly_expenses = monthly_material_costs + \
        monthly_salaries + total_monthly_electricity_consumption
    monthly_income = monthly_production_rate * price_per_tonne

    profit = monthly_income - monthly_expenses

    # print(
    #     f'hourly_consumption_rate_per_machine_in_tonnes: {hourly_consumption_rate_per_machine_in_tonnes}')

    # print(f'total_hourly_consumption_rate: {total_hourly_consumption_rate}')

    # print(f'total_hourly_production_rate: {total_hourly_production_rate}')

    # print(f'monthly_consumption_rate: {monthly_consumption_rate}')

    # print(f'monthly_production_rate: {monthly_production_rate}')

    # print(
    #     f'total_monthly_electricity_consumption: {total_monthly_electricity_consumption}')

    # print(f'')

    # print(f'profit: {profit}')

    return (profit / monthly_expenses) * 100


# print(calculate_profitability(0.3))


hourly_consumption_rate_per_machine_in_tonnes_values = [
    i for i in np.arange(0, 600, 25)]

x_variable = hourly_consumption_rate_per_machine_in_tonnes_values

net_profit_values_1 = [calculate_profitability(
    0.60, j/1000) for j in x_variable]
net_profit_values_2 = [calculate_profitability(
    0.80, j/1000) for j in x_variable]
net_profit_values_3 = [calculate_profitability(
    1, j/1000) for j in x_variable]

net_profit_values_4 = [calculate_profitability(
    0.72, j/1000) for j in x_variable]

net_profit_values_5 = [calculate_profitability(
    0.90, j/1000) for j in x_variable]


plt.plot(x_variable,
         net_profit_values_1, label='TR 60%', marker='o', linestyle='-', color='#000')
plt.plot(x_variable,
         net_profit_values_2, label='TR 80%', marker='^', linestyle='-', color='#000')
plt.plot(x_variable,
         net_profit_values_3, label='TR 100%', marker='s', linestyle='-', color='#000')
plt.plot(x_variable,
         net_profit_values_4, label='État Actuel (TR 72%)', marker='', linestyle='dotted', color='#000')
plt.plot(x_variable,
         net_profit_values_5, label='État Desiré (TR 90%)', marker='', linestyle='dashed', color='#000')

plt.plot([350, 350], [-100, 100], linestyle='-.',
         color='#000', linewidth=1, label='Capacité maximale des machines')

plt.plot([0, 600], [0, 0], linestyle='-',
         color='#000', linewidth=1)


plt.ylim(-100, 100)
plt.xlim(0, 600)

plt.legend()

plt.xticks(np.arange(0, 650, 50))
# plt.grid('g--')

plt.ylabel('Rentabilité (%)')
plt.xlabel("Flux entrant [palettes] (Kg / hr)")

plt.show()
