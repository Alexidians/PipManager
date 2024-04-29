import sys
import PipManager
output = {}
if(not len(sys.argv) >= 1):
    print("[error] incorrect amount of arguments provided. provided:" + len(sys.argv) + " expected: ")
exit()
if(sys.argv[1] == "install"):
    if(not len(sys.argv) >= 2):
     print("[error] incorrect amount of arguments provided. provided:" + len(sys.argv) + " expected: atleast 2")
    exit()
    try:
     output = PipManager.install_module(sys.argv[2])
    except Exception as e:
     print("[error] An exception has accoured")
     output["output"] = e
    print(output["output"])
if(sys.argv[1] == "uninstall"):
    if(not len(sys.argv) >= 2):
     print("[error] incorrect amount of arguments provided. provided:" + len(sys.argv) + " expected: atleast 2")
    exit()
    try:
     output = PipManager.uninstall_module(sys.argv[2])
    except Exception as e:
     print("[error] An exception has accoured")
     output["output"] = e
    print(output["output"])
if(sys.argv[1] == "modules"):
    if(not len(sys.argv) >= 1):
     print("[error] incorrect amount of arguments provided. provided:" + len(sys.argv) + " expected: atleast 1")
    exit()
    output = PipManager.get_modules()
    print(output)
if(sys.argv[1] == "module_versions"):
    if(not len(sys.argv) >= 1):
     print("[error] incorrect amount of arguments provided. provided:" + len(sys.argv) + " expected: atleast 1")
    exit()
    output = PipManager.get_module_versions()
    print(output)
