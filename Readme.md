# Red Tide Home Brewery

## Homebrewery Controller
This is a new single vessel electric brew in a bag (eBIAB) setup for my home brewery.  The PID for mash control uses the algrorithm from Justin Angevaare creator of [brew2](https://github.com/jangevaare/brew2).  The controller will be running on a Raspberry Pi 4 with Node Red and potentially InfluxDB for logging purposes.

### Original/Current Setup
In Feburary 2016, I purchased a Unibräu eBIAB setup.  While it has produced some excellent beers, it is time to update my system to a more automated system with a higher wattage heating element
- [Bräu Supply Unibräu](https://brausupply.com/)
  - 11 gallon kettle
  - Fine mesh basket
- 2 - 1200 W 110V Heating elements
- ['Ferroday' Pump](https://www.amazon.com/gp/product/B073P19L8P)
- 2 - 7 gallon [SS Brewtech Brewmaster Edition](https://www.ssbrewtech.com/collections/brew-buckets/products/the-brewmaster-bucket) buckets

### To Do
- [ ] Put together parts list for building the controller
- [ ] Add wiring schematic and images of controller wiring
- [x] Add timer for mash and hop additions
- [x] BeerXML importing for mash temperature and hop schedules

## Credits and References
[brew2 by Justin Angevaare](https://github.com/jangevaare/brew2)