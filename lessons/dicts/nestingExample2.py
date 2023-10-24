def main():
  businessCategories = initBusinessCategories()

  products = initProducts()

  companies = initCompanies(businessCategories, products)

  employees = initEmployees(companies)

  printEmployeeGreetings(employees)

def printEmployeeGreetings(employees):
  i = 0
  while i < len(employees):
    employee = employees[i]

    productNamesString = createProductNamesString(employee["company"]["products"])

    print(f'Hello, my name is {employee["firstName"]} {employee["lastName"]}, and I work at {employee["company"]["name"]}, which is a {employee["company"]["category"]} business. We sell stuff like: {productNamesString}')

    i = (i + 1)

def createProductNamesString(products):
  productNames = []

  i = 0
  while i < len(products):
    productNames.append(products[i]["name"])

    i = (i + 1)

  productNamesString = ', '.join(productNames)

  return productNamesString

def initBusinessCategories():
  return ["Grocery", "Electronics", "Hobby", "Food", "Finance"]

def initProducts():
  return [
    { "name": "Apple", "weight": 0.8, "price": 3.1 },
    { "name": "Orange", "weight": 1.1, "price": 2.6 },
    { "name": "Dell Laptop", "weight": 4.2, "price": 431.4 },
    { "name": "Stapler", "weight": 0.3, "price": 5.2 },
    { "name": "Hamburger", "weight": 0.3, "price": 9.4 },
    { "name": "Fries", "weight": 0.5, "price": 2.9 }
  ]

def initCompanies(businessCategories, products):
  company1 = {
    "name": "Walmart",
    "category": businessCategories[0],
    "products": [ products[0], products[1], products[3] ]
  }

  company2 = {
    "name": "Hyvee",
    "category": businessCategories[0],
    "products": [ products[0], products[1] ]
  }

  company3 = {
    "name": "Best Buy",
    "category": businessCategories[1],
    "products": [ products[2], products[3] ]
  }

  company4 = {
    "name": "Runza",
    "category": businessCategories[3],
    "products": [ products[4], products[5] ]
  }

  companies = [company1, company2, company3, company4]

  return companies

def initEmployees(companies):
  employee1 = { "firstName": "John", "lastName": "Doe", "company": companies[0] }

  employee2 = { "firstName": "Jane", "lastName": "Doe", "company": companies[0] }

  employee3 = { "firstName": "Chad", "lastName": "Smith", "company": companies[2] }

  employee4 = { "firstName": "Karen", "lastName": "Smith", "company": companies[3] }

  employees = [employee1, employee2, employee3, employee4]

  return employees

if __name__ == '__main__':
  main()
