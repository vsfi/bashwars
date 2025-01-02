# oh-my-pwsh

The task is to find VM which has too much CPU

## Answer

esxi-40-Oxygen.vsfi.org

## Writeup

- Read the .csv
- Select object from Oxygen DC
- Sort by CPU desc
- Print the first result's `host` field

## Oneliner

`((Import-Csv "*.csv" | Where-Object { $_.Datacenter -eq 'Oxygen' } | Sort-Object { [int]$_.CPUCores  } -Descending | Select-Object -First 1)).host`
