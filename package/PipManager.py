import json
import subprocess
import platform

class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

import json

def parse_pip_freeze_output_to_json(output):
    packages = {}
    for line in output.split('\n'):
        line = line.strip()
        if line:
            package_name, package_version = line.split('==', 1)
            if package_name in packages:
                packages[package_name].append(package_version)
            else:
                packages[package_name] = [package_version]
    return packages

def run_commands_and_get_first_output(commands):
    output = {
     "sucess": False,
     "output": None
    }

    for command in commands:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            output["output"] = result.stdout
            output["sucess"] = True
            break
        else:
           output["output"] = result.stderr
           if platform.system() == 'Windows':
            if not result.returncode == 9009:
             output["output"] = result.stderr
           else:
            if not result.returncode == 127:
             output["output"] = result.stderr
    return output

def install_module(name):
    output = run_commands_and_get_first_output(["pip install " + name, "python -m pip install " + name, "py -m pip install " + name])
    if output["sucess"]:
      return output["output"]
    else:
      raise CustomError("Install Error for " + name + ": " + output["output"])

def uninstall_module(name):
    output = run_commands_and_get_first_output(["pip uninstall " + name, "python -m pip uninstall " + name, "py -m pip uninstall " + name])
    if output["sucess"]:
      return output["output"]
    else:
      raise CustomError("Uninstall Error for " + name + ": " + output["output"])

def get_module_versions():
    output = run_commands_and_get_first_output(["pip freeze", "python -m pip freeze", "py -m pip freeze"])
    if output["sucess"]:
       return parse_pip_freeze_output_to_json(output["output"])
    else:
       raise CustomError("Module Version Error: " + output["output"])

def get_modules():
    output = run_commands_and_get_first_output(["pip freeze", "python -m pip freeze", "py -m pip freeze"])
    if output["sucess"]:
       return list(parse_pip_freeze_output_to_json(output["output"]).keys())
    else:
       raise CustomError("Module List Error: " + output["output"])
