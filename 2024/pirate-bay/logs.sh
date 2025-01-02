#!/bin/bash

generate_route() {
  routes=("/rum" "/ship-repair" "/sailors" "/sugar" "/weapons" "/salt" "/silk" "/dakimakura" "/mortars" "/treasure-map")
  echo ${routes[$RANDOM % ${#routes[@]}]}
}

generate_ip() {
  echo "$((RANDOM % 256)).$((RANDOM % 256)).$((RANDOM % 256)).$((RANDOM % 256))"
}

generate_date() {
  random_year=$((RANDOM % 5 + 2019))
  random_month=$((RANDOM % 12 + 1))
  random_day=$((RANDOM % 28 + 1))
  random_hour=$((RANDOM % 24))
  random_minute=$((RANDOM % 60))
  random_second=$((RANDOM % 60))
  printf "%02d/%b/%d:%02d:%02d:%02d +0000\n" $random_day $(date -d "$random_year-$random_month-01" '+%b') $random_year $random_hour $random_minute $random_second
}

generate_user() {
  users=("John" "Sam" "Jack" "Tyrell" "Lina" "Miron" "Richard" "Joseph" "Bill" "David")
  echo ${users[$RANDOM % ${#users[@]}]}
}

log_file="./shop.log"
log_count=0
max_logs=700

while [ $log_count -lt $max_logs ]; do
  current_date=$(generate_date)

  ip_address=$(generate_ip)
  route=$(generate_route)
  bytes_sent=$((RANDOM % 5000 + 500))
  user=$(generate_user)

  log_entry="$ip_address - - [$current_date] \"GET $route HTTP/1.1\" 200 $bytes_sent \"-\" \"$user\""

  echo $log_entry >> $log_file

  if (( log_count == 350)); then
    echo "1.3.3.7 - - [25/Sep/2022:12:07:15 +0000] \"GET /dakimakura HTTP/1.1\" 502 1790 \"-\" "mr.Pirate"" >> $log_file
  fi

  if (( log_count % 100 == 0 )); then
    echo "1.3.3.7 - - [25/Sep/2022:12:07:15 +0000] \"GET /dakimakura HTTP/1.1\" 502 1790 \"-\" "Miron"" >> $log_file
  fi

  ((log_count++))

done
