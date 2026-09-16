import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import sqlite3
    import pandas as pd

    __generated_with = "0.24.0"
    app = mo.App()
    return mo, pd, sqlite3


@app.cell
def _(mo):
    mo.md("""
    # 🏥 Clinic & Patient Demographics Dashboard
    Welcome to the interactive healthcare analytics dashboard. Use the filters below to explore patient distributions across different clinics and age groups.
    """)
    return


@app.cell
def _(pd, sqlite3):
    # Establish local SQLite connection (creates a database file in memory or locally)
    conn = sqlite3.connect("clinic_data.db")

    # Load your CSV files (adjust file paths if they are in a subfolder like 'data/')
    clinics_df = pd.read_csv("data/health/clinic.csv")  # clinic_id, clinic_name, city
    patients_df = pd.read_csv("data/health/patient.csv")  # patient_id, clinic_id, age, age_group

    # Write them into SQLite tables
    clinics_df.to_sql("clinics", conn, if_exists="replace", index=False)
    patients_df.to_sql("patients", conn, if_exists="replace", index=False);

    return clinics_df, conn, patients_df


@app.cell
def _(clinics_df, mo):
    # Get a unique list of cities for the dropdown
    city_list = sorted(clinics_df["city"].dropna().unique().tolist())

    # Create an interactive marimo dropdown widget
    city_dropdown = mo.ui.dropdown(
        options=city_list,
        value=city_list[0] if city_list else None,
        label="Select City: "
    )
    city_dropdown
    return (city_dropdown,)


@app.cell
def _(mo, patients_df):
    # Get a unique list of age groups for the multi-select
    age_groups_list = sorted(patients_df["age_group"].dropna().unique().tolist())

    # Create an interactive marimo multi-select widget (defaulting to all selected)
    age_multiselect = mo.ui.multiselect(
        options=age_groups_list,
        value=age_groups_list,
        label="Select Age Group(s): "
    )
    age_multiselect
    return (age_multiselect,)


@app.cell
def _(age_multiselect, city_dropdown, conn, mo, pd):
    # Guard against unselected states
    mo.stop(city_dropdown.value is None, mo.callout("Please select a city to view data."))
    mo.stop(not age_multiselect.value, mo.callout("Please select at least one age group."))

    # Format the selected age groups safely into a SQL tuple string (e.g., ('Adult', 'Senior'))
    selected_ages = tuple(age_multiselect.value)
    ages_sql_str = str(selected_ages) if len(selected_ages) > 1 else f"('{selected_ages[0]}')"

    # Construct the multi-parameter SQL query
    CUSTOM_SQL_QUERY = f"""
    SELECT 
        c.clinic_name,
        c.city,
        p.age_group,
        COUNT(p.patient_id) AS patient_count
    FROM clinics AS c
    JOIN patients AS p ON c.clinic_id = p.clinic_id
    WHERE c.city = '{city_dropdown.value}'
      AND p.age_group IN {ages_sql_str}
    GROUP BY c.clinic_name, c.city, p.age_group
    ORDER BY patient_count DESC;
    """

    # Run the query and display the table
    result_df = pd.read_sql_query(CUSTOM_SQL_QUERY, conn)
    mo.ui.table(result_df)
    return (result_df,)


@app.cell
def _(result_df):
    import matplotlib.pyplot as plt

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(8, 4))

    if not result_df.empty:
        # Plot patient counts by clinic name
        result_df.plot(
            kind="bar", 
            x="clinic_name", 
            y="patient_count", 
            ax=ax, 
            color="#4c72b0",
            legend=False
        )
        ax.set_title("Patient Counts by Clinic")
        ax.set_xlabel("Clinic Name")
        ax.set_ylabel("Patient Count")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
    else:
        ax.text(0.5, 0.5, "No data available for current filters", horizontalalignment='center', verticalalignment='center')
        ax.axis("off")

    # Marimo automatically renders matplotlib figures when referenced at the end of a cell
    fig
    return


if __name__ == "__main__":
    app.run()
