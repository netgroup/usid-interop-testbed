#!/bin/bash

passed=0
total=0
declare -a endpoints=(
        "fcff:1::1"
        "fcff:2::1"
        "fcff:3::1"
        "fcff:4::1"
        "fcff:5::1"
        "fcff:6::1"
        "fcff:7::1"
        "fcff:8::1"
)

for i in "${endpoints[@]}"; do
	ping -c 1 "${i}" &>/dev/null \
		&& { echo -e "${i}\treachable"; passed=$((passed+1)); } \
		|| { echo -e "${i}\tUNREACHABLE"; }
	total=$((total+1))
done

echo ""
printf "Test PASSED %d/%d\n" ${passed} ${total}
