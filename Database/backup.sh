#!/bin/bash

today() {
	date +"%Y-%m-%d"
}

collections=("Accounts" "Camera" "Admin" "Images" "Sensor" "Station" "User")

mkdir $(today)
for collection in ${collections[@]}; do
	mongoexport --db 'LeanConnectedServicePlatform' --collection $collection --out "./$(today)/$collection.json"
done

tar -czvf "$(today).tar.gz" $(today)

rm -rf $(today)