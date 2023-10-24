def main():
  businessCategories = ["Grocery", "Electronics", "Hobby", "Food", "Finance"]

  company1 = { "name": "Walmart", "category": businessCategories[0] }

  company2 = { "name": "Hyvee", "category": businessCategories[0] }

  company3 = { "name": "Best Buy", "category": businessCategories[1] }

  company4 = { "name": "Runza", "category": businessCategories[3] }

  companies = [company1, company2, company3, company4]

  employee1 = { "firstName": "John", "lastName": "Doe", "company": companies[0] }

  employee2 = { "firstName": "Jane", "lastName": "Doe", "company": companies[0] }

  employee3 = { "firstName": "Chad", "lastName": "Smith", "company": companies[2] }

  employee4 = { "firstName": "Karen", "lastName": "Smith", "company": companies[3] }

  employees = [employee1, employee2, employee3, employee4]

  # print(f'Hello, my name is {employees[0]["firstName"]} {employees[0]["lastName"]}, and I work at {employees[0]["company"]["name"]}, which is a {employees[0]["company"]["category"]} business.')

  i = 0
  while i < len(employees):
    print(f'Hello, my name is {employees[i]["firstName"]} {employees[i]["lastName"]}, and I work at {employees[i]["company"]["name"]}, which is a {employees[i]["company"]["category"]} business.')

    i = (i + 1)

if __name__ == '__main__':
  main()
