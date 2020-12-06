class Category:
  

  def __init__(self,name):
    self.name=name
    self.ledger=list()
    
  
  def check_funds(self,value):
    fund=0
    n=len(self.ledger)
    for i in range(n):
      fund=fund+self.ledger[i]["amount"]
    if value>fund:
      return False
    else:
      return True
  
  def get_balance(self):
    fund=0
    n=len(self.ledger)
    for i in range(n):
      fund=fund+self.ledger[i]["amount"]
    return fund

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
    
  
  def withdraw(self,amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount":-(amount), "description":description})
      return True
    else:
      return False

  def transfer(self, amount, obname):
    objectname = obname.name
    a=self.withdraw(amount, f"Transfer to {objectname}")
    b=obname.deposit(amount, f"Transfer from {self.name}")
    if a:
      return True
    else:
      return False

  def __str__(self):
    title=f"{self.name:*^30}\n"
    items=''
    total=0
    for i in range(len(self.ledger)):
      items+=f"{self.ledger[i]['description'][0:23]:23}" + f"{self.ledger[i]['amount']:>7.2f}" + '\n'
      total+=self.ledger[i]["amount"]
    output=title+items+"Total: "+str(total)
    return output
  


def create_spend_chart(categories):
  string = "Percentage spent by category\n"
  accum = 0
  parts = []
  for category in categories:
    accum = accum + category.get_balance()
  for category in categories:
    parts.append(category.get_balance() * 100 / accum)
    
  act = 100
  while act >= 0:
    if act == 100:
      string = string + str(act) +"|"
    elif act > 0:
      string = string + " " + str(act) +"|"
    else:
      string = string + "  " + str(act) +"|"
    for part in parts:
      if part >= act:
        
        string = string + " o "
    act = act - 10
    string = string + "\n"
  string = string + "    -" + ("---"* len(parts)) + "\n"
  
  atoms = []
  for category in categories:
    atoms.append(list(category.name))
  atomicity = atoms.copy()
  while len(atomicity) > 0:
    subString = ""
    for atom in atoms:
      subString = subString + " " + atom[0] + " "
      if len(atom) >= 1 and atom[0]!=" ":
        atom.remove(atom[0])
        if len(atom) == 0:
          atom.append(" ")
          atomicity.remove(atomicity[0])
    if(len(atomicity) > 0):
      subString = subString + "\n"
    string = string + "    " + subString

  return string