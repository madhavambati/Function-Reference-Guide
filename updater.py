import argparse
import pandas as pd

# Created a CLI for updating databases using argparser 
# user has to specify different details about the function he/she desires to add in the DB
# The CLI form is created as mentioned below
# There are 4 subparsers namely python, cpp, node, html
# Each subparser has arguments for the user to add a function

# python                  cpp 					node 				   html
#   --name 					--name 				  --name 				 --name 					
#   --desp 					--desp 				  --desp 				 --desp
#   --syntax 				--syntax 			  --syntax               --tag
#   --parameters 			--parameters	      --parameters           --example
#   --param_desp 			--example 			  --param_desp
#   --example 				--example_output      --example
#   --example_output 		--module    		  --example_output
#  												  --module					

# --name argument is must to fill for the user and rest of the arguments are optional but recommended to be filled.
# Example: To add a new function in c++ db
# Command in CMD: python updater.py cpp --name "name of fun" --desp "some desp" --syntax "syntax of the fun"
#                 --parameters "parameters that the fun takes" --example "some example"
#                 --example_output "output for the example"  --module "module in which the function belongs"  
# updated Db is stored in "/updated" folder in the root of the project.

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest='command')

py_update = subparser.add_parser("python", help="To add in python database")
py_update.add_argument("--name", help="name of the function", type=str, required=True)
py_update.add_argument("--desp", help="desp of the function", type=str)
py_update.add_argument("--syntax", help="syntax of the function", type=str)
py_update.add_argument("--parameters", help="parameters for the function", type=str)
py_update.add_argument("--param_desp", help="parameter description", type=str)
py_update.add_argument("--example", help="example for the respective function", type=str)
py_update.add_argument("--example_output", help="output for the example", type=str)



node_update = subparser.add_parser("node", help="To add in NodeJS  database")
node_update.add_argument("--name", help="name of the function", type=str, required=True)
node_update.add_argument("--desp", help="desp of the function", type=str)
node_update.add_argument("--syntax", help="syntax of the function", type=str)
node_update.add_argument("--parameters", help="parameters for the function", type=str)
node_update.add_argument("--param_desp", help="parameter description", type=str)
node_update.add_argument("--example", help="example for the respective function", type=str)
node_update.add_argument("--example_output", help="output for the example", type=str)
node_update.add_argument("--module", help="module in which the function belongs", type=str)


cpp_update = subparser.add_parser("cpp", help="To add in C++ database")
cpp_update.add_argument("--name", help="name of the function", type=str, required=True)
cpp_update.add_argument("--desp", help="desp of the function", type=str)
cpp_update.add_argument("--syntax", help="syntax of the function", type=str)
cpp_update.add_argument("--parameters", help="parameters for the function", type=str)
cpp_update.add_argument("--example", help="example for the respective function", type=str)
cpp_update.add_argument("--example_output", help="output for the example", type=str)
cpp_update.add_argument("--module", help="module in which the function belongs", type=str)


html_update = subparser.add_parser("html", help="To add in Html database")
html_update.add_argument("--name", help="name of the function", type=str, required=True)
html_update.add_argument("--desp", help="desp of the function", type=str)
html_update.add_argument("--tag", help="syntax of the function", type=str)
html_update.add_argument("--example", help="example for the respective function", type=str)

delete_function = subparser.add_parser("del", help="To delete function from database")
delete_function.add_argument("--db", help="name of the db to be deleted from, available db's are: python, cpp, node, html", type=str, required=True)
delete_function.add_argument("--name", help="name of the function  to be deleted from the respective Db", type=str, required=True)

args = parser.parse_args()

def delete(db, function_name):

	if function_name in db.index.tolist():
		db.drop([function_name], inplace=True)
		print("*** Successfully deleted from the Database ***\n")
		print("Updates will be reflected after 12am today automatically")
		print("To see the updates immediately please run \"auto_updater.py\" file")
		return db
	else:
		return None

if args.command == "python":
	df_python = pd.read_csv("updated/python.csv", index_col=False)
	if args.name not in df_python["name"].tolist():
		
		df_update_python = {"name": args.name, "desp":args.desp, "example_input":args.example
				   , "example_output": args.example_output, "Syntax":args.syntax
				   ,  "Parameters": args.parameters, "param_description": args.param_desp}

		df_python = df_python.append(df_update_python, ignore_index=True)
		df_python.to_csv("updated/python.csv", index=False, encoding="utf-8")
		print("*** Successfully added to the Database ***\n")
		print("Updates will be reflected after 12am today automatically")
		print("To see the updates immediately please run \"auto_updater.py\" file")
	else:
		print("Error: " + args.name + " already exists in Database")

if args.command == "node":
	df_nodejs = pd.read_csv("updated/nodeJS.csv", index_col=False)
	if args.name not in df_nodejs["name"].tolist():
		
		df_update_node = {"name": args.name, "desp":args.desp, "example_input":args.example
				   , "example_output": args.example_output, "Syntax":args.syntax, "module": args.module
				   ,  "Parameters": args.parameters, "param_description": args.param_desp}

		df_nodejs = df_nodejs.append(df_update_node, ignore_index=True)
		df_nodejs.to_csv("updated/nodeJS.csv", index=False, encoding="utf-8")
		print("*** Successfully added to the Database ***\n")
		print("Updates will be reflected after 12am today automatically")
		print("To see the updates immediately please run \"auto_updater.py\" file")
	else:
		print("Error: " + args.name + " already exists in Database")

if args.command == "cpp":
	df_cpp = pd.read_csv("updated/cpp.csv", index_col=False)
	if args.name not in df_cpp["name"].tolist():
		
		df_update_cpp = {"name": args.name, "desp":args.desp, "example":args.example
				   , "output": args.example_output, "synx":args.syntax
				   , "module": args.module, "parameter": args.parameters}

		df_cpp = df_cpp.append(df_update_cpp, ignore_index=True)
		df_cpp.to_csv("updated/cpp.csv", index=False, encoding="utf-8")
		print("*** Successfully added to the Database ***\n")
		print("Updates will be reflected after 12am today automatically")
		print("To see the updates immediately please run \"auto_updater.py\" file")
	else:
		print("Error: " + args.name + " already exists in Database")


if args.command == "html":

	df_html = pd.read_csv("updated/html.csv", index_col=False)
	if args.name not in df_html["name"].tolist():
		if args.tag is None:
			tag = "<" + args.name + ">"
		else:
			tag = args.tag
		df_update_html = {"name": args.name, "desp":args.desp
						  , "example_input":args.example, "tag":tag }

		df_html = df_html.append(df_update_html, ignore_index=True)
		df_html.to_csv("updated/html.csv", index=False, encoding="utf-8")
		print("*** Successfully added to the Database ***\n")
		print("Updates will be reflected after 12am today automatically")
		print("To see the updates immediately please run \"auto_updater.py\" file")
	else:
		print("Error: " + args.name + " already exists in Database")

if args.command == "del":

	function = str(args.name)
	
	if args.db == "python":
		df_python = pd.read_csv("updated/python.csv", index_col="name")
		df_python = delete(df_python, function)
		if df_python is not None:
			df_python.to_csv("updated/python.csv", encoding="utf-8")
		else:
			print(function + " is not found in "+ args.db +" database.")

	if args.db == "cpp":
		df_cpp = pd.read_csv("updated/cpp.csv", index_col="name")
		df_cpp = delete(df_cpp, function)
		if df_cpp is not None:
			df_cpp.to_csv("updated/cpp.csv", encoding="utf-8")
		else:
			print(function + " is not found in "+ args.db +" database.")

	if args.db == "node":

		df_nodejs = pd.read_csv("updated/nodeJS.csv", index_col="name")
		df_nodejs = delete(df_nodejs, function)
		if df_nodejs is not None:
			df_nodejs.to_csv("updated/nodeJS.csv", encoding="utf-8")
		else:
			print(function + " is not found in "+ args.db +" database.")

	if args.db == "html":
		df_html = pd.read_csv("updated/html.csv", index_col="name")
		df_html = delete(df_html, function)
		if df_html is not None:
			df_html.to_csv("updated/html.csv", encoding="utf-8")
		else:
			print(function + " is not found in "+ args.db +" database.")

	data = args.db
	if data != "python" and data != "cpp" and  data != "node" and  data != "html":
		print(" db name error")
		print(" available db names are:")
		print(" python \n cpp \n node \n html \n")



