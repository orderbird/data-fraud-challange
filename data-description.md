The data is stored in csv format and compressed using gzip compression. The Content of each column is descriped in the following table:

| Column | Type        | Description               | Values |
|--------|-------------|---------------------------|--------|
| 1      | qualitative | Money on checking account | 11 : ... < 0
|        |             |                           | 12 : 0 <= ... < 200
|        |             |                           | 13 : ... >= 200 / salary assignments for at least 1 year
|        |             |                           | 14 : no checking account
| 2      | numerical   | Duration in month     
| 3      | categorical | Credit History            | 30 : no credits taken/ all credits paid back duly
|        |             |                           | 31 : all credits at this bank paid back duly
|        |             |                           | 32 : existing credits paid back duly till now
|        |             |                           | 33 : delay in paying off in the past
|        |             |                           | 34 : other credits existing (not at this bank)
| 4      | categorical | Purpose                   | 40 : car (new)
|        |             |                           | 41 : car (used)
|        |             |                           | 42 : furniture/equipment
|        |             |                           | 43 : radio/television
|        |             |                           | 44 : domestic appliances
|        |             |                           | 45 : repairs
|        |             |                           | 46 : education
|        |             |                           | 47 : vacation
|        |             |                           | 48 : retraining
|        |             |                           | 49 : business
|        |             |                           | 410 : others
| 5      | numerical   | Credit amount
| 6      | quantitive  | Savings account/bonds     | 61 : ... < 100 DM
|        |             |                           | 62 : 100 <= ... < 500
|        |             |                           | 63 : 500 <= ... < 1000
|        |             |                           | 64 : .. >= 1000
|        |             |                           | 65 : unknown
| 7      | qualitative | Current employment since  | 71 : unemployed
|        |             |                           | 72 : ... < 1 year
|        |             |                           | 73 : 1 <= ... < 4 years
|        |             |                           | 74 : 4 <= ... < 7 years
|        |             |                           | 75 : .. >= 7 years
| 8      | numeric     | Installment rate in percentage of disposable income |
| 9      | categorical | Personal status and sex   | 91 : male : divorced/separated
|        |             |                           | 92 : female : divorced/separated/married
|        |             |                           | 93 : male : single
|        |             |                           | 94 : male : married/widowed
|        |             |                           | 95 : female : single
| 10     | qualitative | Other debtors / guarantors | 101 : none
|        |             |                           | 102 : co-applicant
|        |             |                           | 103 : guarantor
| 11     | numerical   | Present residence since 
| 12     | qualitative | Property                  | 121 : real estate
|        |             |                           | 122 : if not 121 : building society savings agreement / life insurance
|        |             |                           | 123 : if not 121/122 : car or other, not in attribute 6
|        |             |                           | 124 : unknown / no property
| 13     | numeerical  | Age
| 14     | categorical | Other installment plans   | 141 : bank
|        |             |                           | 142 : stores
|        |             |                           | 143 : none
| 15     | categorical | Housing                   | 151 : rent
|        |             |                           | 152 : own
|        |             |                           | 153 : for free
| 16     | numerical   | Number of existing credits at this bank
| 17     | categorical | Job                       | 171 : unemployed/ unskilled - non-resident
|        |             |                           | 172 : unskilled - resident
|        |             |                           | 173 : skilled employee / official
|        |             |                           | 174 : management / self-employed / highly qualified employee / officer
| 18     | numerical   | Number of people being liable to provide maintenance for
| 19     | boolean     | Telephone                 | 191 : none
|        |             |                           | 192 : yes, registered under the customers name
| 20     | boolean     | Foreign worker            | 201 : yes
|        |             |                           | 202 : no 
| 21     | boolean     | Result                    | 1 : Good
|        |             |                           | 2 : Bad
