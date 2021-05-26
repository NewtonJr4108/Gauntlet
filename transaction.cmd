curl --location --request POST 'localhost:5000/transaction' \
--header 'Content-Type: application/json' \
--data-raw '{
    "recipient":"recipient-pub-address",
    "amount":5
}'