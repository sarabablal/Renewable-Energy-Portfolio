## EcoSolar Advisor 
EcoSolar Advisor is a CLI tool, made in Python to help people move toward solar power for residential homes in Morocco. You give it an easy monthly electricity bill number, then it calculates the power usage using progressive tax and tariff setups. After that, it sizes a proper photovoltaic system, and checks both the financial returns and the environmental impact. 
### Main features :
#### Tax & net bill calculation (TaxCalc Class) : 
It deducts the national TVA at 14% and also subtracts some fixed grid fees, so the program ends up with the net spending on electricity.
#### Energy consumption estimation: 
It kind of flips the utility "tariff tranches” from MAD to kWh, to estimate your monthly energy consumption and then totals it out to an annual figure.  
#### Solar system sizing (SolarSystem Class) :  
- It sizes the needed PV panels, assuming 500W units, aiming to cover as much as 85% of the monthly energy needs.  
- It also estimates the full hardware arrangement costs, like panels, inverter, and accessories, in the overall budget.  
- Finally it calculates financial savings plus the payback timeline, the ROI measured in years, and that is where you see how quickly it makes sense.
