docker build -t gin_script_01:1.0 -f ./Dockerfile .

docker run -d -p 8003:8080 --name gin_script_01 -t gin_script_01:1.0
