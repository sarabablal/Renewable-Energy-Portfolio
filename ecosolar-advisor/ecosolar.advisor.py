# forming TaxCalc class
class TaxCalc :
  def __init__(self, bill1):
    self.bill1 = bill1 
  
  def calculate_tax(self):
    net_before_tva = self.bill1 / 1.14
    tax = self.bill1 - net_before_tva
    tax_yearly = tax * 12
    return tax, tax_yearly
  
  def calculate_bill(self, tax):
    bill = self.bill1 - tax
    bill_yearly = bill * 12
    return bill, bill_yearly


def estimated_kwh_usage(bill1):
  t1, t2, t3, t4, t5, t6 = 0.9010, 1.0732, 1.1636, 1.3207, 1.4445, 1.5958
  fixed_fees = 15.0
  
  net_bill = (bill1 - fixed_fees) / 1.14
  if net_bill <= 0:
    return 0, 0

  if net_bill <= (100 * t1):
    kwh_monthly = net_bill / t1
  elif net_bill <= (100 * t1 + 50 * t2):
    kwh_monthly = 100 + (net_bill - (100 * t1)) / t2
  elif net_bill <= (200 * t3):
    kwh_monthly = net_bill / t3
  elif net_bill <= (300 * t4):
    kwh_monthly = net_bill / t4
  elif net_bill <= (500 * t5):
    kwh_monthly = net_bill / t5
  else:
    kwh_monthly = net_bill / t6
    
  kwh_yearly = kwh_monthly * 12
  return kwh_monthly, kwh_yearly


# forming SolarSystem class
class SolarSystem:
  def __init__(self):
    self.solar_panel = 2.25 
    self.sp_monthly = self.solar_panel * 30
    self.sp_yearly = self.solar_panel * 365
    
    self.sp500w = 1300
    self.inverter_fixed = 5500
    self.accessories = 2500
  

  def calculate_solar_system(self, kwh_monthly, bill_yearly, bill1):
    target_kwh = kwh_monthly * 0.85

    sp_needed = max(1, round(target_kwh / self.sp_monthly))
    
    sp_saving_monthly = sp_needed * self.sp_monthly
    sp_saving_yearly = sp_needed * self.sp_yearly
    
    sp_saving_monthly_dh = sp_saving_monthly * 1.35
    sp_saving_yearly_dh = sp_saving_monthly_dh * 12
    
    full_sp_price = self.accessories + self.inverter_fixed + (self.sp500w * sp_needed)
    
    payback = full_sp_price / sp_saving_yearly_dh if sp_saving_yearly_dh > 0 else 0
    
    solar = { 
    "sp_needed" : sp_needed,
    "sp_saving_monthly" : sp_saving_monthly,
    "sp_saving_yearly" : sp_saving_yearly,
    "sp_saving_monthly_dh" : sp_saving_monthly_dh,
    "sp_saving_yearly_dh" : sp_saving_yearly_dh,
    "payback" : payback,
    "full_sp_price" : full_sp_price
    }
    return solar


def print_terminal_report(bill1, tax, bill, kwh_monthly, co2_yearly_tonnes, solar):
  print("SOLAR FEASIBILITY REPORT")
  print(f"1. Electricity Consumption & Taxes:")
  print(f"   - Monthly Paid Bill           : {bill1:.2f} MAD")
  print(f"   - Estimated Monthly Taxes     : {tax:.2f} MAD")
  print(f"   - Net Monthly Electricity Cost: {bill:.2f} MAD")
  print(f"   - Estimated Energy Usage       : {kwh_monthly:.2f} kWh/Month")
  print(f"2. Recommended Solar Solution :")
  print(f"   - Required 500W Solar Panels  : {solar['sp_needed']} Units")
  print(f"   - Total Hardware & Setup Price: {solar['full_sp_price']:.2f} MAD")
  print(f"   - Estimated Yearly Savings    : {solar['sp_saving_yearly_dh']:.2f} MAD")
  print(f"   - Estimated Payback Period    : {solar['payback']:.2f} Years") 


if __name__ == '__main__':
  while True:
    try:
      bill1 = float(input("How much you usually pay for your electricity bill in DH? "))
      if bill1 <= 0:
        print("The number you entered is lower than or equal to 0. \nEnter the right number, please.")
      else:
        break
    except ValueError:
      print("Invalid input! Please enter a valid number.")
  
  calc = TaxCalc (bill1)
  tax, tax_yearly = calc.calculate_tax()
  bill, bill_yearly = calc.calculate_bill(tax)
  
  kwh_monthly, kwh_yearly = estimated_kwh_usage(bill1)
  
  system = SolarSystem()
  solar = system.calculate_solar_system(kwh_monthly, bill_yearly, bill1)
  
  print_terminal_report(bill1, tax, bill, kwh_monthly, solar)