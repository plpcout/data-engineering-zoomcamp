set -e

TAXI_TYPE=$1 #green
YEAR=$2  #2020
URL_PREFIX="https://github.com/DataTalksClub/nyc-tlc-data/releases/download"


for MONTH in {1..12}; do
# Format month `01, 02, ... 12`
FMONTH=`printf "%02d" ${MONTH}`

LOCAL_FILE_PATH="data/raw/${TAXI_TYPE}/${YEAR}/${FMONTH}"
FILE_NAME="${TAXI_TYPE}_tripdata_${YEAR}-${FMONTH}.csv.gz"
mkdir -p ${LOCAL_FILE_PATH}

echo Downloading file: ${FILE_NAME}
wget ${URL_PREFIX}/${TAXI_TYPE}/${FILE_NAME} -O ${LOCAL_FILE_PATH}/${FILE_NAME}
done
