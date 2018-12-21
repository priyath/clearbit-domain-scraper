import requests
import json
import sys
import csv

outputFilename = 'company_domain_mapping'
secret_key = 'sk_6548dc273dab30bcb0676bd890eb5d94'
companyCount = 0
not_found_count = 0

if len(sys.argv) > 1:
	outputFilename = sys.argv[1]

#send request to retrieve domain for company
def requestInfo(company):
	params = (
		('name', company),
	)

	response = requests.get('https://company.clearbit.com/v1/domains/find', params=params, auth= (secret_key, ''))
	json_data = json.loads(response.text)
	return json_data["domain"] if "domain" in json_data else ''
	
#read company list from file
with open('company_list') as f:
	companies = [line.rstrip() for line in f]
	companyCount = len(companies)
	print('Number of companies: ' + str(companyCount))

#iterate company list and write output to csv
with open(outputFilename+'.csv', 'w') as file:
	writer = csv.writer(file, lineterminator = '\n',)
	writer.writerow(["Company","Domain"])

	i = 0
	for company in companies:
		prefix = str((i+1)) + '/' + str(companyCount)
		print(prefix + ' requesting domain for: ' + company + ' ' * 100 , end='\r', flush=True)
		domain = requestInfo(company)
		if domain == '':
			not_found_count += 1 
		writer.writerow([company.strip().rstrip(),domain.strip().rstrip()])
		i += 1
	print('\n*************Execution Summary****************')
	print('Total companies searched: ' + str(len(companies)))
	print('Total domains found: ' + str(len(companies) - not_found_count))
	print('Total domains missing: ' + str(not_found_count))
	print('execution output can be found at ' + outputFilename + '.csv')



