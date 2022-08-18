def read_company_ratings(path):
   _companies_ratings = {}
   with open(path) as ratings:
      for line in ratings:
         company, rating = line.split(",")
         rating = rating.split("/")[0]
         _companies_ratings[company] = float(rating)
   return _companies_ratings

def read_items(path, _companies_ratings):
   _items_companies = {}
   with open(r"products.txt") as products:
      for line in products:
         company, item_str = line.split("-")
         item_list = item_str.replace("\n", "").strip().split(",")
         for item in item_list:
            if item not in _items_companies:
               _items_companies[item] = []
            company_order = 0
            for i in range(len(_items_companies[item])):
               if _companies_ratings[_items_companies[item][i]] > _companies_ratings[company]:
                  company_order += 1
               else:
                  break
            _items_companies[item].insert(company_order, company)
   return _items_companies

def search_item(item_name, items_companies, companies_ratings):
   if item_name in items_companies:
      available_companies = items_companies[item_name]
      number_of_companies = len(available_companies)
      if number_of_companies == 1:
         print("Only {0} sells this product.".format(available_companies[0]))
      else:
         print("We suggest you to buy {} from {} because it has the highest ranking as {:.2f}".format(item_name, available_companies[0],
                                                                                                      companies_ratings[available_companies[0]]))
   else:
      print("None of the companies sell this product.")

def run_program(companies_ratings, items_companies):
   while (1):
      item_name = input("Please enter the product you want to buy:")
      if item_name == "exit":
         break
      elif item_name == "Exit":
         item_name = input("Did you mean 'exit'?(y/n)")
         if item_name == "y":
            break
      else:
         search_item(item_name, items_companies, companies_ratings)
   print("Goodbye!")

def main():
   companies_ratings = read_company_ratings(r"ratings.txt")
   items_companies = read_items(r"products.txt", companies_ratings)
   run_program(companies_ratings, items_companies)

if __name__ == "__main__":
   main()