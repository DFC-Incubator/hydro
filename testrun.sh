docker run --rm -a stdout -a stderr -e testde2 -e testde2 --log-driver=none -v /home/mconway/temp/hydro:/de-app-work  --name hydro -w /de-app-work --name hydro --net=bridge  --entrypoint="PopulationVsSoilMoisture.scr" diceunc/hydro1:1.0

docker run --rm -a stdout -a stderr -e testde2 -e testde2 --log-driver=none -v /home/mconway/temp/hydro:/de-app-work  --name hydro -w /de-app-work --name hydro --net=bridge  --entrypoint="python -i" diceunc/hydro1:1.0

