# Average Rainfall Calculator

## Main
- Set total_rainfall to 0
- Set total_months to 0

- Prompt the user for the number of years
- Read years

- USer input validation (positive number)
  - Display error message
  - Prompt the user for the number of years again
  - Read years

- For each year from 1 to years value
  - Display current year

  - For each month
    - Prompt for the rainfall for the current month
    - Read rainfall

    - USer input validation (positive number)
      - Display error message
      - Prompt the user for the rainfall for the current month
      - Get rainfall

    - Add rainfall` to total_rainfall
    - Increment total_months by 1

- Calculate average_rainfall (total_rainfall divided by total_months)

- Display to user total_months, total_rainfall, average_rainfall
