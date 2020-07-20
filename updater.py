import argparse
import pandas as pd

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


args = parser.parse_args()

if args.command == "python":
	df_python = pd.read_csv("updated/python.csv", sep=',', encoding='cp1252', index_col=False)
	if args.name not in df_python["name"].tolist():
		
		df_update_python = {"name": args.name, "desp":args.desp, "example_input":args.example
				   , "example_output": args.example_output, "Syntax":args.syntax
				   ,  "Parameters": args.parameters, "param_description": args.param_desp}

		df_python = df_python.append(df_update_python, ignore_index=True)
		df_python.to_csv("updated/python.csv", index=False)
		print("*** Successfully added to the Database ***")
	else:
		print("Error: " + args.name + " already exists in Database")

if args.command == "node":
	df_nodejs = pd.read_csv("updated/nodeJS.csv", sep=',', encoding='cp1252')
	if args.name not in df_nodejs["name"].tolist():
		
		df_update_node = {"name": args.name, "desp":args.desp, "example_input":args.example
				   , "example_output": args.example_output, "Syntax":args.syntax, "module": args.module
				   ,  "Parameters": args.parameters, "param_description": args.param_desp}

		df_nodejs = df_nodejs.append(df_update_node, ignore_index=True)
		df_nodejs.to_csv("updated/nodeJS.csv", index=False)
		print("*** Successfully added to the Database ***")
	else:
		print("Error: " + args.name + " already exists in Database")

if args.command == "cpp":
	df_cpp = pd.read_csv("updated/cpp.csv", sep=',')
	if args.name not in df_cpp["name"].tolist():
		
		df_update_cpp = {"name": args.name, "desp":args.desp, "example":args.example
				   , "output": args.example_output, "synx":args.syntax
				   , "module": args.module, "parameter": args.parameters}

		df_cpp = df_cpp.append(df_update_cpp, ignore_index=True)
		df_cpp.to_csv("updated/cpp.csv", index=False)
		print("*** Successfully added to the Database ***")
	else:
		print("Error: " + args.name + " already exists in Database")


if args.command == "html":

	df_html = pd.read_csv("updated/html.csv", sep=',', encoding='cp1252')
	if args.name not in df_html["name"].tolist():
		if args.tag is None:
			tag = "<" + args.name + ">"
		else:
			tag = args.tag
		df_update_html = {"name": args.name, "desp":args.desp
						  , "example_input":args.example, "tag":tag }

		df_html = df_html.append(df_update_html, ignore_index=True)
		df_html.to_csv("updated/html.csv", index=False)
		print("*** Successfully added to the Database ***")
	else:
		print("Error: " + args.name + " already exists in Database")
